class ShutterSpeed:
    dial = None
    max_dial_value = None

    values = [500, 250, 125, 60, 30, 15]

    def __init__(self, dial, max_dial_value):
        self.dial = dial
        self.max_dial_value = max_dial_value

    @property
    def value(self):
        percentage = int((self.dial.value / self.max_dial_value) * 100)
        max_index = len(self.values) - 1

        index = int(((max_index) * (100 - percentage)) / 100)
        return self.values[index]
