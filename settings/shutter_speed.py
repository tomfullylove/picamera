class ShutterSpeed:
    dial = None

    min_value = None
    max_value = None

    values = [1000, 2000, 4000, 8000, 16667, 33333, 66667, 125000, 250000, 500000, 1000000]

    def __init__(self, dial, min_value, max_value):
        self.dial = dial
        self.min_value = min_value
        self.max_value = max_value

    @property
    def value(self):
        normalized = (self.dial.value - self.min_value) / (self.max_value - self.min_value)
        percentage = normalized * 100

        max_index = len(self.values) - 1
        index = round(((max_index) * (100 - percentage)) / 100)
        return self.values[index]
