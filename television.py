class Television:
    MIN_VOLUME = 0
    def __init__(self) -> None:
        self.__muted = False
        self.volume = Television.MIN_VOLUME

    def power(self):
        """
        Method to controll the power.
        """
        pass

    def mute(self):
        """
        Method to mute the volume.
        """
        pass

    def channel_up(self):
        """
        Methof to increase the tv channel.
        """
        pass

    def channel_down(self):
        """
        Method to decrease the tv channel.
        """
        pass

    def volume_up(self):
        """
        Method to increase the volume.
        """
        pass

    def volume_down(self):
        """
        Method to decrease the volume.
        """
        pass

    def __str__(self):
        """
        Method to show the tv status.
        :return: tv status.
        """
        if self.__muted:
            return f'Volume = {Television.MIN_VOLUME}'
        else:
            return f'xxx'