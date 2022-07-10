import unittest
from linear_algebra.linear_algebra import LinearAlgebra

V = [1.0, 2.5, 5, 7.5]
W = [1, 3, 5, 7]
X = [0, 1.2, 3.4, 5.6, 7.8]
C = 2

class Test_Polygon(unittest.TestCase):

    def setUp(self):
        self.linalg = LinearAlgebra()

    def test_distance(self):
        """Test distance method."""
        self.assertTrue(self.linalg.distance(v=V, w=W), 0)
        with self.assertRaises(AssertionError):
            self.linalg.distance(v=V, w=X)

    def test_squared_distance(self):
        """Test squared_distance method."""
        self.assertTrue(self.linalg.squared_distance(v=V, w=W), 0)
        with self.assertRaises(AssertionError):
            self.linalg.squared_distance(v=V, w=X)

    def test_vector_magnitude(self):
        """Test vector_magnitude method."""
        self.assertTrue(round(self.linalg.vector_magnitude(v=V), 6), 9.407444)
        with self.assertRaises(ValueError):
            self.linalg.vector_magnitude(v=C)

    def test_sum_of_squares(self):
        """Test sum_of_squares method."""
        self.assertTrue(self.linalg.sum_of_squares(v=V), 88.5)
        with self.assertRaises(ValueError):
            self.linalg.sum_of_squares(v=C)

    def test_dot_product(self):
        """Test dot_product method."""
        self.assertTrue(self.linalg.dot_product(v=V, w=W), 86)
        with self.assertRaises(AssertionError):
            self.linalg.dot_product(v=V, w=X)

    def test_vector_mean(self):
        """Test vector_mean method."""
        self.assertListEqual(self.linalg.vector_mean(vector_list=[V, W]), [1.0, 2.75, 5, 7.25])
        with self.assertRaises(AssertionError):
            self.linalg.vector_sum(vector_list=[V, X])

    def test_scalar_multiply(self):
        """Test scalar_multiply method."""
        self.assertListEqual(self.linalg.scalar_multiply(c=2, v=V), [2.0, 5.0, 10, 15.])
        with self.assertRaises(ValueError):
            self.linalg.scalar_multiply(c='2', v=V)

    def test_vector_sum(self):
        """Test vector_sum method."""
        self.assertListEqual(self.linalg.vector_sum(vector_list=[V, W]), [2.0, 5.5, 10, 14.5])
        with self.assertRaises(AssertionError):
            self.linalg.vector_sum(vector_list=[V, X])

    def test_vector_add(self):
        """Test vector_add method."""
        self.assertListEqual(self.linalg.vector_add(v=V, w=W), [2.0, 5.5, 10, 14.5])
        with self.assertRaises(AssertionError):
            self.linalg.vector_add(v=V, w=X)

    def test_vector_subtract(self):
        """Test vector_subtract method."""
        self.assertListEqual(self.linalg.vector_subtract(v=V, w=W), [0, -0.5, 0, 0.5])
        with self.assertRaises(AssertionError):
            self.linalg.vector_subtract(v=V, w=X)
        
    def test_validate_vectors_same_length(self):
        """Test _validate_vectors_same_length_ method."""
        self.assertTrue(self.linalg._validate_vectors_same_length_([V, W]))
        self.assertTrue(self.linalg._validate_vectors_same_length_([V]))
        with self.assertRaises(AssertionError):
            self.linalg._validate_vectors_same_length_([V, X])

    def test_validate_vectors_(self):
        """Test _validate_vectors_ method."""
        self.assertTrue(self.linalg._validate_vectors_([V, X]))
        with self.assertRaises(ValueError):
            self.linalg._validate_vectors_([V, 'a'])

    def test_validate_vector_(self):
        """Test _validate_vector_ method."""
        self.assertTrue(self.linalg._validate_vector_(V))
        with self.assertRaises(ValueError):
            self.linalg._validate_vector_('a')
            self.linalg._validate_vector_(['2'])
            self.linalg._validate_vector_(1.234)
            self.linalg._validate_vector_(1)
            self.linalg._validate_vector_([])
            self.linalg._validate_vector_(None)

    def test_validate_scalar_(self):
        """Test _validate_scalar_ method."""
        self.assertTrue(self.linalg._validate_scalar_(C))
        with self.assertRaises(ValueError):
            self.linalg._validate_vector_('a')
            self.linalg._validate_vector_(['2'])
            self.linalg._validate_vector_([])
            self.linalg._validate_vector_(None)