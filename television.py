class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3
    def __init__(self) -> None:
        self.__status = False
        self.__muted = False
        self.volume = Television.MIN_VOLUME
        self.channel = Television.MIN_CHANNEL

    def power(self):
        """
        Method to controll the power.
        """
        if self.__status:
            self.__status = False
        else:
            self.__status = True

    def mute(self):
        """
        Method to mute and unmute the tv when it't on.
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
            else:
                self.__muted = True

    def channel_up(self):
        """
        Method to increase the tv channel.
        """
        if self.__status:
            self.__muted = False
            if self.channel == 3:
                self.channel = Television.MIN_CHANNEL
            else:
                self.channel += 1

    def channel_down(self):
        """
        Method to decrease the tv channel.
        """
        if self.__status:
            self.__muted = False
            if self.channel == 0:
                self.channel = Television.MAX_CHANNEL
            else:
                self.channel -= 1

    def volume_up(self):
        """
        Method to increase the tv volume.
        """
        if self.__status:
            self.__muted = False
            if self.volume < Television.MAX_VOLUME:
                self.volume += 1
            else:
                self.volume = Television.MAX_VOLUME

    def volume_down(self):
        """
        Method to decrease the tv volume.
        """
        if self.__status:
            self.__muted = False
            if self.volume > Television.MIN_VOLUME:
                self.volume -= 1
            else:
                self.volume = Television.MIN_VOLUME

    def __str__(self):
        """
        Method to display the resulting tv object.
        """
        if self.__muted:
            return f'Power = {self.__status}, Channel = {self.channel}, Volume = {Television.MIN_VOLUME}'
        else:
            return f'Power = {self.__status}, Channel = {self.channel}, Volume = {self.volume}'

