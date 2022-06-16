import unittest

class TestStringMethods(unittest.TestCase):
    '''this code is to do anything'''

    def test_upper(self):
        '''this code is to do anything'''
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        '''this code is to do anything'''
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        '''this code is to do anything'''
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
