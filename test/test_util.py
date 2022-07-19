import unittest
from util import validate_scalar, validate_vector,  validate_matrix, validate_positive_scalar, validate_probability,\
    validate_positive_integer

V = [1.0, 2.5, 5, 7.5]
W = [1, 3, 5, 7]
X = [0, 1.2, 3.4, 5.6, 7.8]
M = [V, W]
N = [V, X]
C = 2

class Test_Util(unittest.TestCase):

    def setUp(self):
        self.util = None
            
    def test_validate_vector(self):
        """Test _validate_vector method."""
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
    
    def test_validate_scalar(self):
        """Test _validate_scalar method."""
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

    def test_validate_postive_scalar(self):
        """Test _validate_positive_scalar method."""
        self.assertTrue(validate_positive_scalar(C))
        with self.assertRaises(ValueError):
            validate_positive_scalar(-1 * C)
        with self.assertRaises(ValueError):
            validate_positive_scalar('a')
        with self.assertRaises(ValueError):
            validate_positive_scalar(['2'])
        with self.assertRaises(ValueError):
            validate_positive_scalar([])
        with self.assertRaises(ValueError):
            validate_positive_scalar(None)

    def test_validate_postive_integer(self):
        """Test _validate_positive_scalar method."""
        self.assertTrue(validate_positive_integer(C))
        with self.assertRaises(ValueError):
            validate_positive_integer(0.5)
        with self.assertRaises(ValueError):
            validate_positive_integer(-1 * C)
        with self.assertRaises(ValueError):
            validate_positive_integer('a')
        with self.assertRaises(ValueError):
            validate_positive_integer(['2'])
        with self.assertRaises(ValueError):
            validate_positive_integer([])
        with self.assertRaises(ValueError):
            validate_positive_integer(None)

    def test_validate_probability(self):
        """Test _validate_probability method."""
        self.assertTrue(validate_probability(0.0))
        self.assertTrue(validate_probability(0.5))
        self.assertTrue(validate_probability(1.0))
        with self.assertRaises(ValueError):
            self.assertTrue(validate_probability(C))
        with self.assertRaises(ValueError):
            validate_probability(-1 * C)
        with self.assertRaises(ValueError):
            validate_probability('a')
        with self.assertRaises(ValueError):
            validate_probability(['2'])
        with self.assertRaises(ValueError):
            validate_probability([])
        with self.assertRaises(ValueError):
            validate_probability(None)