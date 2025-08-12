import atexit
from utils.logger import logger
from hardware import screen, gain_button, shutter_button
from settings import Gain, Camera

logger.info("App initialising")

gain = Gain(screen)

camera = Camera(gain.value)
camera.start()

atexit.register(camera.stop)

def on_gain_cycle():
    gain.cycle()
    logger.info(f"Gain cycled: {gain.value}")
    camera.set_gain(gain.value)

def on_shutter():
    camera.trigger()
    logger.info("RAW image captured")

gain_button.when_pressed = on_gain_cycle
shutter_button.when_pressed = on_shutter

logger.info("App ready")

from signal import pause
pause()
