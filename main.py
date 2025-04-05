from signal import pause
from gpiozero import Button
from adafruit_ads1x15.analog_in import AnalogIn

from utils.logger import logger

from hardware import screen, channel_0
from settings import ISO

logger.info("App initialising")

button = Button(17)
iso = ISO(screen)
button.when_pressed = lambda: (iso.cycle(), logger.info("ISO cycled"))

max_value = 26301
percentage = int((channel_0.value / 26301) * 100)

logger.info(f"percentage: {percentage}")

logger.info("App ready")

pause()