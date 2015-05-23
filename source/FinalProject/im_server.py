"""
:mod:`source.FinalProject.im_server` -- Module that describes the im server
===========================================================================
This file includes the code that will describe the IM server functionality
"""
import logging
import socket
from Queue import Queue

from im_common import SERVER_PORT, NUM_USERS


class IMServer(object):
    """
    The server class that will route messages to and from connected friends

    :param addr: The address of the server
    :type addr: str
    """

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    ch = logging.StreamHandler()
    logger.addHandler(ch)

    def __init__(self, addr):
        self.__server_address = addr
        self.__server_socket = None
        self.__friend_connected = False
        self.user_list = []
        self.msg_queue = Queue()
        self.running = False

    def start(self):
        """
        Starts the process of receiving messages

        :return: None
        :rtype: None
        """
        self.running = True

        self.__server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__server_socket.bind((self.__server_address, SERVER_PORT))
        self.__server_socket.listen(2)

        for _ in range(NUM_USERS):  # Connect 2 users
            conn, addr = self.__server_socket.accept()

    def stop(self):
        """
        Closes the server socket

        :return: None
        :rtype: None
        """
        if self.__server_socket:
            self.__server_socket.close()
            self.running = False