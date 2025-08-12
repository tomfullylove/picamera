import os, signal, subprocess
from utils.logger import logger

class Camera:
    def __init__(self, gain_value):
        self.gain = gain_value
        self.proc = None

    def _cmd(self):
        return [
            "rpicam-still",
            "--nopreview",
            "-t", "0",
            "--signal",
            "--raw",
            "--output", "frame_%06d.dng",
            "--analoggain", str(self.gain),
        ]

    def start(self):
        if self.proc and self.proc.poll() is None:
            return
        self.proc = subprocess.Popen(
            self._cmd(),
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        logger.info(f"rpicam-still started (pid={self.proc.pid}, gain={self.gain})")

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