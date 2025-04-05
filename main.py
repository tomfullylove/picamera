from signal import pause
from st7789 import ST7789 as Screen, BG_SPI_CS_FRONT
from gpiozero import Button

from settings import ISO

screen = Screen(
     	height=240,
      	rotation=90,
     	port=0,
    	cs=BG_SPI_CS_FRONT,
	dc=9,
	backlight=18,
	spi_speed_hz=80 * 1000 * 1000,
	offset_left=0,
	offset_top=0,
)
button = Button(17)

iso = ISO(screen)
button.when_pressed = iso.cycle

pause()