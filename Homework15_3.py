class TVController:
    def __init__(self, channels):
        self.channels = channels
        self.current_index = 0

    def first_channel(self):
        self.current_index = 0
        return self.channels[self.current_index]

    def last_channel(self):
        self.current_index = len(self.channels) - 1
        return self.channels[self.current_index]

    def turn_channel(self, n):
        if 1 <= n <= len(self.channels):
            self.current_index = n - 1
            return self.channels[self.current_index]
        else:
            return "Канал не существует."

    def next_channel(self):
        self.current_index = (self.current_index + 1) % len(self.channels)
        return self.channels[self.current_index]

    def previous_channel(self):
        self.current_index = (self.current_index - 1) % len(self.channels)
        return self.channels[self.current_index]

    def current_channel(self):
        return self.channels[self.current_index]

    def exists(self, query):
        if isinstance(query, int):
            return "Да" if 1 <= query <= len(self.channels) else "Нет"
        elif isinstance(query, str):
            return "Да" if query in self.channels else "Нет"
        else:
            return "Нет"



CHANNELS = ["BBC", "Discovery", "TV1000"]
controller = TVController(CHANNELS)

print(controller.first_channel())
print(controller.last_channel())
print(controller.turn_channel(1))
print(controller.next_channel())
print(controller.previous_channel())
print(controller.current_channel())
print(controller.exists(4))
print(controller.exists("BBC"))
