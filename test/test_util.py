import unittest
from util import validate_scalar, validate_vector,  validate_matrix

V = [1.0, 2.5, 5, 7.5]
W = [1, 3, 5, 7]
X = [0, 1.2, 3.4, 5.6, 7.8]
M = [V, W]
N = [V, X]
C = 2

class Test_Util(unittest.TestCase):

    def setUp(self):
        self.util = None
            
    def test_validate_vector_(self):
        """Test _validate_vector_ method."""
        self.assertTrue(validate_vector(V))
        with self.assertRaises(ValueError):
            validate_vector('a')
        with self.assertRaises(ValueError):
            validate_vector(['2'])
        with self.assertRaises(ValueError):
            validate_vector(1.234)
        with self.assertRaises(ValueError):
            validate_vector(1)
        with self.assertRaises(ValueError):
            validate_vector([])
        with self.assertRaises(ValueError):
            validate_vector(None)
    
    def test_validate_scalar_(self):
        """Test _validate_scalar_ method."""
        self.assertTrue(validate_scalar(C))
        with self.assertRaises(ValueError):
            validate_scalar('a')
        with self.assertRaises(ValueError):
            validate_scalar(['2'])
        with self.assertRaises(ValueError):
            validate_scalar([])
        with self.assertRaises(ValueError):
            validate_scalar(None)

    def test_validate_matrix(self):
        """Test _validate_matrix_ method."""
        self.assertTrue(validate_matrix(M))
        self.assertTrue(validate_matrix([V]))
        with self.assertRaises(ValueError):
            validate_matrix(C)
        with self.assertRaises(AssertionError):
            validate_matrix(N)
        with self.assertRaises(ValueError):
            validate_matrix([])

