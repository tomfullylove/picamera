from PIL import Image
from st7789 import ST7789 as Screen, BG_SPI_CS_FRONT

class ISO:
	screen = None
	values = [100, 200, 400, 800, 1600, 3200]
	index = 0

	def __init__(self, screen):
		self.screen = screen
		self.set_image()

	def set_image(self):
		image = Image.open(f"assets/{self.value}.jpg")
		self.screen.display(image)

	def cycle(self):
		self.index = (self.index + 1) % len(self.values)
		self.set_image()

	@property
	def value(self):
		return self.values[self.index]