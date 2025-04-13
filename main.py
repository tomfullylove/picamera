from signal import pause

from utils.logger import logger

from hardware import screen, gain_button, shutter_dial
from settings import Gain, ShutterSpeed

logger.info("App initialising")

gain = Gain(screen)
gain_button.when_pressed = lambda: (gain.cycle(), logger.info(f"Gain cycled: {gain.value}"))

shutter_speed = ShutterSpeed(shutter_dial, 0, 17500)
# gain_button.when_pressed = lambda: logger.info(f"Shutter speed: {shutter_speed.value}")

logger.info("App ready")

pause()