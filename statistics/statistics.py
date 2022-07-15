# CHAPTER 5: STATISTICS
from collections import Counter
from math import sqrt
from util import validate_scalar, validate_vector, validate_matrix
from linear_algebra.linear_algebra import LinearAlgebra as la

class Stats():
    """
    A class to define statistical operations.
    """

    def __init__(self):
        """
        Initialize class.
        """

    def num_points(self, v):
        """
        Returns the number of elements within the input vector.
        """
        validate_vector(v)
        return self._num_points_(v=v)

    def _num_points_(self, v):
        """
        Returns the number of elements within the input vector.
        """
        return len(v)

    def mean(self, v):
        """
        Returns the arithmetic mean of the input vector elements.
        """
        validate_vector(v)
        return self._mean_(v=v)

    def _mean_(self, v):
        """
        Returns the arithmetic mean of the input vector elements.
        """
        return sum(v) / self._num_points_(v)

    def max(self, v):
        """
        Returns the largest vector element.
        """
        validate_vector(v)
        return self._max_(v=v)

    def _max_(self, v):
        """
        Returns the largest vector element.
        """
        return max(v)

    def min(self, v):
        """
        Returns the smallest vector element.
        """
        validate_vector(v)
        return self._min_(v=v)

    def _min_(self, v):
        """
        Returns the smallest vector element.
        """
        return min(v)

    def median(self, v):
        """
        Returns the median value of the input vector.
        """
        validate_vector(v)
        return self._median_(v=v)

    def _median_(self, v):
        """
        Returns the median value of the input vector.
        """
        n = self._num_points_(v=v)
        sorted_vector = sorted(v)
        midpoint = n // 2           # Floor division to get index of median value

        if n % 2 == 1:              # If n is odd
            return sorted_vector[midpoint]
        else:                       # If n is even, take average of two center values
            return (sorted_vector[midpoint] + sorted_vector[midpoint - 1]) / 2

    def quantile(self, v, q):
        """
        Returns the pth percentile value in the input vector.
        """
        validate_vector(v)
        return self._quantile_(v=v, q=q)

    def _quantile_(self, v, q):
        """
        Returns the pth percentile value in the input vector.

        For example, the value returned for a p value of 0.25, 25% of the data points would be below the returned value,
        and 75% would be greater than the returned value.

        """
        q_index = int(q * self._num_points_(v=v))
        return sorted(v)[q_index]

    def mode(self, v):
        """
        Returns the most common value (or values) in the vector as a list (since there can be more than one).
        """
        validate_vector(v)
        return self._mode_(v)

    def _mode_(self, v):
        """
        Returns the most common value (or values) in the vector as a list.
        """
        counts = Counter(v)
        max_count = max(counts.values())
        return [x for x, count in counts.items() if count == max_count]

    def range(self, v):
        """
        Returns the dispersion (maximum value - the minimum value) of the input vector.
        """
        validate_vector(v)
        return self._range_(v=v)

    def _range_(self, v):
        """
        Returns the dispersion (maximum value - the minimum value) of the input vector.
        """
        return self._max_(v=v) - self._min_(v=v)

    def de_mean(self, v):
        """
        Returns a new vector in which the vector mean has been subtracted from each element, so that the mean of the
        new vector is 0. In other words, translate the vector by its mean.
        """
        validate_vector(v)
        return self._de_mean_(v=v)

    def _de_mean_(self, v):
        """
        Returns a new vector in which the vector mean has been subtracted from each element, so that the mean of the
        new vector is 0. In other words, translate the vector by its mean.
        """
        mu = self._mean_(v=v)
        return [x - mu for x in v]

    def variance(self, v):
        """
        Returns the variance of the input vector, which is assumed to have at least 2 elements.

        Note - We divide by n-1 instead of n because when the vector is a partial sampling from a much larger dataset,
        the mean of the sample is only an estimate of the mean of the full dataset. This means that on average the
        square of each elements deviation [(x - mu) ** 2 ] from the mean is underestimated, and we divide by (n - 1)
        in an attempt to remove that bias.

        https://en.wikipedia.org/wiki/Unbiased_estimation_of_standard_deviation
        """
        validate_vector(v)
        return self._variance_(v=v)

    def _variance_(self, v):
        """
        Returns the variance of the input vector, which is assumed to have at least 2 elements.
        """
        validate_vector(v)
        return la()._sum_of_squares_(v=self._de_mean_(v=v)) / (self._num_points_(v=v) - 1)

    def standard_deviation(self, v):
        """
        Returns the standard deviation of the input vector, calculated as the square root of the variance.
        """
        validate_vector(v)
        return self._standard_deviation_(v=v)

    def _standard_deviation_(self, v):
        """
        Returns the standard deviation of the input vector, calculated as the square root of the variance.
        """
        return sqrt(self._variance_(v=v))

    def interquartile_range(self, v):
        """
        Returns the range between the 75th percentile value and the 25th percentile value.
        """
        validate_vector(v)
        return self._interquartile_range_(v=v)

    def _interquartile_range_(self, v):
        """
        Returns the range between the 75th percentile value and the 25th percentile value.
        """
        return self._quantile_(v=v, q=0.75) - self._quantile_(v=v, q=0.25)

    def covariance(self, v, w):
        """
        Returns the covariance of two input vectors. Te covariance measures how two variables vary in tandem from their
        means.

        Recall the dot product sums up the products of the corresponding pairs of elements, so the covariance is the sum
        of the products of the variances of the corresponding pairs of elements, divided by n - 1.

        """
        validate_matrix([v, w])
        return self._covariance_(v=v, w=w)

    def _covariance_(self, v, w):
        """
        Returns the covariance of two input vectors.
        """

        return la()._dot_product_(v=self._de_mean_(v=v),
                                  w=self._de_mean_(v=w)) / (self._num_points_(v) - 1)

    def correlation(self, v, w):
        """
        Returns the correlation between the two input variables, calculated as the covariance of the two vectors divided
        by their respective standard deviations.

        Correlation will always be between -1 (perfect anti-correlation) and 1 (perfect correlation). The closer to 0,
        the weaker the correlation.

        """
        validate_matrix([v, w])
        return self._correlation_(v=v, w=w)

    def _correlation_(self, v, w):
        """
        Returns the correlation between the two input variables, calculated as the covariance of the two vectors divided
        by their respective standard deviations.

        """
        stdev_v = self._standard_deviation_(v=v)
        stdev_w = self._standard_deviation_(v=w)
        if stdev_v > 0 and stdev_w > 0:
            return self._covariance_(v, w) / stdev_v / stdev_w
        else:
            return 0
