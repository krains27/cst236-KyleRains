"""
Test for source.pyTona.main
"""
import difflib
import mock

import getpass
from pyTona.main import (Interface, NOT_A_QUESTION_RETURN, UNKNOWN_QUESTION, NO_QUESTION,
                         NO_TEACH)
import pyTona.answer_funcs as answer
from unittest import TestCase
from ReqTracer import requirements
import subprocess

QUESTION_MARK = chr(0x3F)

class MyS(object):
    def connect(self, address):
        pass

class BaseTest(TestCase):
    def setUp(self):
        self.test_pytona = Interface()

    def tearDown(self):
        if answer.seq_finder:
            answer.seq_finder.stop()

class TestPytona(BaseTest):
    @requirements(['#0001'])
    def test_question_as_string(self):
        question_str = 'How is feet in miles ' + QUESTION_MARK
        result = self.test_pytona.ask(question=question_str)
        self.assertNotEqual(result, NOT_A_QUESTION_RETURN)

    @requirements(['#0001'])
    def test_question_as_string_int(self):
        question_int = 10
        with self.assertRaises(Exception):
            self.test_pytona.ask(question=question_int)

    @requirements(['#0002'])
    def test_answer_question_how(self):
        question_str = 'How are you' + QUESTION_MARK
        result = self.test_pytona.ask(question=question_str)
        self.assertNotEqual(result, NOT_A_QUESTION_RETURN)

    @requirements(['#0002'])
    def test_answer_question_what(self):
        question_str = 'What are you' + QUESTION_MARK
        result = self.test_pytona.ask(question=question_str)
        self.assertNotEqual(result, NOT_A_QUESTION_RETURN)

    @requirements(['#0002'])
    def test_answer_question_where(self):
        question_str = 'Where are you' + QUESTION_MARK
        result = self.test_pytona.ask(question=question_str)
        self.assertNotEqual(result, NOT_A_QUESTION_RETURN)

    @requirements(['#0002'])
    def test_answer_question_why(self):
        question_str = 'Why are you doing this' + QUESTION_MARK
        result = self.test_pytona.ask(question=question_str)
        self.assertNotEqual(result, NOT_A_QUESTION_RETURN)

    @requirements(['#0002'])
    def test_answer_question_who(self):
        question_str = 'Who are you' + QUESTION_MARK
        result = self.test_pytona.ask(question=question_str)
        self.assertNotEqual(result, NOT_A_QUESTION_RETURN)

    @requirements(['#0003'])
    def test_invalid_keyword(self):
        question_str = 'Are you going fishing' + QUESTION_MARK
        result = self.test_pytona.ask(question=question_str)
        self.assertEqual(result, NOT_A_QUESTION_RETURN)

    @requirements(['#0004'])
    def test_no_question_mark(self):
        question_str = 'Are you going fishing'
        result = self.test_pytona.ask(question=question_str)
        self.assertEqual(result, NOT_A_QUESTION_RETURN)

    @requirements(['#0005'])
    def test_broken_down_question(self):
        expected_result = 'Who are you'
        question_str = 'Who are you ' + QUESTION_MARK
        self.test_pytona.ask(question=question_str)
        self.assertEqual(expected_result, self.test_pytona.last_question)

    @requirements(['#0006'])
    def test_answer_question_90_percent(self):
        question_str = 'Who invented Pyt ' + QUESTION_MARK
        # Make sure that the string is 90 percent or higher
        self.assertGreaterEqual(difflib.SequenceMatcher(a='Who invented Pyt', b='Who invented Python').ratio(), .9)
        result = self.test_pytona.ask(question=question_str)
        self.assertEqual(result, 'Guido Rossum(BDFL)')

    @requirements(['#0006'])
    def test_answer_question_less_90_percent(self):
        question_str = 'Who invented Py' + QUESTION_MARK
        # Make sure that the string is less than 90 percent
        self.assertLessEqual(difflib.SequenceMatcher(a='Who invented Py', b='Who invented Python').ratio(), .9)
        result = self.test_pytona.ask(question=question_str)
        self.assertNotEqual(result, 'Guido Rossum(Benevolent Dictator For Life)')

    @requirements(['#0007'])
    def test_exclude_number(self):
        expected_result = 'What is feet in miles'
        question_str = 'What is 322 feet in miles ' + QUESTION_MARK
        self.test_pytona.ask(question=question_str)
        self.assertEqual(expected_result, self.test_pytona.last_question)

    @requirements(['#0007'])
    def test_exclude_number_ending(self):
        expected_result = 'Who invented Python'
        question_str = 'Who invented Python 3 ' + QUESTION_MARK
        self.test_pytona.ask(question=question_str)
        self.assertEqual(expected_result, self.test_pytona.last_question)

    @requirements(['#0008'])
    def test_valid_match(self):
        question_str = 'Who invented Python' + QUESTION_MARK
        result = self.test_pytona.ask(question=question_str)
        self.assertEqual(result, 'Guido Rossum(BDFL)')

    @requirements(['#0009'])
    def test_invalid_match(self):
        question_str = 'Who are you' + QUESTION_MARK
        result = self.test_pytona.ask(question=question_str)
        self.assertEqual(result, UNKNOWN_QUESTION)

    @requirements(['#0010', '#0011'])
    def test_provide_answer_string(self):
        question_str = 'Who are you' + QUESTION_MARK
        self.test_pytona.ask(question=question_str)
        self.test_pytona.teach(answer='I am Groot')
        result = self.test_pytona.ask(question=question_str)
        self.assertEqual(result, 'I am Groot')

    @requirements(['#0011'])
    def test_provide_answer_func(self):
        def conv_num_to_char(num):
            return chr(int(num))

        question_str = 'What is 100 as a character' + QUESTION_MARK
        self.test_pytona.ask(question=question_str)
        self.test_pytona.teach(answer=conv_num_to_char)
        result = self.test_pytona.ask(question=question_str)
        self.assertEqual(result, 'd')

    @requirements(['#0012'])
    def test_provide_answer_no_question(self):
        result = self.test_pytona.teach(answer='I am Groot')
        self.assertEqual(result, NO_QUESTION)

    @requirements(['#0013'])
    def test_answer_to_answered_question(self):
        question_str = 'Who invented Python ' + QUESTION_MARK
        self.test_pytona.ask(question=question_str)
        result = self.test_pytona.teach(answer='A machine')
        self.assertEqual(result, NO_TEACH)

        # Make sure question wasn't changed
        result = self.test_pytona.ask(question=question_str)
        self.assertEqual(result, 'Guido Rossum(BDFL)')

    @requirements(['#0014', '#0015'])
    def test_updating_answer_string(self):
        question_str = 'Who invented Python' + QUESTION_MARK
        result = self.test_pytona.ask(question=question_str)
        self.assertEqual(result, 'Guido Rossum(BDFL)')

        self.test_pytona.correct(answer='A machine')
        result = self.test_pytona.ask(question=question_str)
        self.assertEqual(result, 'A machine')

    @requirements(['#0015'])
    def test_updating_answer_func(self):
        def answer_func():
            return 'A machine'

        question_str = 'Who invented Python' + QUESTION_MARK
        result = self.test_pytona.ask(question=question_str)
        self.assertEqual(result, 'Guido Rossum(BDFL)')

        self.test_pytona.correct(answer=answer_func)
        result = self.test_pytona.ask(question=question_str)
        self.assertEqual(result, 'A machine')

    @requirements(['#0016'])
    def test_updating_answer_no_question(self):
        result = self.test_pytona.correct(answer='A machine')
        self.assertEqual(result, NO_QUESTION)

    @requirements(['#0017'])
    def test_answer_to_feet_question(self):
        miles_val = 500.0/5280.0
        question_str = 'What is 500 feet in miles' + QUESTION_MARK
        result = self.test_pytona.ask(question=question_str)
        self.assertEqual(result, '{} miles'.format(miles_val))

    @requirements(['#0017'])
    def test_answer_to_feet_question_neg(self):
        miles_val = -500.0/5280.0
        question_str = 'What is -500 feet in miles' + QUESTION_MARK
        result = self.test_pytona.ask(question=question_str)
        self.assertEqual(result, '{} miles'.format(miles_val))

    @requirements(['#0019'])
    def test_answer_to_python_question_valid(self):
        question_str = 'Who invented Python' + QUESTION_MARK
        result = self.test_pytona.ask(question=question_str)
        self.assertEqual(result, 'Guido Rossum(BDFL)')

    @requirements(['#0020'])
    def test_answer_to_understand_question_valid(self):
        question_str = 'Why don\'t you understand me' + QUESTION_MARK
        result = self.test_pytona.ask(question=question_str)
        self.assertEqual(result, 'Because you do not speak 1s and 0s')

    @requirements(['#0021'])
    def test_answer_to_shutdown_question_valid(self):
        question_str = 'Why don\'t you shutdown' + QUESTION_MARK
        result = self.test_pytona.ask(question=question_str)
        self.assertEqual(result, 'I\'m afraid I can\'t do that {}'.format(getpass.getuser()))

    @requirements(['#0022'])
    @mock.patch('subprocess.Popen')
    def test_answer_to_where_am_question(self, mock_popen):
        process_mock = mock.Mock()
        attrs = {'communicate.return_value': ['Lab4']}
        process_mock.configure_mock(**attrs)
        mock_popen.return_value = process_mock
        question_str = 'Where am I ' + QUESTION_MARK
        result = self.test_pytona.ask(question=question_str)
        self.assertEqual(result, 'Lab4')

    @requirements(['#0022'])
    @mock.patch('subprocess.Popen')
    def test_answer_to_where_am_question_unknown_no_exception(self, mock_popen):
        process_mock = mock.Mock()
        attrs = {'communicate.return_value': [None]}
        process_mock.configure_mock(**attrs)
        mock_popen.return_value = process_mock
        question_str = 'Where am I ' + QUESTION_MARK
        result = self.test_pytona.ask(question=question_str)
        self.assertEqual(result, 'Unknown')

    @requirements(['#0022'])
    @mock.patch('subprocess.Popen')
    def test_answer_to_where_am_question_unknown_exception(self, mock_popen):
        process_mock = mock.Mock()
        attrs = {'communicate.side_effect': Exception}
        process_mock.configure_mock(**attrs)
        mock_popen.return_value = process_mock
        question_str = 'Where am I ' + QUESTION_MARK
        result = self.test_pytona.ask(question=question_str)
        self.assertEqual(result, 'Unknown')

    @requirements(['#0023'])
    @mock.patch('subprocess.Popen')
    def test_answer_to_where_you_question(self, mock_popen):
        process_mock = mock.Mock()
        attrs = {'communicate.return_value': ['https://github.com/krains27/cst236-KyleRains']}
        process_mock.configure_mock(**attrs)
        mock_popen.return_value = process_mock
        question_str = 'Where are you ' + QUESTION_MARK
        result = self.test_pytona.ask(question=question_str)
        self.assertEqual(result, 'https://github.com/krains27/cst236-KyleRains')

    @requirements(['#0023'])
    @mock.patch('subprocess.Popen')
    def test_answer_to_where_you_question_exception(self, mock_popen):
        process_mock = mock.Mock()
        attrs = {'communicate.side_effect': Exception}
        process_mock.configure_mock(**attrs)
        mock_popen.return_value = process_mock
        question_str = 'Where are you ' + QUESTION_MARK
        result = self.test_pytona.ask(question=question_str)
        self.assertEqual(result, 'Unknown')

    @requirements(['#0023'])
    @mock.patch('subprocess.Popen')
    def test_answer_to_where_you_question_no_exception(self, mock_popen):
        process_mock = mock.Mock()
        attrs = {'communicate.return_value': [None]}
        process_mock.configure_mock(**attrs)
        mock_popen.return_value = process_mock
        question_str = 'Where are you ' + QUESTION_MARK
        result = self.test_pytona.ask(question=question_str)
        self.assertEqual(result, 'Unknown')

    @requirements(['#0024', '#0026'])
    @mock.patch('socket.socket')
    def test_answer_to_who_else(self, test):
        m = test.return_value
        m.connect.return_value = None
        m.send.return_value = None
        m.recv.return_value = 'Kyle$Brit$Alex$Josh'
        question_str = 'Who else is here ' + QUESTION_MARK
        result = self.test_pytona.ask(question=question_str)
        self.assertEqual(['Kyle', 'Brit', 'Alex', 'Josh'], result)

    @requirements(['#0025'])
    @mock.patch('socket.socket')
    def test_answer_to_who_else_connection_call(self, test):
        m = test.return_value
        m.connect.return_value = None
        m.send.return_value = None
        m.recv.return_value = 'A$B$C$D'
        question_str = 'Who else is here ' + QUESTION_MARK
        self.test_pytona.ask(question=question_str)
        m.send.assert_called_with('Who?')
        m.connect.assert_called_with(('192.168.64.3', '1337'))

    @requirements(['#0027'])
    @mock.patch('socket.socket')
    def test_answer_to_who_else_exception(self, test):
        m = test.return_value
        m.connect.side_effect = Exception
        question_str = 'Who else is here ' + QUESTION_MARK
        result = self.test_pytona.ask(question=question_str)
        self.assertEqual(result, 'IT\'S A TRAAAPPPP')

    @requirements(['#0028'])
    def test_fibonacci_answer_0(self):
        question_str = 'What is the 0 digit of the Fibonacci Sequence ' + QUESTION_MARK
        result = self.test_pytona.ask(question=question_str)
        self.assertEqual(result, 0)

    @requirements(['#0028'])
    def test_fibonacci_answer_1(self):
        question_str = 'What is the 1 digit of the Fibonacci Sequence ' + QUESTION_MARK
        result = self.test_pytona.ask(question=question_str)
        self.assertEqual(result, 1)

    @requirements(['#0029'])
    def test_fibonacci_answer_thinking(self):
        with mock.patch('pyTona.answer_funcs.random.randint') as mock_random:
            mock_random.return_value = 10
            question_str = 'What is the 15 digit of the Fibonacci Sequence ' + QUESTION_MARK
            result = self.test_pytona.ask(question=question_str)
            self.assertEqual(result, 'Thinking...')

    @requirements(['#0029'])
    def test_fibonacci_answer_one_second(self):
        with mock.patch('pyTona.answer_funcs.random.randint') as mock_random:
            mock_random.return_value = 5
            question_str = 'What is the 15 digit of the Fibonacci Sequence ' + QUESTION_MARK
            result = self.test_pytona.ask(question=question_str)
            self.assertEqual(result, 'One second')

    @requirements(['#0029'])
    def test_fibonacci_answer_cool_jets(self):
        with mock.patch('pyTona.answer_funcs.random.randint') as mock_random:
            mock_random.return_value = 2
            question_str = 'What is the 15 digit of the Fibonacci Sequence ' + QUESTION_MARK
            result = self.test_pytona.ask(question=question_str)
            self.assertEqual(result, 'cool your jets')

    @requirements(['#0030'])
    def test_too_may_params(self):
        with self.assertRaises(Exception) as error:
            question_str = 'What is the 15 15 digit of the Fibonacci Sequence ' + QUESTION_MARK
            result = self.test_pytona.ask(question=question_str)
