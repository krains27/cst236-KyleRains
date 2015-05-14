"""
Test for SharpTona
"""
from pywinauto import application
from unittest import TestCase


class BaseTest(TestCase):

    def setUp(self):
        self.sharpTona_app = application.Application()
        self.sharpTona_app.start('sharpTona.exe')
        self.app_wndw = self.sharpTona_app['SharpTona']

    def tearDown(self):
        self.sharpTona_app.kill_()


class TestSharpTona(BaseTest):
    def test_window_title(self):
        self.assertEqual(self.app_wndw.Texts()[0], 'SharpTona')

    def test_label_question(self):
        self.assertEqual(self.app_wndw['Question:'].Texts()[0], 'Question:')

    def test_label_answer(self):
        self.assertEqual(self.app_wndw['Answer:'].Texts()[0][:-1], 'Answer:')

    def test_enter_question_recieve_answer(self):
        self.app_wndw['Question:Edit'].TypeKeys("How are you?", with_spaces=True)
        self.app_wndw['Ask'].Click()
        self.assertEqual(self.app_wndw['Answer:Edit'].Texts()[0],
                         'I don\'t know please teach me.')

    def test_default_question_answer(self):
        self.app_wndw['Question:Edit'].TypeKeys("What is the answer to everything?",
                                                                  with_spaces=True)
        self.app_wndw['Ask'].Click()
        self.assertEqual(self.app_wndw['Answer:Edit'].Texts()[0], '42')

    def test_default_disabled_teach_button(self):
        self.assertFalse(self.app_wndw['Teach'].IsEnabled())

    def test_default_disabled_correct_button(self):
        self.assertFalse(self.app_wndw['Correct'].IsEnabled())

    def test_default_disabled_answer_box(self):
        self.assertFalse(self.app_wndw['Answer:Edit'].IsEnabled())

    def test_display_answer(self):
        self.app_wndw['Question:Edit'].TypeKeys("What is the answer to everything?",
                                                                  with_spaces=True)
        self.app_wndw['Ask'].Click()
        self.assertEqual(self.app_wndw['Answer:Edit'].Texts()[0], '42')

    def test_no_question(self):
        self.app_wndw['Ask'].Click()
        self.assertEqual(self.app_wndw['Answer:Edit'].Texts()[0], 'Was that a question?')

    def test_known_question(self):
        self.app_wndw['Question:Edit'].TypeKeys("What is the answer to everything?",
                                                                  with_spaces=True)
        self.app_wndw['Ask'].Click()
        self.assertEqual(self.app_wndw['Answer:Edit'].Texts()[0], '42')
        self.assertTrue(self.app_wndw['Answer'].IsEnabled())

    def test_correct_button(self):
        self.app_wndw['Question:Edit'].TypeKeys("What is the answer to everything?",
                                                                  with_spaces=True)
        self.app_wndw['Ask'].Click()
        self.assertEqual(self.app_wndw['Answer:Edit'].Texts()[0], '42')
        self.app_wndw['Answer:Edit'].TypeKeys("Nobody knows the answer to everything.",
                                                                  with_spaces=True)
        self.app_wndw['Correct'].Click()
        self.assertFalse(self.app_wndw['Answer:Edit'].IsEnabled())
        self.assertFalse(self.app_wndw['Teach'].IsEnabled())
        self.assertFalse(self.app_wndw['Correct'].IsEnabled())
        self.app_wndw['Ask'].Click()
        self.assertEqual(self.app_wndw['Answer:Edit'].Texts()[0],
                         'Nobody knows the answer to everything.')
        self.assertFalse(self.app_wndw['Teach'].IsEnabled())
        self.assertTrue(self.app_wndw['Correct'].IsEnabled())

    def test_teach_button_enable(self):
        self.app_wndw['Question:Edit'].TypeKeys("Who are you?", with_spaces=True)
        self.app_wndw['Ask'].Click()
        self.assertEqual(self.app_wndw['Answer:Edit'].Texts()[0],
                         'I don\'t know please teach me.')
        self.assertTrue(self.app_wndw['Teach'].IsEnabled())

    def test_teach_button_with_answer(self):
        self.app_wndw['Question:Edit'].TypeKeys("Who are you?", with_spaces=True)
        self.app_wndw['Ask'].Click()
        self.assertEqual(self.app_wndw['Answer:Edit'].Texts()[0],
                         'I don\'t know please teach me.')
        self.assertTrue(self.app_wndw['Teach'].IsEnabled())
        self.app_wndw['Answer:Edit'].TypeKeys("I am Groot", with_spaces=True)
        self.app_wndw['Teach'].Click()
        self.assertFalse(self.app_wndw['Answer:Edit'].IsEnabled())
        self.assertFalse(self.app_wndw['Teach'].IsEnabled())
        self.assertFalse(self.app_wndw['Correct'].IsEnabled())
        self.app_wndw['Ask'].Click()
        self.assertEqual(self.app_wndw['Answer:Edit'].Texts()[0], 'I am Groot')
        self.assertFalse(self.app_wndw['Teach'].IsEnabled())
        self.assertTrue(self.app_wndw['Correct'].IsEnabled())