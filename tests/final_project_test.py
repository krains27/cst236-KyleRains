"""
Test for FinalProject
"""
from source.FinalProject.im_client import IMClient
from unittest import TestCase
from testfixtures import LogCapture
import mock


class BaseTest(TestCase):
    def setUp(self):
        self.test_im_client = IMClient()

    def tearDown(self):
        pass


class TestFinalProject(BaseTest):
    def test_im_server_address_valid(self):
        self.test_im_client.server_addr = '127.0.0.1'
        self.assertEqual(self.test_im_client.server_addr, '127.0.0.1')

    def test_im_server_address_invalid_format(self):
        with LogCapture() as l:
            self.test_im_client.server_addr = '127.0.0'
            self.assertEqual(self.test_im_client.server_addr, None)

        l.check(
            ('source.FinalProject.im_client.IMClient', 'ERROR', 'Invalid Server IP address. Must be in IPv4 format'),
        )

    def test_im_server_address_invalid_address(self):
        with LogCapture() as l:
            self.test_im_client.server_addr = '277.11.11.1'
            self.assertEqual(self.test_im_client.server_addr, None)

        l.check(
            ('source.FinalProject.im_client.IMClient', 'ERROR', 'Invalid Server IP address'),
        )

    def test_im_server_address_float_address(self):
        with LogCapture() as l:
            self.test_im_client.server_addr = 122.22
            self.assertEqual(self.test_im_client.server_addr, None)

        l.check(
            ('source.FinalProject.im_client.IMClient', 'ERROR', 'Invalid Server IP address. Must be in IPv4 format'),
        )

    def test_user_name_valid(self):
        self.test_im_client.username = 'Krains'
        self.assertEqual(self.test_im_client.username, 'Krains')

    def test_user_name_too_long(self):
        with LogCapture() as l:
            self.test_im_client.username = 'This user name will be too long'
            self.assertEqual(self.test_im_client.username, None)

        l.check(
            ('source.FinalProject.im_client.IMClient', 'ERROR', 'User name is too long'),
        )

    def test_user_name_invalid_format(self):
        with LogCapture() as l:
            self.test_im_client.username = 123456
            self.assertEqual(self.test_im_client.username, None)

        l.check(
            ('source.FinalProject.im_client.IMClient', 'ERROR', 'User name needs to be a string'),
        )

    def test_im_friend_address_valid(self):
            self.test_im_client.friend_addr = '127.0.0.1'
            self.assertEqual(self.test_im_client.friend_addr, '127.0.0.1')

    def test_im_friend_address_invalid_format(self):
        with LogCapture() as l:
            self.test_im_client.friend_addr = '127.0.0'
            self.assertEqual(self.test_im_client.friend_addr, None)

        l.check(
            ('source.FinalProject.im_client.IMClient', 'ERROR', 'Invalid Friend IP address. Must be in IPv4 format'),
        )

    def test_im_friend_address_invalid_address(self):
        with LogCapture() as l:
            self.test_im_client.friend_addr = '277.11.11.1'
            self.assertEqual(self.test_im_client.friend_addr, None)

        l.check(
            ('source.FinalProject.im_client.IMClient', 'ERROR', 'Invalid Friend IP address'),
        )

    def test_im_friend_address_float_address(self):
        with LogCapture() as l:
            self.test_im_client.friend_addr = 122.22
            self.assertEqual(self.test_im_client.friend_addr, None)

        l.check(
            ('source.FinalProject.im_client.IMClient', 'ERROR', 'Invalid Friend IP address. Must be in IPv4 format'),
        )

    '''def test_connect_server_offline(self):
        with LogCapture as l:
            self.test_im_client.server_addr = '127.0.0.1'
            self.test_im_client.friend_addr = '127.0.0.1'''''
