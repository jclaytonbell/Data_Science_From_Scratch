import unittest
from linear_algebra.linear_algebra import LinearAlgebra

V = [1.0, 2.5, 5, 7.5]
W = [1, 3, 5, 7]
X = [0, 1.2, 3.4, 5.6, 7.8]
M = [V, W]
N = [V, X]
C = 2

class Test_LinAlg(unittest.TestCase):

    def setUp(self):
        self.linalg = LinearAlgebra()

    def test_make_matrix(self):
        """Test make_matrix method."""
        m1 = self.linalg.make_matrix(n_rows=2, n_columns=2, entry_fn=self.linalg.zeroes)
        self.assertTupleEqual(self.linalg.matrix_shape(m=m1), (2, 2))
        self.assertListEqual(m1, [[0, 0], [0, 0]])
        m2 = self.linalg.make_matrix(n_rows=2, n_columns=2, entry_fn=self.linalg.ones)
        self.assertTupleEqual(self.linalg.matrix_shape(m=m2), (2, 2))
        self.assertListEqual(m2, [[1, 1], [1, 1]])
        m3 = self.linalg.make_matrix(n_rows=2, n_columns=2, entry_fn=self.linalg.is_diagonal)
        self.assertTupleEqual(self.linalg.matrix_shape(m=m3), (2, 2))
        self.assertListEqual(m3, [[1, 0], [0, 1]])
        m4 = self.linalg.make_matrix(n_rows=2, n_columns=2, entry_fn=None)
        self.assertTupleEqual(self.linalg.matrix_shape(m=m4), (2, 2))
        self.assertListEqual(m4, [[0, 0], [0, 0]])
        with self.assertRaises(ValueError):
            self.linalg.make_matrix(n_rows=-2, n_columns=-2, entry_fn=None)

    def test_get_row(self):
        """Test get_row method."""
        self.assertListEqual(self.linalg.get_row(m=M, i=0), V)
        with self.assertRaises(ValueError):
            self.assertListEqual(self.linalg.get_row(m=C, i=0), V)

    def test_get_column(self):
        """Test get_column method."""
        self.assertListEqual(self.linalg.get_column(m=M, j=0), [1.0, 1])
        with self.assertRaises(ValueError):
            self.assertListEqual(self.linalg.get_column(m=C, j=0), W)

    def test_matrix_shape(self):
        """Test matrix_shape method."""
        self.assertTupleEqual(self.linalg.matrix_shape(m=M), (2, 4))
        with self.assertRaises(ValueError):
            self.linalg.matrix_shape(m=C)
        with self.assertRaises(ValueError):
            self.linalg.matrix_shape(m=[[]])
        with self.assertRaises(ValueError):
            self.linalg.matrix_shape(m=[])

    def test_distance(self):
        """Test distance method."""
        self.assertEqual(round(self.linalg.distance(v=V, w=W), 6), 0.707107)
        with self.assertRaises(AssertionError):
            self.linalg.distance(v=V, w=X)

    def test_squared_distance(self):
        """Test squared_distance method."""
        self.assertEqual(self.linalg.squared_distance(v=V, w=W), 0.5)
        with self.assertRaises(AssertionError):
            self.linalg.squared_distance(v=V, w=X)

    def test_magnitude(self):
        """Test magnitude method."""
        self.assertEqual(round(self.linalg.magnitude(v=V), 6), 9.407444)
        with self.assertRaises(ValueError):
            self.linalg.magnitude(v=C)

    def test_sum_of_squares(self):
        """Test sum_of_squares method."""
        self.assertEqual(self.linalg.sum_of_squares(v=V), 88.5)
        with self.assertRaises(ValueError):
            self.linalg.sum_of_squares(v=C)

    def test_dot_product(self):
        """Test dot_product method."""
        self.assertEqual(self.linalg.dot_product(v=V, w=W), 86)
        with self.assertRaises(AssertionError):
            self.linalg.dot_product(v=V, w=X)

    def test_mean(self):
        """Test mean method."""
        self.assertListEqual(self.linalg.mean(v_list=[V, W]), [1.0, 2.75, 5, 7.25])
        with self.assertRaises(AssertionError):
            self.linalg.sum(v_list=[V, X])

    def test_scalar_multiply(self):
        """Test scalar_multiply method."""
        self.assertListEqual(self.linalg.scalar_multiply(c=2, v=V), [2.0, 5.0, 10, 15.])
        with self.assertRaises(ValueError):
            self.linalg.scalar_multiply(c='2', v=V)

    def test_sum(self):
        """Test sum method."""
        self.assertListEqual(self.linalg.sum(v_list=[V, W]), [2.0, 5.5, 10, 14.5])
        with self.assertRaises(AssertionError):
            self.linalg.sum(v_list=[V, X])

    def test_add(self):
        """Test add method."""
        self.assertListEqual(self.linalg.add(v=V, w=W), [2.0, 5.5, 10, 14.5])
        with self.assertRaises(AssertionError):
            self.linalg.add(v=V, w=X)

    def test_subtract(self):
        """Test subtract method."""
        self.assertListEqual(self.linalg.subtract(v=V, w=W), [0, -0.5, 0, 0.5])
        with self.assertRaises(AssertionError):
            self.linalg.subtract(v=V, w=X)




