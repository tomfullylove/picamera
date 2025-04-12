from signal import pause

from utils.logger import logger

from hardware import screen, iso_button, shutter_dial
from settings import ISO, ShutterSpeed

logger.info("App initialising")

iso = ISO(screen)
iso_button.when_pressed = lambda: (iso.cycle(), logger.info("ISO cycled"))

shutter_speed = ShutterSpeed(shutter_dial, -850, 13900)
# iso_button.when_pressed = lambda: logger.info(f"Shutter speed: {shutter_speed.value}")

logger.info("App ready")

pause()