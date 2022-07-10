import unittest
from linear_algebra.linear_algebra import LinearAlgebra

V = [1.0, 2.5, 5, 7.5]
W = [1, 3, 5, 7]
X = [0, 1.2, 3.4, 5.6, 7.8]

class Test_Polygon(unittest.TestCase):

    def setUp(self):
        self.vector = LinearAlgebra()

    def test_validate_vectors_same_length(self):
        """Test _validate_vectors_same_length_ method."""
        self.assertTrue(self.vector._validate_vectors_same_length_([V, W]))
        self.assertTrue(self.vector._validate_vectors_same_length_([V]))
        with self.assertRaises(ValueError):
            self.vector._validate_vectors_same_length_([V, X])
            # self.vector._validate_vectors_(['2'])
            # self.vector._validate_vectors_(1.234)
            # self.vector._validate_vectors_(1)
            # self.vector._validate_vectors_([])
            # self.vector._validate_vectors_(None)

    def test_validate_vectors_(self):
        """Test _validate_vectors_ method."""
        self.assertTrue(self.vector._validate_vectors_([V, X]))
        with self.assertRaises(ValueError):
            self.vector._validate_vectors_([V, 'a'])
            self.vector._validate_vectors_(['2'])
            self.vector._validate_vectors_(1.234)
            self.vector._validate_vectors_(1)
            self.vector._validate_vectors_([])
            self.vector._validate_vectors_(None)

    def test_validate_vector_(self):
        """Test _validate_vector_ method."""
        self.assertTrue(self.vector._validate_vector_(V))
        with self.assertRaises(ValueError):
            self.vector._validate_vector_('a')
            self.vector._validate_vector_(['2'])
            self.vector._validate_vector_(1.234)
            self.vector._validate_vector_(1)
            self.vector._validate_vector_([])
            self.vector._validate_vector_(None)
