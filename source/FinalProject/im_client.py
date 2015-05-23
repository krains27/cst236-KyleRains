"""
:mod:`source.FinalProject.im_client` -- Module that describes the im client
===========================================================================
This file includes the code that will describe the IM client functionality
"""

import logging
import socket

from im_common import HDR_DELIMETER, SERVER_PORT


class IMClient(object):
    """
    The client class that will allow a user to send messages to a connected friend
    """

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    ch = logging.StreamHandler()
    logger.addHandler(ch)

    def __init__(self):
        self.__server_addr = None
        self.__username = None
        self.__friend_name = None
        self.__socket = None
        self.connected = False
        self.friend_connected = False
        self.rx_thread = None

    def close(self):
        """
        Closes the socket and exits the program

        :return: None
        :rtype: None
        """
        if self.__socket:
            self.__socket.close()
            self.connected = False

    def connect_info_valid(self):
        """
        Verifies that user has a valid username, friend name, and server address

        :return: True is all info is valid
        :rtype: bool
        """
        if self.server_addr is None:
            self.logger.error('A server address must be specified before attempting to connect')
            return False

        if self.username is None:
            self.logger.error('A username must be specified before attempting to connect')
            return False

        if self.friend_name is None:
            self.logger.error('A friend name must be specified before attempting to connect')
            return False

        return True

    def connect(self, wait_for_friend=True):
        """
        Attempts to connect to the IM server.

        :param wait_for_friend: Determines whether you want to wait for friend if first
            connected
        :type wait_for_friend: bool

        :return: None
        :rtype: None
        """
        if self.connect_info_valid():
            self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_connect_info = (self.server_addr, SERVER_PORT)
            try:
                self.__socket.connect(server_connect_info)
                self.__socket.sendall(self.construct_header_message() + str(wait_for_friend))
                self.connected = True
            except socket.error:
                self.connected = False
                self.logger.error('Server connection failed. Make sure the IM server has been started')

    def construct_header_message(self):
        """
        Constructs and returns the header message

        :return: Header message
        :rtype: str
        """
        return self.username + HDR_DELIMETER + self.friend_name + HDR_DELIMETER

    def handle_message(self, data):
        """
        Handles the incoming data whether it is a server response or and IM

        :param data: Message received from the server
        :type data: str

        :return: None
        :rtype: None
        """
        if data[0] == HDR_DELIMETER:  # Server response
            self.friend_connected = bool(int(data[1:]))
        else:
            self.logger.info(self.friend_name + '> ' + data)

    def send_message(self, msg):
        """
        Sends a message to the friend if the friend is online

        :param msg: Message to send
        :type msg: str

        :return: None
        :rtype: None
        """
        if self.friend_connected:
            self.__socket.sendall(msg)
        else:
            self.logger.info('Friend is not online. Message was not sent')

    @property
    def friend_name(self):
        """
        Returns the current name of the friend to connect to

        :return: Friend address
        :rtype: str
        """
        return self.__friend_name

    @friend_name.setter
    def friend_name(self, name):
        """
        Sets the name of the friend that user is attempting to connect to  if the
        username is a string that is 10 or less characters

        :param name: Username
        :type name: str

        :return: None
        :rtype: None
        """
        if isinstance(name, str):
            if len(name) <= 10:
                self.__friend_name = name
            else:
                self.logger.error('Friend name is too long')
        else:
            self.logger.error('Friend name needs to be a string')

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