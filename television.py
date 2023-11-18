class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3
    def __init__(self) -> None:
<<<<<<< Updated upstream
        pass

    def power(self):
        pass
=======
        self.__status = False
        self.__muted = False
        self.volume = Television.MIN_VOLUME
        self.channel = Television.MIN_CHANNEL

    def power(self):
        """
        Method to controll the power.
        """
        self.__status = True
        
>>>>>>> Stashed changes

    def mute(self):
        pass

    def channel_up(self):
<<<<<<< Updated upstream
=======
        """
        Method to increase the tv channel.
        """
>>>>>>> Stashed changes
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