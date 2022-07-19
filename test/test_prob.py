import random
import unittest
from probability.probability import Probability

V = [1.0, 2.5, 5, 7.5]
W = [1, 3, 5, 7]
X = [0, 1.2, 3.4, 5.6, 7.8]
M = [V, W]
N = [V, X]
C = 2

class Test_Probability(unittest.TestCase):

    def setUp(self):
        self.prob = Probability()

    def test_uniform_pdf(self):
        """Test uniform_pdf method."""
        self.assertEqual(self.prob.uniform_pdf(x=-1), 0)
        self.assertEqual(self.prob.uniform_pdf(x=0), 1)
        self.assertEqual(self.prob.uniform_pdf(x=0.5), 1)
        self.assertEqual(self.prob.uniform_pdf(x=1), 0)
        self.assertEqual(self.prob.uniform_pdf(x=1.5), 0)
        with self.assertRaises(ValueError):
            self.assertEqual(self.prob.uniform_pdf(x=[0.5]), 1)
            self.assertEqual(self.prob.uniform_pdf(x='0.5'), 1)

    def test_uniform_cdf(self):
        """Test uniform_cdf method."""
        self.assertEqual(self.prob.uniform_cdf(x=-1), 0)
        self.assertEqual(self.prob.uniform_cdf(x=0), 0)
        self.assertEqual(self.prob.uniform_cdf(x=0.5), 0.5)
        self.assertEqual(self.prob.uniform_cdf(x=1), 1)
        self.assertEqual(self.prob.uniform_cdf(x=1.5), 1)
        with self.assertRaises(ValueError):
            self.assertEqual(self.prob.uniform_cdf(x=[0.5]), 1)
            self.assertEqual(self.prob.uniform_cdf(x='0.5'), 1)

    def test_normal_pdf(self):
        """Test normal_pdf method."""
        self.assertEqual(round(self.prob.normal_pdf(x=-1, mu=0, sigma=1), 6), 0.241971)
        self.assertEqual(round(self.prob.normal_pdf(x=0, mu=-1, sigma=1), 6), 0.241971)
        with self.assertRaises(ValueError):
            self.assertEqual(round(self.prob.normal_pdf(x=0.5, mu=0, sigma=-1), 6), 0.352065)
            self.assertEqual(round(self.prob.normal_pdf(x=[-1], mu=0, sigma=1), 6), 0)
            self.assertEqual(round(self.prob.normal_pdf(x="0", mu=0, sigma=1), 6), 1)
            self.assertEqual(round(self.prob.normal_pdf(x=-1, mu="0", sigma=1), 6), 0)
            self.assertEqual(round(self.prob.normal_pdf(x=0, mu=[0], sigma=1), 6), 1)
            self.assertEqual(round(self.prob.normal_pdf(x=-1, mu=0, sigma="1"), 6), 0)
            self.assertEqual(round(self.prob.normal_pdf(x=0, mu=0, sigma=[1]), 6), 1)

    def test_normal_cdf(self):
        """Test normal_cdf method."""
        self.assertEqual(round(self.prob.normal_cdf(x=-1, mu=0, sigma=1), 6), 0.158655)
        self.assertEqual(round(self.prob.normal_cdf(x=0, mu=-1, sigma=1), 6), 0.841345)
        with self.assertRaises(ValueError):
            self.assertEqual(round(self.prob.normal_cdf(x=0.5, mu=0, sigma=-1), 6), 0.352065)
            self.assertEqual(round(self.prob.normal_cdf(x=[-1], mu=0, sigma=1), 6), 0)
            self.assertEqual(round(self.prob.normal_cdf(x="0", mu=0, sigma=1), 6), 1)
            self.assertEqual(round(self.prob.normal_cdf(x=-1, mu="0", sigma=1), 6), 0)
            self.assertEqual(round(self.prob.normal_cdf(x=0, mu=[0], sigma=1), 6), 1)
            self.assertEqual(round(self.prob.normal_cdf(x=-1, mu=0, sigma="1"), 6), 0)
            self.assertEqual(round(self.prob.normal_cdf(x=0, mu=0, sigma=[1]), 6), 1)

    def test_inverse_normal_cdf(self):
        """Test inverse_normal_cdf method."""
        self.assertEqual(round(self.prob.inverse_normal_cdf(x=0.158655, mu=0, sigma=1, tolerance=0.00001), 4), -1)
        self.assertEqual(round(self.prob.inverse_normal_cdf(x=0.841345, mu=-1, sigma=1, tolerance=0.00001), 4), 0)
        with self.assertRaises(ValueError):
            self.assertEqual(round(self.prob.inverse_normal_cdf(x=0.5, mu=0, sigma=-1, tolerance=0.00001), 6), 0.352065)
        with self.assertRaises(ValueError):
            self.assertEqual(round(self.prob.inverse_normal_cdf(x=[-1], mu=0, sigma=1, tolerance=0.00001), 6), 0)
        with self.assertRaises(ValueError):
            self.assertEqual(round(self.prob.inverse_normal_cdf(x="0", mu=0, sigma=1, tolerance=0.00001), 6), 1)
        with self.assertRaises(ValueError):
            self.assertEqual(round(self.prob.inverse_normal_cdf(x=-1, mu="0", sigma=1, tolerance=0.00001), 6), 0)
        with self.assertRaises(ValueError):
            self.assertEqual(round(self.prob.inverse_normal_cdf(x=0, mu=[0], sigma=1, tolerance=0.00001), 6), 1)
        with self.assertRaises(ValueError):
            self.assertEqual(round(self.prob.inverse_normal_cdf(x=-1, mu=0, sigma="1", tolerance=0.00001), 6), 0)
        with self.assertRaises(ValueError):
            self.assertEqual(round(self.prob.inverse_normal_cdf(x=0, mu=0, sigma=[1], tolerance=0.00001), 6), 1)

    def test_bernoulli_trial(self):
        """Test bernoullli_trial method."""
        random.seed(123)
        self.assertEqual(self.prob.bernoulli_trial(p=0.0), 0)
        self.assertEqual(self.prob.bernoulli_trial(p=0.5), 1)
        self.assertEqual(self.prob.bernoulli_trial(p=1.0), 1)
        with self.assertRaises(ValueError):
            self.assertEqual(self.prob.bernoulli_trial(p=C), 0)
        with self.assertRaises(ValueError):
            self.assertEqual(self.prob.bernoulli_trial(p='C'), 0)
        with self.assertRaises(ValueError):
            self.assertEqual(self.prob.bernoulli_trial(p=[0.5]), 0)

    def test_binomial(self):
        """Test binomial method."""
        random.seed(123)
        self.assertEqual(self.prob.binomial(n=10, p=0.0), 0)
        self.assertEqual(self.prob.binomial(n=10, p=0.5), 9)
        self.assertEqual(self.prob.binomial(n=10, p=1.0), 10)
        with self.assertRaises(ValueError):
            self.assertEqual(self.prob.binomial(n=-1, p=C), 0)
        with self.assertRaises(ValueError):
            self.assertEqual(self.prob.binomial(n=0.5, p=C), 0)
        with self.assertRaises(ValueError):
            self.assertEqual(self.prob.binomial(n=1, p=C), 0)
        with self.assertRaises(ValueError):
            self.assertEqual(self.prob.binomial(n=1, p='C'), 0)
        with self.assertRaises(ValueError):
            self.assertEqual(self.prob.binomial(n=1, p=[0.5]), 0)