class Television:
    __min_volume = 0
    __max_volume = 100
    __min_channel = 1
    __max_channel = 100

    def __init__(self):
        self.__is_on = False
        self.__volume = 30
        self.__channel = 1

    def turn_on(self):
        self.__is_on = True

    def turn_off(self):
        self.__is_on = False

    def is_on(self):
        return self.__is_on

    def check_power(self):
        if not self.__is_on:
            raise Exception("TV is off")

    def increase_volume(self):
        self.check_power()
        if self.__volume < self.__max_volume:
            self.__volume += 1

    def decrease_volume(self):
        self.check_power()
        if self.__volume > self.__min_volume:
            self.__volume -= 1

    def set_channel(self, channel):
        self.check_power()
        if self.__min_channel <= channel <= self.__max_channel:
            self.__channel = channel
        else:
            raise ValueError("Invalid channel")

    def change_channel_up(self):
        self.check_power()
        if self.__min_channel <= self.__channel < self.__max_channel:
            self.__channel += 1

    def change_channel_down(self):
        self.check_power()
        if self.__min_channel < self.__channel <= self.__max_channel:
            self.__channel -= 1

    def get_volume(self):
        return self.__volume

    def get_channel(self):
        return self.__channel