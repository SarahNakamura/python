class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3
    def __init__(self) -> None:
        self.__muted = False
        self.volume = Television.MIN_VOLUME

    def power(self):
        """
        Method to controll the power.
        """
        pass

    def mute(self):
        pass

    def channel_up(self):
        """
        Methof to increase the tv channel.
        """
        pass

    def channel_down(self):
        pass

    def volume_up(self):
        pass

    def volume_down(self):
        pass

    def __str__(self):
        if self.__muted:
            return f'Volume = {Television.MIN_VOLUME}'
        else:
            return f'xxx'