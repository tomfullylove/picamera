from signal import pause
from gpiozero import Button
from adafruit_ads1x15.analog_in import AnalogIn

from utils.logger import logger

from hardware import screen, channel_0
from settings import ISO, ShutterSpeed

logger.info("App initialising")

button = Button(17)
iso = ISO(screen)
button.when_pressed = lambda: (iso.cycle(), logger.info("ISO cycled"))

shutter_speed = ShutterSpeed(channel_0, 26301)
# button.when_pressed = lambda: logger.info(f"Shutter speed: {shutter_speed.value}")

logger.info("App ready")

pause()