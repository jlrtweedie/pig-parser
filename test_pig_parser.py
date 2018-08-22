import pig_parser as pig
import numpy as np
import unittest


class PigParserTestCase(unittest.TestCase):
    """Unit tests for each main function in pig_parser.py"""

    def test_load(self):
        # Test: abc.csv is loaded into local variable storage as ndarray
        pig._load('d', 'abc.csv')
        self.assertIsInstance(pig.VARIABLES['d'], np.ndarray)

    def test_filter(self):
        # Test: masked array is submatrix of input array
        pig._filter('d', 'e', 0, 2, '>')
        self.assertIn(pig.VARIABLES['e'][0], pig.VARIABLES['d'])
        self.assertIn(pig.VARIABLES['e'][1], pig.VARIABLES['d'])

    def test_generate(self):
        # Test: elements in generated array double checked vs input array
        pig._generate('d', 'f', [[0, '+', 1], [1, '*', 2]])
        self.assertEqual(pig.VARIABLES['f'][:,0].all(),
                         (pig.VARIABLES['d'][:,0]+1).all())
        self.assertEqual(pig.VARIABLES['f'][:,1].all(),
                         (pig.VARIABLES['d'][:,1]*2).all())

    def test_parse(self):
        # Test: run parse function on pig_script.txt and check sample
        # test conditions for test_load, test_filter, and test_generate
        with open('pig_script.txt') as script:
            for line in script:
                pig.pig_parser(line)

        self.assertIsInstance(pig.VARIABLES['a'], np.ndarray)
        self.assertIsInstance(pig.VARIABLES['b'], np.ndarray)
        self.assertIsInstance(pig.VARIABLES['c'], np.ndarray)
        self.assertEqual(pig.VARIABLES['b'][:,0].all(),
                         pig.VARIABLES['a'][:,0].all())
        self.assertEqual(pig.VARIABLES['b'][:,1].all(),
                         (pig.VARIABLES['a'][:,0]*2).all())
        self.assertEqual(pig.VARIABLES['b'][:,2].all(),
                         pig.VARIABLES['a'][1].all())
        self.assertIn(pig.VARIABLES['c'], pig.VARIABLES['b'])

def suite():
    suite = unittest.TestSuite()
    suite.addTest(PigParserTestCase('test_parse'))
    suite.addTest(PigParserTestCase('test_load'))
    suite.addTest(PigParserTestCase('test_generate'))
    suite.addTest(PigParserTestCase('test_filter'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner(failfast=True)
    runner.run(suite())
