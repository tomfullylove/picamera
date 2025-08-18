import os, signal, subprocess
from utils.logger import logger

class Camera:
    def __init__(self, gain_value):
        self.gain = gain_value
        self.proc = None


    def _cmd(self):
        output_directory = Path(BASE_DIR) / "images"
        output_directory.mkdir(parents=True, exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_pattern = str(output_directory / f"frame_{timestamp}_%06d.dng")

        return [
            "rpicam-still",
            "--nopreview",
            "-t", "0",
            "--signal",
            "--raw",
            "--output", output_pattern,
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