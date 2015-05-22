"""
Test for FinalProject
"""
import mock

from source.FinalProject.im_client import IMClient
from source.FinalProject.im_server import IMServer
from source.FinalProject.im_common import HDR_DELIMETER
from unittest import TestCase
from testfixtures import LogCapture


class BaseTest(TestCase):
    def setUp(self):
        self.test_im_client = IMClient()
        self.test_im_server = IMServer(addr='127.0.0.1')

    def tearDown(self):
        self.test_im_server.stop()


class TestFinalProject(BaseTest):
    def test_im_server_address_valid(self):
        self.test_im_client.server_addr = '127.0.0.1'
        self.assertEqual(self.test_im_client.server_addr, '127.0.0.1')

    def test_im_server_address_invalid_format(self):
        with LogCapture() as l:
            self.test_im_client.server_addr = '127.0.0'
            self.assertEqual(self.test_im_client.server_addr, None)

        l.check(
            ('source.FinalProject.im_client', 'ERROR', 'Invalid Server IP address. Must be in IPv4 format'),
        )

    def test_im_server_address_invalid_address(self):
        with LogCapture() as l:
            self.test_im_client.server_addr = '277.11.11.1'
            self.assertEqual(self.test_im_client.server_addr, None)

        l.check(
            ('source.FinalProject.im_client', 'ERROR', 'Invalid Server IP address'),
        )

    def test_im_server_address_float_address(self):
        with LogCapture() as l:
            self.test_im_client.server_addr = 122.22
            self.assertEqual(self.test_im_client.server_addr, None)

        l.check(
            ('source.FinalProject.im_client', 'ERROR', 'Invalid Server IP address. Must be in IPv4 format'),
        )

    def test_user_name_valid(self):
        self.test_im_client.username = 'Krains'
        self.assertEqual(self.test_im_client.username, 'Krains')

    def test_user_name_too_long(self):
        with LogCapture() as l:
            self.test_im_client.username = 'This user name will be too long'
            self.assertEqual(self.test_im_client.username, None)

        l.check(
            ('source.FinalProject.im_client', 'ERROR', 'User name is too long'),
        )

    def test_user_name_invalid_format(self):
        with LogCapture() as l:
            self.test_im_client.username = 123456
            self.assertEqual(self.test_im_client.username, None)

        l.check(
            ('source.FinalProject.im_client', 'ERROR', 'User name needs to be a string'),
        )

    def test_im_friend_name_valid(self):
            self.test_im_client.friend_name = 'my friend'
            self.assertEqual(self.test_im_client.friend_name, 'my friend')

    def test_im_friend_name_too_long(self):
        with LogCapture() as l:
            self.test_im_client.friend_name = 'A name that will be too long'
            self.assertEqual(self.test_im_client.friend_name, None)

        l.check(
            ('source.FinalProject.im_client', 'ERROR', 'Friend name is too long'),
        )

    def test_im_friend_name_invalid_format(self):
        with LogCapture() as l:
            self.test_im_client.friend_name = 12345
            self.assertEqual(self.test_im_client.friend_name, None)

        l.check(
            ('source.FinalProject.im_client', 'ERROR', 'Friend name needs to be a string'),
        )

    def test_connect_server_offline(self):
        with LogCapture() as l:
            self.test_im_client.server_addr = '127.0.0.1'
            self.test_im_client.username = 'kyle'
            self.test_im_client.friend_name = 'friend'
            self.test_im_client.connect()

        l.check(
            ('source.FinalProject.im_client', 'ERROR', 'Server connection failed. Make sure the IM server has been started'),
        )

    def test_connect_server_no_server_addr(self):
        with LogCapture() as l:
            self.test_im_client.username = 'Kyle'
            self.test_im_client.friend_name = 'Friend'
            self.test_im_client.connect()

        l.check(
            ('source.FinalProject.im_client', 'ERROR', 'A server address must be specified before attempting to connect'),
        )

    def test_connect_server_no_username(self):
        with LogCapture() as l:
            self.test_im_client.friend_name = 'Friend'
            self.test_im_client.server_addr = '127.0.0.1'
            self.test_im_client.connect()

        l.check(
            ('source.FinalProject.im_client', 'ERROR', 'A username must be specified before attempting to connect'),
        )

    def test_connect_server_no_friend_name(self):
        with LogCapture() as l:
            self.test_im_client.username = 'Kyle'
            self.test_im_client.server_addr = '127.0.0.1'
            self.test_im_client.connect()

        l.check(
            ('source.FinalProject.im_client', 'ERROR', 'A friend name must be specified before attempting to connect'),
        )

    @mock.patch('socket.socket')
    def test_connect_server(self, mock_sock):
        sock = mock_sock.return_value
        sock.connect.return_value = None
        sock.send.return_value = None
        self.test_im_client.server_addr = '127.0.0.1'
        self.test_im_client.username = 'kyle'
        self.test_im_client.friend_name = 'friend'
        self.test_im_client.connect()

        sock.sendall.assert_called_with('kyle' + HDR_DELIMETER + 'friend' + HDR_DELIMETER + 'True')

    @mock.patch('socket.socket')
    def test_close_im(self, mock_sock):
        sock = mock_sock.return_value
        sock.connect.return_value = None
        sock.sendall.return_value = None
        sock.recv.return_value = 'kyle' + HDR_DELIMETER + 'friend' + HDR_DELIMETER + 'True'
        sock.accept.return_value = sock, [None]
        sock.close.return_value = None
        self.test_im_server.start()
        self.test_im_client.server_addr = '127.0.0.1'
        self.test_im_client.username = 'kyle'
        self.test_im_client.friend_name = 'friend'
        self.test_im_client.connect()
        self.test_im_client.close()

        self.assertFalse(self.test_im_client.connected)

    @mock.patch('socket.socket')
    def test_send_msg_connected(self, mock_sock):
        sock = mock_sock.return_value
        sock.connect.return_value = None
        sock.sendall.return_value = None
        sock.recv.return_value = 'kyle' + HDR_DELIMETER + 'friend' + HDR_DELIMETER + 'True'
        sock.accept.return_value = sock, [None]
        sock.close.return_value = None
        self.test_im_client.friend_connected = True
        self.test_im_server.start()
        self.test_im_client.server_addr = '127.0.0.1'
        self.test_im_client.username = 'kyle'
        self.test_im_client.friend_name = 'friend'
        self.test_im_client.connect()
        self.test_im_client.send_message('test message')

        sock.sendall.assert_called_with('test message')

    @mock.patch('socket.socket')
    def test_send_msg_not_connected(self, mock_sock):
        sock = mock_sock.return_value
        sock.connect.return_value = None
        sock.sendall.return_value = None
        sock.recv.return_value = 'kyle' + HDR_DELIMETER + 'friend' + HDR_DELIMETER + 'True'
        sock.accept.return_value = sock, [None]
        sock.close.return_value = None
        self.test_im_server.start()
        self.test_im_client.server_addr = '127.0.0.1'
        self.test_im_client.username = 'kyle'
        self.test_im_client.friend_name = 'friend'
        self.test_im_client.connect()
        self.test_im_client.send_message('test message')

        sock.sendall.assert_not_called_with('test message')

    def test_client_handle_msg_server_resp_true(self):
        data = HDR_DELIMETER + '1'
        self.test_im_client.handle_message(data)

        self.assertTrue(self.test_im_client.friend_connected)

    def test_client_handle_msg_server_resp_false(self):
        data = HDR_DELIMETER + '0'
        self.test_im_client.handle_message(data)

        self.assertFalse(self.test_im_client.friend_connected)

    def test_client_handle_msg_friend_msg(self):
        with LogCapture() as l:
            data = 'This is a message'
            self.test_im_client.friend_name = 'friend'
            self.test_im_client.handle_message(data)

        l.check(
            ('source.FinalProject.im_client', 'INFO', 'friend> This is a message'),
        )