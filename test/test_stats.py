import unittest
from statistics.statistics import Stats

V = [1.0, 2.5, 5, 7.5]
W = [1, 3, 5, 7]
X = [0, 1.2, 3.4, 5.6, 7.8]
M = [V, W]
N = [V, X]
C = 2

class Test_Stats(unittest.TestCase):

    def setUp(self):
        self.stats = Stats()

    def test_num_points(self):
        """Test num_points method."""
        self.assertEqual(self.stats.num_points(vector=V), 4)
        with self.assertRaises(ValueError):
            self.assertEqual(self.stats.num_points(vector=C), 4)
            self.assertEqual(self.stats.num_points(vector='C'), 4)

    def test_vector_mean(self):
        """Test vector_mean method."""
        self.assertEqual(self.stats.vector_mean(vector=W), 4)
        with self.assertRaises(ValueError):
            self.assertEqual(self.stats.vector_mean(vector=C), 4)
            self.assertEqual(self.stats.vector_mean(vector='C'), 4)

    def test_vector_max(self):
        """Test vector_max method."""
        self.assertEqual(self.stats.vector_max(vector=W), 7)
        with self.assertRaises(ValueError):
            self.assertEqual(self.stats.vector_max(vector=C), 4)
            self.assertEqual(self.stats.vector_max(vector='C'), 4)

    def test_vector_min(self):
        """Test vector_min method."""
        self.assertEqual(self.stats.vector_min(vector=W), 1)
        with self.assertRaises(ValueError):
            self.assertEqual(self.stats.vector_min(vector=C), 4)
            self.assertEqual(self.stats.vector_min(vector='C'), 4)

    def test_vector_median(self):
        """Test vector_median method."""
        self.assertEqual(self.stats.vector_median(vector=W), 4)
        self.assertEqual(self.stats.vector_median(vector=X), 3.4)
        with self.assertRaises(ValueError):
            self.assertEqual(self.stats.vector_median(vector=C), 4)
            self.assertEqual(self.stats.vector_median(vector='C'), 4)

    def test_vector_quantile(self):
        """Test vector_quantile( method."""
        self.assertEqual(self.stats.vector_quantile(vector=W, q=0.25), 3)
        self.assertEqual(self.stats.vector_quantile(vector=W, q=0.6), 5)
        self.assertEqual(self.stats.vector_quantile(vector=X, q=0.5), 3.4)
        with self.assertRaises(ValueError):
            self.assertEqual(self.stats.vector_quantile(vector=C, q=0.25), 4)
            self.assertEqual(self.stats.vector_quantile(vector='C', q=0.25), 4)