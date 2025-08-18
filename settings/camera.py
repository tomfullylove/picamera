import os, signal, subprocess
from utils.logger import logger

class Camera:
    def __init__(self, gain_value):
        self.gain = gain_value
        self.proc = None

    def _cmd(self):
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        return [
            "rpicam-still",
            "--nopreview",
            "-t", "0",
            "--signal",
            "--raw",
            "--output", "/home/picamera/images/{timestamp}_%06d.dng",
            "--analoggain", str(self.gain),
        ]

    def start(self):
        if self.proc and self.proc.poll() is None:
            return
        self.proc = subprocess.Popen(
            self._cmd(),
        )

    def stop(self):
        if self.proc and self.proc.poll() is None:
            self.proc.terminate()
            try:
                self.proc.wait(timeout=2)
            except subprocess.TimeoutExpired:
                self.proc.kill()
        self.proc = None

    def trigger(self):
        self.start()
        os.kill(self.proc.pid, signal.SIGUSR1)

    def set_gain(self, new_gain):
        self.gain = new_gain
        self.stop()
        self.start()