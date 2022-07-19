#CHAPTER 6: PROBABILITY
from util import validate_scalar, validate_vector, validate_matrix, validate_positive_scalar, validate_probability,\
    validate_positive_integer
from math import erf, exp, pi, sqrt
import random

class Probability():
    """
    A class to define probability methods and related operations.
    """

    def __init__(self):
        """
        Initialize class.
        """

    def uniform_pdf(self, x):
        """
        Returns the uniform probability density function of x.
        """
        validate_scalar(scalar=x)
        return self._uniform_pdf_(x=x)

    def _uniform_pdf_(self, x):
        """
        Returns the uniform probability density function of x.
        """
        return 1 if x >=0 and x < 1 else 0

    def uniform_cdf(self, x):
        """
        Returns the uniform cumulative density function of x, the probability that a uniform random variable is <= x.
        """
        validate_scalar(scalar=x)
        return self._uniform_cdf_(x=x)

    def _uniform_cdf_(self, x):
        """
        Returns the uniform cumulative density function of x, the probability that a uniform random variable is <= x.
        """
        if x < 0:
            return 0
        elif x < 1:
            return x
        else:
            return 1

    def normal_pdf(self, x, mu=0, sigma=1):
        """
        Returns the normal probabilty density function of x, with mean (mu) and standard deviation (sigma).
        """
        validate_scalar(scalar=x)
        validate_scalar(scalar=mu)
        validate_positive_scalar(scalar=sigma)
        return self._normal_pdf_(x=x, mu=mu, sigma=sigma)

    def _normal_pdf_(self, x, mu=0, sigma=1):
        """
        Returns the normal probabilty density function of x, with mean (mu) and standard deviation (sigma).
        """
        return exp((-(x - mu) ** 2) / (2 * sigma ** 2)) / (sigma * sqrt(2 * pi))

    def normal_cdf(self, x, mu=0, sigma=1):
        """
        Returns the cumulative density density function of x, with mean (mu) and standard deviation (sigma).
        """
        validate_scalar(scalar=x)
        validate_scalar(scalar=mu)
        validate_positive_scalar(scalar=sigma)
        return self._normal_cdf_(x=x, mu=mu, sigma=sigma)

    def _normal_cdf_(self, x, mu=0, sigma=1):
        """
        Returns the normal cumulative density function of x, with mean (mu) and standard deviation (sigma).
        """
        return (1 + erf((x - mu) / sqrt(2) / sigma)) / 2

    def inverse_normal_cdf(self, x, mu=0, sigma=1, tolerance=0.00001):
        """
        Returns the cumulative density density function of x, with mean (mu) and standard deviation (sigma).
        """
        validate_scalar(scalar=x)
        validate_scalar(scalar=mu)
        validate_positive_scalar(scalar=sigma)
        return self._inverse_normal_cdf_(x=x, mu=mu, sigma=sigma, tolerance=tolerance)

    def _inverse_normal_cdf_(self, x, mu=0, sigma=1, tolerance=0.00001):
        """
        Returns the approximate inverse of the normal cumulative density function of x using binary search, with mean
        (mu) and standard deviation (sigma).
        """
        # If not standard normal, compute as if standard, and then rescale by multiplying by sigma and adding mu.
        if mu != 0 or sigma != 1:
            return mu + sigma * self._inverse_normal_cdf_(x=x, mu=0, sigma=1, tolerance=tolerance)

        low_z, low_x = -10.0, 0.0                           # normal_cdf(-10 is very very close to 0
        hi_z, hi_x = 10.0, 1.0                              # normal_cdf(10 is very very close to 1
        while hi_z - low_z > tolerance:
            mid_z = (low_z + hi_z) / 2                      # get midpoint
            mid_x = self._normal_cdf_(x=mid_z, mu=0, sigma=1)
            if mid_x < x:                                   # midpoint is too low
                low_z, low_x = mid_z, mid_x
            elif mid_x > x:                                 # midpoint is too high
                hi_z, hi_x = mid_z, mid_x
            else:
                break

        return mid_z

    def bernoulli_trial(self, p):
        """
        Returns 1 if input probability is less than a random number, else returns 0 (i.e., a coin flip).
        """
        validate_probability(scalar=p)
        return self._bernoulli_trial_(p=p)

    def _bernoulli_trial_(self, p):
        """
        Returns 1 if input probability is less than a random number, else returns 0.
        """
        return 1 if random.random() < p else 0

    def binomial(self, n, p):
        """
        Returns the sum of the results of n Beroulli trials
        """
        validate_positive_integer(n)
        validate_probability(scalar=p)
        return self._binomial_(n=n, p=p)

    def _binomial_(self, n, p):
        """
        Returns the sum of the results of n Beroulli trials
        """
        return sum(self.bernoulli_trial(p=p) for _ in range(n))