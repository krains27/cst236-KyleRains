"""
Test for source.pyTona.main
"""
import difflib
import getpass
from datetime import datetime
from source.pyTona import main
from unittest import TestCase
from ReqTracer import requirements

QUESTION_MARK = chr(0x3E)

class BaseTest(TestCase):
    def setUp(self):
        self.test_pytona = main.Interface()

class TestPytona(BaseTest):
    @requirements(['#0001'])
    def test_question_as_string(self):
        question_str = 'How is feet in miles' + QUESTION_MARK
        result = self.test_pytona.ask(question=question_str)
        self.assertNotEqual(result, main.NOT_A_QUESTION_RETURN)

    @requirements(['#0001'])
    def test_question_as_string_int(self):
        question_int = 10
        with self.assertRaises(Exception):
            self.test_pytona.ask(question=question_int)

    @requirements(['#0002'])
    def test_answer_question_how(self):
        question_str = 'How are you' + QUESTION_MARK
        result = self.test_pytona.ask(question=question_str)
        self.assertNotEqual(result, main.NOT_A_QUESTION_RETURN)

    @requirements(['#0002'])
    def test_answer_question_what(self):
        question_str = 'What are you' + QUESTION_MARK
        result = self.test_pytona.ask(question=question_str)
        self.assertNotEqual(result, main.NOT_A_QUESTION_RETURN)

    @requirements(['#0002'])
    def test_answer_question_where(self):
        question_str = 'Where are you' + QUESTION_MARK
        result = self.test_pytona.ask(question=question_str)
        self.assertNotEqual(result, main.NOT_A_QUESTION_RETURN)

    @requirements(['#0002'])
    def test_answer_question_why(self):
        question_str = 'Why are you doing this' + QUESTION_MARK
        result = self.test_pytona.ask(question=question_str)
        self.assertNotEqual(result, main.NOT_A_QUESTION_RETURN)

    @requirements(['#0002'])
    def test_answer_question_who(self):
        question_str = 'Who are you' + QUESTION_MARK
        result = self.test_pytona.ask(question=question_str)
        self.assertNotEqual(result, main.NOT_A_QUESTION_RETURN)

    @requirements(['#0003'])
    def test_invalid_keyword(self):
        question_str = 'Are you going fishing' + QUESTION_MARK
        result = self.test_pytona.ask(question=question_str)
        self.assertEqual(result, main.NOT_A_QUESTION_RETURN)

    @requirements(['#0004'])
    def test_no_question_mark(self):
        question_str = 'Are you going fishing'
        result = self.test_pytona.ask(question=question_str)
        self.assertEqual(result, main.NOT_A_QUESTION_RETURN)

    @requirements(['#0005'])
    def test_broken_down_question(self):
        expected_result = 'Who are you'
        question_str = 'Who are you' + QUESTION_MARK
        self.test_pytona.ask(question=question_str)
        print self.test_pytona.last_question
        self.assertEqual(expected_result, self.test_pytona.last_question)

    @requirements(['#0006'])
    def test_answer_question_90_percent(self):
        question_str = 'Who invented Pyt' + QUESTION_MARK
        # Make sure that the string is 90 percent or higher
        self.assertGreaterEqual(difflib.SequenceMatcher(a='Who invented Pyt', b='Who invented Python').ratio(), .9)
        result = self.test_pytona.ask(question=question_str)
        self.assertEqual(result, 'Guido Rossum(Benevolent Dictator For Life)')

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

    @requirements(['#0007'])
    def test_exclude_number_hex(self):
        expected_result = 'What is feet in miles'
        question_str = 'What is 0x55 feet in miles' + QUESTION_MARK
        self.test_pytona.ask(question=question_str)
        self.assertEqual(expected_result, self.test_pytona.last_question)

    @requirements(['#0007'])
    def test_exclude_number_oct(self):
        expected_result = 'What is feet in miles'
        question_str = 'What is 0o100 feet in miles' + QUESTION_MARK
        self.test_pytona.ask(question=question_str)
        self.assertEqual(expected_result, self.test_pytona.last_question)

    @requirements(['#0008'])
    def test_valid_match(self):
        question_str = 'Who invented Python' + QUESTION_MARK
        result = self.test_pytona.ask(question=question_str)
        self.assertEqual(result, 'Guido Rossum(Benevolent Dictator For Life)')

    @requirements(['#0009'])
    def test_invalid_match(self):
        question_str = 'Who are you' + QUESTION_MARK
        result = self.test_pytona.ask(question=question_str)
        self.assertEqual(result, main.UNKNOWN_QUESTION)

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
        self.assertEqual(result, main.NO_QUESTION)

    @requirements(['#0013'])
    def test_answer_to_answered_question(self):
        question_str = 'Who invented Python' + QUESTION_MARK
        self.test_pytona.ask(question=question_str)
        result = self.test_pytona.teach(answer='A machine')
        self.assertEqual(result, main.NO_TEACH)

        # Make sure question wasn't changed
        result = self.test_pytona.ask(question=question_str)
        self.assertEqual(result, 'Guido Rossum(Benevolent Dictator For Life)')

    @requirements(['#0014', '#0015'])
    def test_updating_answer_string(self):
        question_str = 'Who invented Python' + QUESTION_MARK
        result = self.test_pytona.ask(question=question_str)
        self.assertEqual(result, 'Guido Rossum(Benevolent Dictator For Life)')

        self.test_pytona.correct(answer='A machine')
        result = self.test_pytona.ask(question=question_str)
        self.assertEqual(result, 'A machine')

    @requirements(['#0015'])
    def test_updating_answer_func(self):
        def answer_func():
            return 'A machine'

        question_str = 'Who invented Python' + QUESTION_MARK
        result = self.test_pytona.ask(question=question_str)
        self.assertEqual(result, 'Guido Rossum(Benevolent Dictator For Life)')

        self.test_pytona.correct(answer=answer_func)
        result = self.test_pytona.ask(question=question_str)
        self.assertEqual(result, 'A machine')

    @requirements(['#0016'])
    def test_updating_answer_no_question(self):
        result = self.test_pytona.correct(answer='A machine')
        self.assertEqual(result, main.NO_QUESTION)

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

    @requirements(['#0018'])
    def test_answer_to_time_question_date_time_format(self):
        date_time = datetime(year=1984, month=12, day=27, hour=11, minute=23, second=00)
        current_time = date_time.now()
        time_diff = current_time - date_time
        question_str = 'How many seconds since 12/27/1984 11:23:00' + QUESTION_MARK
        result = self.test_pytona.ask(question=question_str)
        self.assertEqual(result, '{}'.format(time_diff.seconds))

    @requirements(['#0018'])
    def test_answer_to_time_question_date_time_separated(self):
        date_time = datetime(year=1984, month=12, day=27, hour=11, minute=23, second=00)
        current_time = date_time.now()
        time_diff = current_time - date_time
        question_str = 'How many seconds since 12 27 1984 11 23 00' + QUESTION_MARK
        result = self.test_pytona.ask(question=question_str)
        self.assertEqual(result, '{}'.format(time_diff.seconds))

    @requirements(['#0018'])
    def test_answer_to_time_question_no_date_time(self):
        date_time = datetime(year=1984, month=12, day=27, hour=11, minute=23, second=00)
        current_time = date_time.now()
        time_diff = current_time - date_time
        question_str = 'How many seconds since' + QUESTION_MARK
        result = self.test_pytona.ask(question=question_str)
        self.assertEqual(result, '{}'.format(time_diff.seconds))

    @requirements(['#0019'])
    def test_answer_to_python_question_valid(self):
        question_str = 'Who invented Python' + QUESTION_MARK
        result = self.test_pytona.ask(question=question_str)
        self.assertEqual(result, 'Guido Rossum(Benevolent Dictator For Life)')

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

