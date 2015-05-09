"""
Test for source.pyTona.main
"""
import difflib
import mock
import random
import string
import time
import os

import getpass
from pyTona.main import (Interface, NOT_A_QUESTION_RETURN, UNKNOWN_QUESTION, NO_QUESTION,
                         NO_TEACH)
import pyTona.answer_funcs as answer
from pyTona.question_answer import QA
from unittest import TestCase
from ReqTracer import requirements
import data_storage
import subprocess

QUESTION_MARK = chr(0x3F)
LIST_CREATED = False
RAND_QUESTIONS = {}
PERFORMANCE_DATA = {}

THOUSANDTH_FIB_STR = '4346655768693745643568852767504062580256466051737178040248172908' +\
                     '95365554179490518904038798400792551692959225930803226347752096896' +\
                     '23239873322471161642996440906533187938298969649928516003704476137' +\
                     '795166849228875'

THOUSANDTH_FIB_DIGIT = long(THOUSANDTH_FIB_STR)


def create_rand_questions():
    """
    Creates a list of 1 million random questions.

    :return: None
    :rtype: None
    """
    global LIST_CREATED

    if not LIST_CREATED:
        for index in range(1000000):
            rand_str = ''
            for char in str(index):
                rand_str += char + random.choice(string.letters)

            question = 'What #' + rand_str
            answer = 'Answer to question #' + rand_str

            RAND_QUESTIONS[question] = QA(question, answer)

        LIST_CREATED = True

class BaseTest(TestCase):
    def setUp(self):
        self.test_pytona = Interface()
        self.fname = ".\\source\\pyTona\\pytona_text_file.txt"

    def tearDown(self):
        if answer.seq_finder:
            answer.seq_finder.stop()
            answer.seq_finder = None

        if os.path.exists(self.fname):
            os.remove(self.fname)


class TestPytona(BaseTest):
    @requirements(['#0001'])
    def test_question_as_string(self):
        question_str = 'How is feet in miles' + QUESTION_MARK
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
        question_str = 'Who are you' + QUESTION_MARK
        self.test_pytona.ask(question=question_str)
        self.assertEqual(expected_result, self.test_pytona.last_question)

    @requirements(['#0006'])
    def test_answer_question_90_percent(self):
        question_str = 'Who invented Pyt' + QUESTION_MARK
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
        question_str = 'What is 322 feet in miles' + QUESTION_MARK
        self.test_pytona.ask(question=question_str)
        self.assertEqual(expected_result, self.test_pytona.last_question)

    @requirements(['#0007'])
    def test_exclude_number_ending(self):
        expected_result = 'Who invented Python'
        question_str = 'Who invented Python 3' + QUESTION_MARK
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
        question_str = 'Who invented Python' + QUESTION_MARK
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
        question_str = 'Where am I' + QUESTION_MARK
        result = self.test_pytona.ask(question=question_str)
        self.assertEqual(result, 'Lab4')

    @requirements(['#0022'])
    @mock.patch('subprocess.Popen')
    def test_answer_to_where_am_question_unknown_no_exception(self, mock_popen):
        process_mock = mock.Mock()
        attrs = {'communicate.return_value': [None]}
        process_mock.configure_mock(**attrs)
        mock_popen.return_value = process_mock
        question_str = 'Where am I' + QUESTION_MARK
        result = self.test_pytona.ask(question=question_str)
        self.assertEqual(result, 'Unknown')

    @requirements(['#0022'])
    @mock.patch('subprocess.Popen')
    def test_answer_to_where_am_question_unknown_exception(self, mock_popen):
        process_mock = mock.Mock()
        attrs = {'communicate.side_effect': Exception}
        process_mock.configure_mock(**attrs)
        mock_popen.return_value = process_mock
        question_str = 'Where am I' + QUESTION_MARK
        result = self.test_pytona.ask(question=question_str)
        self.assertEqual(result, 'Unknown')

    @requirements(['#0023'])
    @mock.patch('subprocess.Popen')
    def test_answer_to_where_you_question(self, mock_popen):
        process_mock = mock.Mock()
        attrs = {'communicate.return_value': ['https://github.com/krains27/cst236-KyleRains']}
        process_mock.configure_mock(**attrs)
        mock_popen.return_value = process_mock
        question_str = 'Where are you' + QUESTION_MARK
        result = self.test_pytona.ask(question=question_str)
        self.assertEqual(result, 'https://github.com/krains27/cst236-KyleRains')

    @requirements(['#0023'])
    @mock.patch('subprocess.Popen')
    def test_answer_to_where_you_question_exception(self, mock_popen):
        process_mock = mock.Mock()
        attrs = {'communicate.side_effect': Exception}
        process_mock.configure_mock(**attrs)
        mock_popen.return_value = process_mock
        question_str = 'Where are you' + QUESTION_MARK
        result = self.test_pytona.ask(question=question_str)
        self.assertEqual(result, 'Unknown')

    @requirements(['#0023'])
    @mock.patch('subprocess.Popen')
    def test_answer_to_where_you_question_no_exception(self, mock_popen):
        process_mock = mock.Mock()
        attrs = {'communicate.return_value': [None]}
        process_mock.configure_mock(**attrs)
        mock_popen.return_value = process_mock
        question_str = 'Where are you' + QUESTION_MARK
        result = self.test_pytona.ask(question=question_str)
        self.assertEqual(result, 'Unknown')

    @requirements(['#0024', '#0026'])
    @mock.patch('socket.socket')
    def test_answer_to_who_else(self, test):
        m = test.return_value
        m.connect.return_value = None
        m.send.return_value = None
        m.recv.return_value = 'Kyle$Brit$Alex$Josh'
        question_str = 'Who else is here' + QUESTION_MARK
        result = self.test_pytona.ask(question=question_str)
        self.assertEqual(['Kyle', 'Brit', 'Alex', 'Josh'], result)

    @requirements(['#0025'])
    @mock.patch('socket.socket')
    def test_answer_to_who_else_connection_call(self, test):
        m = test.return_value
        m.connect.return_value = None
        m.send.return_value = None
        m.recv.return_value = 'A$B$C$D'
        question_str = 'Who else is here' + QUESTION_MARK
        self.test_pytona.ask(question=question_str)
        m.send.assert_called_with('Who?')
        m.connect.assert_called_with(('192.168.64.3', 1337))

    @requirements(['#0027'])
    @mock.patch('socket.socket')
    def test_answer_to_who_else_exception(self, test):
        m = test.return_value
        m.connect.side_effect = Exception
        question_str = 'Who else is here' + QUESTION_MARK
        result = self.test_pytona.ask(question=question_str)
        self.assertEqual(result, 'IT\'S A TRAAAPPPP')

    @requirements(['#0028'])
    def test_fibonacci_answer_0(self):
        question_str = 'What is the 0 digit of the Fibonacci Sequence' + QUESTION_MARK
        result = self.test_pytona.ask(question=question_str)
        self.assertEqual(result, 0)

    @requirements(['#0028'])
    def test_fibonacci_answer_1(self):
        question_str = 'What is the 1 digit of the Fibonacci Sequence' + QUESTION_MARK
        result = self.test_pytona.ask(question=question_str)
        self.assertEqual(result, 1)

    @requirements(['#0029'])
    def test_fibonacci_answer_thinking(self):
        with mock.patch('pyTona.answer_funcs.random.randint') as mock_random:
            mock_random.return_value = 10
            question_str = 'What is the 15 digit of the Fibonacci Sequence' + QUESTION_MARK
            result = self.test_pytona.ask(question=question_str)
            self.assertEqual(result, 'Thinking...')

    @requirements(['#0029'])
    def test_fibonacci_answer_one_second(self):
        with mock.patch('pyTona.answer_funcs.random.randint') as mock_random:
            mock_random.return_value = 2
            question_str = 'What is the 15 digit of the Fibonacci Sequence' + QUESTION_MARK
            result = self.test_pytona.ask(question=question_str)
            self.assertEqual(result, 'One second')

    @requirements(['#0029'])
    def test_fibonacci_answer_cool_jets(self):
        with mock.patch('pyTona.answer_funcs.random.randint') as mock_random:
            mock_random.return_value = 0
            question_str = 'What is the 15 digit of the Fibonacci Sequence' + QUESTION_MARK
            result = self.test_pytona.ask(question=question_str)
            self.assertEqual(result, 'cool your jets')

    @requirements(['#0035'])
    def test_too_may_params(self):
        with self.assertRaises(Exception) as error:
            question_str = 'What is the 15 15 digit of the Fibonacci Sequence' + QUESTION_MARK
            result = self.test_pytona.ask(question=question_str)

    @requirements(['#0030'])
    def test_storage_load_100_thou(self):
        self.test_pytona.question_answers = {}
        create_rand_questions()

        # 100 thousand question/answer pairs
        for i in RAND_QUESTIONS.keys()[:99999]:
            self.test_pytona.question_answers[i] = RAND_QUESTIONS[i]

        random_question_ans = random.randint(0, 99999)

        question = self.test_pytona.question_answers.keys()[random_question_ans]
        answer = self.test_pytona.question_answers[question].value

        result = self.test_pytona.ask(question=question + QUESTION_MARK)
        self.assertEqual(result, answer)

    @requirements(['#0030'])
    def test_storage_load_1_point_500_thou(self):
        self.test_pytona.question_answers = {}
        create_rand_questions()

        # 500 thousand question/answer pairs
        for i in RAND_QUESTIONS.keys()[:499999]:
            self.test_pytona.question_answers[i] = RAND_QUESTIONS[i]

        random_question_ans = random.randint(0, 499999)

        question = self.test_pytona.question_answers.keys()[random_question_ans]
        answer = self.test_pytona.question_answers[question].value

        result = self.test_pytona.ask(question=question + QUESTION_MARK)
        self.assertEqual(result, answer)

    @requirements(['#0030'])
    def test_storage_load_1_million(self):
        self.test_pytona.question_answers = {}
        create_rand_questions()

        # Add 1 million question/answer pairs
        self.test_pytona.question_answers = RAND_QUESTIONS

        random_question_ans = random.randint(0, 999999)

        question = self.test_pytona.question_answers.keys()[random_question_ans]
        answer = self.test_pytona.question_answers[question].value

        result = self.test_pytona.ask(question=question + QUESTION_MARK)

        self.assertEqual(result, answer)

    @requirements(['#0031'])
    def test_store_5_ms_string_answer(self):
        desired_time = 5 * (10**-3)

        question_str = 'Who are you' + QUESTION_MARK
        self.test_pytona.ask(question=question_str)

        start = time.clock()
        self.test_pytona.teach(answer='I am Groot')
        store_time = time.clock() - start

        self.assertLess(store_time, desired_time)

    @requirements(['#0031'])
    def test_store_5_ms_func_answer(self):
        def answer_func():
            return 'I am Groot'

        desired_time = 5 * (10**-3)

        question_str = 'Who are you' + QUESTION_MARK
        self.test_pytona.ask(question=question_str)

        start = time.clock()
        self.test_pytona.teach(answer=answer_func)
        store_time = time.clock() - start

        self.assertLess(store_time, desired_time)

    @requirements(['#0031'])
    def test_store_string_load_test(self):
        create_rand_questions()
        data_storage.add_title(title='Store Load Test')
        data_storage.add_axes_title(key='Store Load Test',
                                    x_axis_title='Number of Question/Answer Pairs',
                                    y_axis_title='Storage Time')

        self.test_pytona.question_answers = {}

        question_str = 'Who are you' + QUESTION_MARK
        self.test_pytona.ask(question=question_str)

        start = time.clock()
        self.test_pytona.teach(answer='I am Groot')
        store_time = time.clock() - start
        data_storage.add_data(key='Store Load Test',
                              data_points=[len(self.test_pytona.question_answers),
                                           store_time])

        self.test_pytona.question_answers = {}

        # Add one million question/answer pairs
        for i in RAND_QUESTIONS.keys()[:1000]:
            self.test_pytona.question_answers[i] = RAND_QUESTIONS[i]

        question_str = 'Who are you' + QUESTION_MARK
        self.test_pytona.ask(question=question_str)

        start = time.clock()
        self.test_pytona.teach(answer='I am Groot')
        store_time = time.clock() - start
        data_storage.add_data(key='Store Load Test',
                              data_points=[len(self.test_pytona.question_answers),
                                           store_time])

        self.test_pytona.question_answers = {}

        # Add one million question/answer pairs
        for i in RAND_QUESTIONS.keys()[:10000]:
            self.test_pytona.question_answers[i] = RAND_QUESTIONS[i]

        question_str = 'Who are you' + QUESTION_MARK
        self.test_pytona.ask(question=question_str)

        start = time.clock()
        self.test_pytona.teach(answer='I am Groot')
        store_time = time.clock() - start
        data_storage.add_data(key='Store Load Test',
                              data_points=[len(self.test_pytona.question_answers),
                                           store_time])

        self.test_pytona.question_answers = {}

        # Add one million question/answer pairs
        for i in RAND_QUESTIONS.keys()[:100000]:
            self.test_pytona.question_answers[i] = RAND_QUESTIONS[i]

        question_str = 'Who are you' + QUESTION_MARK
        self.test_pytona.ask(question=question_str)

        start = time.clock()
        self.test_pytona.teach(answer='I am Groot')
        store_time = time.clock() - start
        data_storage.add_data(key='Store Load Test',
                              data_points=[len(self.test_pytona.question_answers),
                                           store_time])

        self.test_pytona.question_answers = RAND_QUESTIONS

        question_str = 'Who are you' + QUESTION_MARK
        self.test_pytona.ask(question=question_str)

        start = time.clock()
        self.test_pytona.teach(answer='I am Groot')
        store_time = time.clock() - start
        data_storage.add_data(key='Store Load Test',
                              data_points=[len(self.test_pytona.question_answers),
                                           store_time])

    @requirements(['#0032'])
    def test_retrieve_5_ms_string_answer(self):
        desired_time = 5 * (10**-3)

        question_str = 'Who are you' + QUESTION_MARK
        self.test_pytona.ask(question=question_str)

        self.test_pytona.teach(answer='I am Groot')

        start = time.clock()
        self.test_pytona.ask(question=question_str)
        store_time = time.clock() - start

        self.assertLess(store_time, desired_time)

    @requirements(['#0032'])
    def test_retrieve_5_ms_func_answer(self):
        def answer_func():
            return 'I am Groot'

        desired_time = 5 * (10**-3)

        question_str = 'Who are you' + QUESTION_MARK
        self.test_pytona.ask(question=question_str)

        self.test_pytona.teach(answer=answer_func)

        start = time.clock()
        self.test_pytona.ask(question=question_str)
        store_time = time.clock() - start

        self.assertLess(store_time, desired_time)

    @requirements(['#0032'])
    def test_retrieve_string_load_test(self):
        create_rand_questions()
        data_storage.add_title(title='Retrieve Load Test')
        data_storage.add_axes_title(key='Retrieve Load Test',
                                    x_axis_title='Number of Question/Answer Pairs',
                                    y_axis_title='Retrieval Time')

        self.test_pytona.question_answers = {}

        question_str = 'Who are you' + QUESTION_MARK
        self.test_pytona.ask(question=question_str)

        self.test_pytona.teach(answer='I am Groot')

        start = time.clock()
        self.test_pytona.ask(question=question_str)
        store_time = time.clock() - start

        data_storage.add_data(key='Retrieve Load Test',
                              data_points=[len(self.test_pytona.question_answers),
                                           store_time])

        self.test_pytona.question_answers = {}

        # Add one million question/answer pairs
        for i in RAND_QUESTIONS.keys()[:1000]:
            self.test_pytona.question_answers[i] = RAND_QUESTIONS[i]

        question_str = 'Who are you' + QUESTION_MARK
        self.test_pytona.ask(question=question_str)

        self.test_pytona.teach(answer='I am Groot')

        start = time.clock()
        self.test_pytona.ask(question=question_str)
        store_time = time.clock() - start
        data_storage.add_data(key='Retrieve Load Test',
                              data_points=[len(self.test_pytona.question_answers),
                                           store_time])

        self.test_pytona.question_answers = {}

        # Add one million question/answer pairs
        for i in RAND_QUESTIONS.keys()[:10000]:
            self.test_pytona.question_answers[i] = RAND_QUESTIONS[i]

        question_str = 'Who are you' + QUESTION_MARK
        self.test_pytona.ask(question=question_str)

        self.test_pytona.teach(answer='I am Groot')

        start = time.clock()
        self.test_pytona.ask(question=question_str)
        store_time = time.clock() - start
        data_storage.add_data(key='Retrieve Load Test',
                              data_points=[len(self.test_pytona.question_answers),
                                           store_time])

        self.test_pytona.question_answers = {}

        # Add one million question/answer pairs
        for i in RAND_QUESTIONS.keys()[:100000]:
            self.test_pytona.question_answers[i] = RAND_QUESTIONS[i]

        question_str = 'Who are you' + QUESTION_MARK
        self.test_pytona.ask(question=question_str)

        self.test_pytona.teach(answer='I am Groot')

        start = time.clock()
        self.test_pytona.ask(question=question_str)
        store_time = time.clock() - start
        data_storage.add_data(key='Retrieve Load Test',
                              data_points=[len(self.test_pytona.question_answers),
                                           store_time])

        self.test_pytona.question_answers = RAND_QUESTIONS

        question_str = 'Who are you' + QUESTION_MARK
        self.test_pytona.ask(question=question_str)

        self.test_pytona.teach(answer='I am Groot')

        start = time.clock()
        self.test_pytona.ask(question=question_str)
        store_time = time.clock() - start
        data_storage.add_data(key='Retrieve Load Test',
                              data_points=[len(self.test_pytona.question_answers),
                                           store_time])

    @requirements(['#0033'])
    def test_fibonacci_answer_100(self):
        question_str = 'What is the 100 digit of the Fibonacci Sequence' + QUESTION_MARK
        self.test_pytona.ask(question=question_str)

        start = time.clock()

        result = self.test_pytona.ask(question=question_str)

        while time.clock() - start < 60 and result in ["Thinking...", "One second", "cool your jets"]:
            result = self.test_pytona.ask(question=question_str)

        self.assertEqual(result, 354224848179261915075, 'Verify correct result')

    @requirements(['#0033'])
    def test_fibonacci_answer_1000(self):
        question_str = 'What is the 1000 digit of the Fibonacci Sequence' + QUESTION_MARK
        self.test_pytona.ask(question=question_str)

        start = time.clock()

        result = self.test_pytona.ask(question=question_str)

        while time.clock() - start < 60 and result in ["Thinking...", "One second", "cool your jets"]:
            result = self.test_pytona.ask(question=question_str)

        self.assertEqual(result, THOUSANDTH_FIB_DIGIT)

    @requirements(['#0033'])
    def test_fibonacci_answer_1001(self):
        question_str = 'What is the 1001 digit of the Fibonacci Sequence' + QUESTION_MARK
        self.test_pytona.ask(question=question_str)
        time.sleep(120)  # Give adequate time to find digit
        self.assertEqual(answer.seq_finder.num_indexes, 1000, 'Index should only be 1000 max')

    @requirements(['#0034'])
    def test_fibonacci_generate_1000_under_60(self):
        question_str = 'What is the 1000 digit of the Fibonacci Sequence' + QUESTION_MARK

        start = time.clock()

        result = self.test_pytona.ask(question=question_str)

        # Loop until result is found or 60s has elapsed
        while time.clock() - start < 60 and result in ["Thinking...", "One second", "cool your jets"]:
            result = self.test_pytona.ask(question=question_str)

        self.assertLess(time.clock() - start, 60)
        self.assertEqual(result, THOUSANDTH_FIB_DIGIT, 'Verify correct result')

    @requirements(['#0034'])
    def test_fibonacci_generation_time(self):
        data_storage.add_title(title='Fibonacci Digit Generation')
        data_storage.add_axes_title(key='Fibonacci Digit Generation',
                                    x_axis_title='Fibonacci Digit',
                                    y_axis_title='Calculation Time')


        question_str = 'What is the 1 digit of the Fibonacci Sequence' + QUESTION_MARK

        start = time.clock()

        result = self.test_pytona.ask(question=question_str)

        # Loop until result is found or 60s has elapsed
        while time.clock() - start < 60 and result in ["Thinking...", "One second", "cool your jets"]:
            result = self.test_pytona.ask(question=question_str)
        calc_time = time.clock() - start

        self.assertEqual(result, 1, 'Verify correct result')

        data_storage.add_data(key='Fibonacci Digit Generation',
                              data_points=[1, calc_time])

        question_str = 'What is the 10 digit of the Fibonacci Sequence' + QUESTION_MARK

        start = time.clock()

        result = self.test_pytona.ask(question=question_str)

        # Loop until result is found or 60s has elapsed
        while time.clock() - start < 60 and result in ["Thinking...", "One second", "cool your jets"]:
            result = self.test_pytona.ask(question=question_str)
        calc_time = time.clock() - start

        self.assertEqual(result, 55, 'Verify correct result')

        data_storage.add_data(key='Fibonacci Digit Generation',
                              data_points=[10, calc_time])

        question_str = 'What is the 100 digit of the Fibonacci Sequence' + QUESTION_MARK

        start = time.clock()

        result = self.test_pytona.ask(question=question_str)

        # Loop until result is found or 60s has elapsed
        while time.clock() - start < 60 and result in ["Thinking...", "One second", "cool your jets"]:
            result = self.test_pytona.ask(question=question_str)
        calc_time = time.clock() - start

        self.assertEqual(result, 354224848179261915075, 'Verify correct result')

        data_storage.add_data(key='Fibonacci Digit Generation',
                              data_points=[100, calc_time])

        question_str = 'What is the 1000 digit of the Fibonacci Sequence' + QUESTION_MARK

        start = time.clock()

        result = self.test_pytona.ask(question=question_str)

        # Loop until result is found or 60s has elapsed
        while time.clock() - start < 60 and result in ["Thinking...", "One second", "cool your jets"]:
            result = self.test_pytona.ask(question=question_str)
        calc_time = time.clock() - start

        self.assertEqual(result, THOUSANDTH_FIB_DIGIT, 'Verify correct result')

        data_storage.add_data(key='Fibonacci Digit Generation',
                              data_points=[1000, calc_time])


    @requirements(['#0040'])
    def test_prime_digit_too_high(self):
        question_str = 'What is the last Prime numbers before 10001' + QUESTION_MARK

        result = self.test_pytona.ask(question=question_str)

        self.assertEqual(result, 'Digit too high')

    @requirements(['#0036'])
    def test_prime_digit_100(self):
        question_str = 'What is the last Prime numbers before 100' + QUESTION_MARK

        result = self.test_pytona.ask(question=question_str)

        self.assertEqual(result, 97)

    @requirements(['#0036'])
    def test_prime_digit_10000(self):
        question_str = 'What is the last Prime numbers before 10000' + QUESTION_MARK

        start = time.clock()
        result = self.test_pytona.ask(question=question_str)
        elapsed_time = time.clock() - start

        self.assertEqual(result, 9973)
        self.assertLess(elapsed_time, 5)

    @requirements(['#0036'])
    def test_generate_prime_timing(self):
        data_storage.add_title(title='Prime Number Generation')
        data_storage.add_axes_title(key='Prime Number Generation',
                                    x_axis_title='Prime Number Ceiling',
                                    y_axis_title='Calculation Time')

        question_str = 'What is the last Prime numbers before 10' + QUESTION_MARK

        start = time.clock()
        self.test_pytona.ask(question=question_str)
        store_time = time.clock() - start

        data_storage.add_data(key='Prime Number Generation',
                              data_points=[10, store_time])

        question_str = 'What is the last Prime numbers before 100' + QUESTION_MARK

        start = time.clock()
        self.test_pytona.ask(question=question_str)
        store_time = time.clock() - start

        data_storage.add_data(key='Prime Number Generation',
                              data_points=[100, store_time])

        question_str = 'What is the last Prime numbers before 500' + QUESTION_MARK

        start = time.clock()
        self.test_pytona.ask(question=question_str)
        store_time = time.clock() - start

        data_storage.add_data(key='Prime Number Generation',
                              data_points=[500, store_time])

        question_str = 'What is the last Prime numbers before 1000' + QUESTION_MARK

        start = time.clock()
        self.test_pytona.ask(question=question_str)
        store_time = time.clock() - start

        data_storage.add_data(key='Prime Number Generation',
                              data_points=[1000, store_time])

        question_str = 'What is the last Prime numbers before 5000' + QUESTION_MARK

        start = time.clock()
        self.test_pytona.ask(question=question_str)
        store_time = time.clock() - start

        data_storage.add_data(key='Prime Number Generation',
                              data_points=[5000, store_time])

        question_str = 'What is the last Prime numbers before 7500' + QUESTION_MARK

        start = time.clock()
        self.test_pytona.ask(question=question_str)
        store_time = time.clock() - start

        data_storage.add_data(key='Prime Number Generation',
                              data_points=[7500, store_time])

        question_str = 'What is the last Prime numbers before 10000' + QUESTION_MARK

        start = time.clock()
        self.test_pytona.ask(question=question_str)
        store_time = time.clock() - start

        data_storage.add_data(key='Prime Number Generation',
                              data_points=[10000, store_time])

    @requirements(['#0037'])
    def test_number_list(self):
        test_list = []

        for i in range(100):
            test_list.append(i)

        question_str = 'Where is the list of numbers I asked for' + QUESTION_MARK

        result = self.test_pytona.ask(question=question_str)


        self.assertEqual(result, test_list)

    @requirements(['#0037'])
    def test_number_list_performance(self):
        desired_time = 500 * (10 ** -3)
        test_list = []

        for i in range(100):
            test_list.append(i)

        start = time.clock()
        question_str = 'Where is the list of numbers I asked for' + QUESTION_MARK
        elapsed_time = time.clock() - start

        result = self.test_pytona.ask(question=question_str)

        self.assertEqual(result, test_list)
        self.assertLess(elapsed_time, desired_time)

    @requirements(['#0041'])
    def test_square_root_too_high(self):
        question_str = 'What is the square root of 1000001' + QUESTION_MARK

        result = self.test_pytona.ask(question=question_str)

        self.assertEqual(result, 'Digit too high')

    @requirements(['#0041'])
    def test_square_root_max(self):
        question_str = 'What is the square root of 1000000' + QUESTION_MARK

        result = self.test_pytona.ask(question=question_str)

        self.assertEqual(result, 1000)

    @requirements(['#0041'])
    def test_square_root_float_result(self):
        question_str = 'What is the square root of 10' + QUESTION_MARK

        result = self.test_pytona.ask(question=question_str)

        self.assertAlmostEqual(result, 3.1622, 3)

    @requirements(['#0041'])
    def test_square_root_max(self):
        desired_time = 3 * (10 ** -3)
        question_str = 'What is the square root of 1000000' + QUESTION_MARK

        start = time.clock()
        result = self.test_pytona.ask(question=question_str)
        elapsed_time = time.clock() - start

        self.assertEqual(result, 1000)
        self.assertLess(elapsed_time, desired_time)

    @requirements(['#0041'])
    def test_square_root_timing(self):
        data_storage.add_title(title='Square Root Calculation')
        data_storage.add_axes_title(key='Square Root Calculation',
                                    x_axis_title='Number to Calculate',
                                    y_axis_title='Calculation Time')

        question_str = 'What is the square root of 1' + QUESTION_MARK

        start = time.clock()
        result = self.test_pytona.ask(question=question_str)
        calc_time = time.clock() - start

        self.assertEqual(result, 1)

        data_storage.add_data(key='Square Root Calculation',
                              data_points=[1, calc_time])

        question_str = 'What is the square root of 10' + QUESTION_MARK

        start = time.clock()
        result = self.test_pytona.ask(question=question_str)
        calc_time = time.clock() - start

        self.assertAlmostEqual(result, 3.1622, 3)

        data_storage.add_data(key='Square Root Calculation',
                              data_points=[10, calc_time])

        question_str = 'What is the square root of 100' + QUESTION_MARK

        start = time.clock()
        result = self.test_pytona.ask(question=question_str)
        calc_time = time.clock() - start

        self.assertEqual(result, 10)

        data_storage.add_data(key='Square Root Calculation',
                              data_points=[100, calc_time])

        question_str = 'What is the square root of 1000' + QUESTION_MARK

        start = time.clock()
        result = self.test_pytona.ask(question=question_str)
        calc_time = time.clock() - start

        self.assertAlmostEqual(result, 31.622, 2)

        data_storage.add_data(key='Square Root Calculation',
                              data_points=[1000, calc_time])

        question_str = 'What is the square root of 10000' + QUESTION_MARK

        start = time.clock()
        result = self.test_pytona.ask(question=question_str)
        calc_time = time.clock() - start

        self.assertEqual(result, 100)

        data_storage.add_data(key='Square Root Calculation',
                              data_points=[10000, calc_time])

        question_str = 'What is the square root of 100000' + QUESTION_MARK

        start = time.clock()
        result = self.test_pytona.ask(question=question_str)
        calc_time = time.clock() - start

        self.assertAlmostEqual(result, 316.2277, 3)

        data_storage.add_data(key='Square Root Calculation',
                              data_points=[100000, calc_time])

        question_str = 'What is the square root of 1000000' + QUESTION_MARK

        start = time.clock()
        result = self.test_pytona.ask(question=question_str)
        calc_time = time.clock() - start

        self.assertEqual(result, 1000)

        data_storage.add_data(key='Square Root Calculation',
                              data_points=[1000000, calc_time])

    @requirements(['#0042'])
    def test_file_read_no_file(self):
        question_str = 'Why don\'t you go read a file' + QUESTION_MARK

        result = self.test_pytona.ask(question=question_str)

        self.assertEqual(result, 'File doesn\'t exist')

    @requirements(['#0042'])
    def test_file_read_10000_bytes(self):
        desired_time = 2 * (10 ** -3)
        # Create the file, and write 1000 bytes to it.
        with open(self.fname, 'w') as fhnd:
            for bytes in range(9999):
                fhnd.write(random.choice(string.letters))

            fhnd.write('\n')

        question_str = 'Why don\'t you go read a file' + QUESTION_MARK

        start = time.clock()
        result = self.test_pytona.ask(question=question_str)
        elapsed_time = time.clock() - start

        print elapsed_time

        self.assertEqual(result, 10000)
        self.assertLess(elapsed_time, desired_time)

    @requirements(['#0042'])
    def test_file_read_10000_bytes_linux_config_test(self):
        desired_time = 2 * (10 ** -3)
        # Create the file, and write 1000 bytes to it. Open in binary mode, so \n doesn't
        # convert to windows newline
        with open(self.fname, 'wb') as fhnd:
            for bytes in range(9999):
                fhnd.write(random.choice(string.letters))

            fhnd.write('\n')

        question_str = 'Why don\'t you go read a file' + QUESTION_MARK

        start = time.clock()
        result = self.test_pytona.ask(question=question_str)
        elapsed_time = time.clock() - start

        print elapsed_time

        self.assertEqual(result, 10000)
        self.assertLess(elapsed_time, desired_time)

    @requirements(['#0031'])
    def test_store_response_isolation_test(self):
        desired_speed = 5 * (10 ** -3)
        create_rand_questions()
        self.test_pytona.question_answers = RAND_QUESTIONS

        question_str = 'Who are you'
        answer_str = 'I am groot'

        start = time.clock()
        self.test_pytona.question_answers[question_str] = QA(question_str, answer_str)
        store_time = time.clock() - start

        self.assertLess(store_time, desired_speed)

    @requirements(['#0031'])
    def test_retrieve_response_isolation_test(self):
        desired_speed = 5 * (10 ** -3)
        create_rand_questions()
        self.test_pytona.question_answers = RAND_QUESTIONS

        question_str = 'Who are you'
        answer_str = 'I am groot'

        self.test_pytona.question_answers[question_str] = QA(question_str, answer_str)

        start = time.clock()
        result = self.test_pytona.question_answers[question_str]
        store_time = time.clock() - start

        self.assertLess(store_time, desired_speed)

    def test_system_endurance(self):
        # Create the file, and write 1000 bytes to it.
        with open(self.fname, 'w') as fhnd:
            for bytes in range(9999):
                fhnd.write(random.choice(string.letters))

            fhnd.write('\n')

        test_list = []

        for i in range(100):
            test_list.append(i)

        for _ in range(10000):
            question_str = 'What is the last Prime numbers before 1000' + QUESTION_MARK

            result = self.test_pytona.ask(question=question_str)

            self.assertEqual(result, 997)

            question_str = 'Where is the list of numbers I asked for' + QUESTION_MARK

            result = self.test_pytona.ask(question=question_str)

            self.assertEqual(result, test_list)

            question_str = 'What is the square root of 1000000' + QUESTION_MARK

            result = self.test_pytona.ask(question=question_str)

            self.assertEqual(result, 1000)

            question_str = 'Why don\'t you go read a file' + QUESTION_MARK

            result = self.test_pytona.ask(question=question_str)

            self.assertEqual(result, 10000)

    def test_system_spike(self):
        create_rand_questions()
        original_questions = self.test_pytona.question_answers  # Save off original questions
        added_questions = RAND_QUESTIONS

        for question in original_questions.keys():
            added_questions[question] = original_questions[question]

        # Create the file, and write 1000 bytes to it.
        with open(self.fname, 'w') as fhnd:
            for bytes in range(9999):
                fhnd.write(random.choice(string.letters))

            fhnd.write('\n')

        test_list = []

        for i in range(100):
            test_list.append(i)

        # Ask questions with original set
        for _ in range(100):
            question_str = 'What is the last Prime numbers before 1000' + QUESTION_MARK

            result = self.test_pytona.ask(question=question_str)

            self.assertEqual(result, 997)

            question_str = 'Where is the list of numbers I asked for' + QUESTION_MARK

            result = self.test_pytona.ask(question=question_str)

            self.assertEqual(result, test_list)

            question_str = 'What is the square root of 1000000' + QUESTION_MARK

            result = self.test_pytona.ask(question=question_str)

            self.assertEqual(result, 1000)

            question_str = 'Why don\'t you go read a file' + QUESTION_MARK

            result = self.test_pytona.ask(question=question_str)

            self.assertEqual(result, 10000)

        self.test_pytona.question_answers = added_questions

        # Ask questions with original set + 1 million questions
        for _ in range(100):
            question_str = 'What is the last Prime numbers before 1000' + QUESTION_MARK

            result = self.test_pytona.ask(question=question_str)

            self.assertEqual(result, 997)

            question_str = 'Where is the list of numbers I asked for' + QUESTION_MARK

            result = self.test_pytona.ask(question=question_str)

            self.assertEqual(result, test_list)

            question_str = 'What is the square root of 1000000' + QUESTION_MARK

            result = self.test_pytona.ask(question=question_str)

            self.assertEqual(result, 1000)

            question_str = 'Why don\'t you go read a file' + QUESTION_MARK

            result = self.test_pytona.ask(question=question_str)

            self.assertEqual(result, 10000)

        self.test_pytona.question_answers = original_questions

        # Ask questions with original set
        for _ in range(100):
            question_str = 'What is the last Prime numbers before 1000' + QUESTION_MARK

            result = self.test_pytona.ask(question=question_str)

            self.assertEqual(result, 997)

            question_str = 'Where is the list of numbers I asked for' + QUESTION_MARK

            result = self.test_pytona.ask(question=question_str)

            self.assertEqual(result, test_list)

            question_str = 'What is the square root of 1000000' + QUESTION_MARK

            result = self.test_pytona.ask(question=question_str)

            self.assertEqual(result, 1000)

            question_str = 'Why don\'t you go read a file' + QUESTION_MARK

            result = self.test_pytona.ask(question=question_str)

            self.assertEqual(result, 10000)