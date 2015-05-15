import logging
import socket

class IMClient(object):
    def __init__(self):
        self.logger = logging.getLogger(__name__ + '.' + self.__class__.__name__)
        self.__server_addr = None
        self.__username = None
        self.__friend_addr = None

    @property
    def friend_addr(self):
        """
        Returns the current address of the friend to connect to

        :return: Friend address
        :rtype: str
        """
        return self.__friend_addr

    @friend_addr.setter
    def friend_addr(self, address):
        """
        Checks for a valid ip address, then sets the friend address if
        it is valid

        :param address: Friend address to connect to
        :type address: str

        :return: None
        :rtype: None
        """
        if addr_format(address):
            try:
                socket.inet_aton(address)
                self.__friend_addr = address
            except socket.error:
                self.logger.error('Invalid Friend IP address')
        else:
            self.logger.error('Invalid Friend IP address. Must be in IPv4 format')

    @property
    def server_addr(self):
        """
        Returns the current server address

        :return: Server address
        :rtype: str
        """
        return self.__server_addr

    @server_addr.setter
    def server_addr(self, address):
        """
        Checks for a valid ip address, then sets the address if
        it is valid

        :param address: Server address to connect to
        :type address: str

        :return: None
        :rtype: None
        """
        if addr_format(address):
            try:
                socket.inet_aton(address)
                self.__server_addr = address
            except socket.error:
                self.logger.error('Invalid Server IP address')
        else:
            self.logger.error('Invalid Server IP address. Must be in IPv4 format')

    @property
    def username(self):
        """
        Returns the username that will be displayed with message

        :return: Username
        :rtype: str
        """
        return self.__username

    @username.setter
    def username(self, uname):
        """
        Sets the username if the username is a string that is 10
        or less characters

        :param uname: Username
        :type uname: str

        :return: None
        :rtype: None
        """
        if isinstance(uname, str):
            if len(uname) <= 10:
                self.__username = uname
            else:
                self.logger.error('User name is too long')
        else:
            self.logger.error('User name needs to be a string')

def addr_format(address):
    """
    Verifies the format of the given IP address

    :param address: IP address to verify
    :type address: str

    :return: True if valid format
    :rtype: bool
    """
    if not isinstance(address, str):
        return False
    fields = address.split('.')

    if len(fields) < 4:
        return False
    else:
        return True

