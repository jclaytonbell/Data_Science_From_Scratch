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
        self.assertEqual(self.stats.num_points(v=V), 4)
        with self.assertRaises(ValueError):
            self.assertEqual(self.stats.num_points(v=C), 4)
            self.assertEqual(self.stats.num_points(v='C'), 4)

    def test_mean(self):
        """Test mean method."""
        self.assertEqual(self.stats.mean(v=W), 4)
        with self.assertRaises(ValueError):
            self.assertEqual(self.stats.mean(v=C), 4)
            self.assertEqual(self.stats.mean(v='C'), 4)

    def test_max(self):
        """Test max method."""
        self.assertEqual(self.stats.max(v=W), 7)
        with self.assertRaises(ValueError):
            self.assertEqual(self.stats.max(v=C), 4)
            self.assertEqual(self.stats.max(v='C'), 4)

    def test_min(self):
        """Test min method."""
        self.assertEqual(self.stats.min(v=W), 1)
        with self.assertRaises(ValueError):
            self.assertEqual(self.stats.min(v=C), 4)
            self.assertEqual(self.stats.min(v='C'), 4)

    def test_median(self):
        """Test median method."""
        self.assertEqual(self.stats.median(v=W), 4)
        self.assertEqual(self.stats.median(v=X), 3.4)
        with self.assertRaises(ValueError):
            self.assertEqual(self.stats.median(v=C), 4)
            self.assertEqual(self.stats.median(v='C'), 4)

    def test_quantile(self):
        """Test quantile( method."""
        self.assertEqual(self.stats.quantile(v=W, q=0.25), 3)
        self.assertEqual(self.stats.quantile(v=W, q=0.6), 5)
        self.assertEqual(self.stats.quantile(v=X, q=0.5), 3.4)
        with self.assertRaises(ValueError):
            self.assertEqual(self.stats.quantile(v=C, q=0.25), 4)
            self.assertEqual(self.stats.quantile(v='C', q=0.25), 4)

    def test_mode(self):
        """Test mode method."""
        self.assertListEqual(self.stats.mode(v=V+W), [1, 5])
        self.assertListEqual(self.stats.mode(v=V + W + V[0:2]), [1])
        with self.assertRaises(ValueError):
            self.assertListEqual(self.stats.mode(v=C), [4])
            self.assertListEqual(self.stats.mode(v='C'), [4])

    def test_range(self):
        """Test range method."""
        self.assertEqual(self.stats.range(v=W), 6)
        with self.assertRaises(ValueError):
            self.assertEqual(self.stats.range(v=C), 4)
            self.assertEqual(self.stats.range(v='C'), 4)

    def test_de_mean(self):
        """Test de_mean method."""
        self.assertListEqual(self.stats.de_mean(v=W), [-3, -1, 1, 3])
        with self.assertRaises(ValueError):
            self.assertListEqual(self.stats.de_mean(v=C), [-3, -1, 1, 3])
            self.assertListEqual(self.stats.de_mean(v='C'), [-3, -1, 1, 3])

    def test_variance(self):
        """Test variance method."""
        self.assertEqual(round(self.stats.variance(v=W), 6), 6.666667)
        with self.assertRaises(ValueError):
            self.assertEqual(self.stats.variance(v=C), 2)
            self.assertEqual(self.stats.variance(v='C'), 2)

    def test_standard_deviation(self):
        """Test standard_deviation method."""
        self.assertEqual(round(self.stats.standard_deviation(v=W), 6), 2.581989)
        with self.assertRaises(ValueError):
            self.assertEqual(self.stats.standard_deviation(v=C), 2)
            self.assertEqual(self.stats.standard_deviation(v='C'), 2)

    def test_interquartile_range(self):
        """Test interquartile_range method."""
        self.assertEqual(round(self.stats.interquartile_range(v=W), 6), 4)
        with self.assertRaises(ValueError):
            self.assertEqual(self.stats.interquartile_range(v=C), 2)
            self.assertEqual(self.stats.interquartile_range(v='C'), 2)

    def test_covariance(self):
        """Test covariance method."""
        self.assertEqual(round(self.stats.covariance(v=V, w=W), 6), 7.333333)
        with self.assertRaises(ValueError):
            self.assertEqual(self.stats.covariance(v=V, w=C), 2)
            self.assertEqual(self.stats.covariance(v=V, w='C'), 2)

    def test_correlation(self):
        """Test correlation method."""
        self.assertEqual(round(self.stats.correlation(v=V, w=W), 6), 0.993859)
        with self.assertRaises(ValueError):
            self.assertEqual(self.stats.correlation(v=V, w=C), 2)
            self.assertEqual(self.stats.correlation(v=V, w='C'), 2)