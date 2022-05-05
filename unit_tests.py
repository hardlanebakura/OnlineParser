import unittest

class TestModule(unittest.TestCase):

    def TestIntInputs(self):
        '''function should fail on non float inputs'''
        #self.assertRaisesRegexp(TypeError, 'Expected float input', get_users("a"))

    def testExample1(self):
        '''testing on the input data for example 1'''
        #self.assertEqual(get_users(1.0), 10.95)

if (__name__ == "__main__"):
    unittest.main()