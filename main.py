import subprocess
from signal import pause

from utils.logger import logger

from hardware import screen, gain_button, shutter_button
from settings import Gain

def capture(gain):
    command = [
        "rpicam-still",
        "--nopreview",
        "--output", "test.jpg",
        "--analoggain", str(gain),
        "--immediate",
    ]
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as error:
        logger.error(f"Error capturing image: {error}")

logger.info("App initialising")

gain = Gain(screen)
gain_button.when_pressed = lambda: (gain.cycle(), logger.info(f"Gain cycled: {gain.value}"))

shutter_button.when_pressed = lambda: (capture(gain.value), logger.info(f"Image captured"))

logger.info("App ready")

pause()