from unittest import TestCase
import camelCase

class TestInputString(TestCase):

    def test_camelcase_format_hello_world(self):
        txt = camelCase.camelcase_format('hello world')
        self.assertEqual('helloWorld', txt)


    def test_camelcase_format_string_with_numeric(self):
        txt = camelCase.camelcase_format('hello world 2')
        self.assertEqual('helloWorld2', txt)


    def test_camelcase_format_string_with_sp_chars(self):
        txt = camelCase.camelcase_format('hel!lo wo#$#$¿%^^&*(¿)rld ¿^$%^%#')
        self.assertEqual('helloWorld', txt)


    def test_camelcase_format_empty_string(self):
        with self.assertRaises(ValueError):
            camelCase.camelcase_format('')

        with self.assertRaises(ValueError):
            camelCase.camelcase_format('   ')


    def test_camelcase_format_numeric(self):
        with self.assertRaises(ValueError):
            camelCase.camelcase_format('2')

        with self.assertRaises(ValueError):
            camelCase.camelcase_format('0')

        with self.assertRaises(ValueError):
            camelCase.camelcase_format('12345')


    def test_camelcase_format_special_chars(self):
        with self.assertRaises(ValueError):
            camelCase.camelcase_format('!')

        with self.assertRaises(ValueError):
            camelCase.camelcase_format('!@#')

        with self.assertRaises(ValueError):
            camelCase.camelcase_format('!¿°‣')
