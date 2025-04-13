from PIL import Image
from st7789 import ST7789 as Screen, BG_SPI_CS_FRONT

class Gain:
	screen = None

	values = [
		{"value": 1, "iso": 100},
		{"value": 2, "iso": 200},
		{"value": 4, "iso": 400},
		{"value": 8, "iso": 800},
		{"value": 16, "iso": 1600},
		{"value": 22, "iso": 3200}
	]
	index = 0

	def __init__(self, screen):
		self.screen = screen
		self.set_image()

	def set_image(self):
		image = Image.open(f"assets/{self.iso}.jpg")
		self.screen.display(image)

	def cycle(self):
		self.index = (self.index + 1) % len(self.values)
		self.set_image()

	@property
	def value(self):
		return self.values[self.index]["value"]

	@property
	def iso(self):
		return self.values[self.index]["iso"]
