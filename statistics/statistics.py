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

    def num_points(self, vector):
        """
        Returns the number of elements within the input vector.
        """
        validate_vector(vector)
        return self._num_points_(vector=vector)

    def _num_points_(self, vector):
        """
        Returns the number of elements within the input vector.
        """
        return len(vector)

    def vector_mean(self, vector):
        """
        Returns the arithmetic mean of the input vector elements.
        """
        validate_vector(vector)
        return self._vector_mean_(vector=vector)

    def _vector_mean_(self, vector):
        """
        Returns the arithmetic mean of the input vector elements.
        """
        return sum(vector) / self._num_points_(vector)

    def vector_max(self, vector):
        """
        Returns the largest vector element.
        """
        validate_vector(vector)
        return self._vector_max_(vector=vector)

    def _vector_max_(self, vector):
        """
        Returns the largest vector element.
        """
        return max(vector)

    def vector_min(self, vector):
        """
        Returns the smallest vector element.
        """
        validate_vector(vector)
        return self._vector_min_(vector=vector)

    def _vector_min_(self, vector):
        """
        Returns the smallest vector element.
        """
        return min(vector)

    def vector_median(self, vector):
        """
        Returns the median value of the input vector.
        """
        validate_vector(vector)
        return self._vector_median_(vector=vector)

    def _vector_median_(self, vector):
        """
        Returns the median value of the input vector.
        """
        n = self._num_points_(vector=vector)
        sorted_vector = sorted(vector)
        midpoint = n // 2           # Floor division to get index of median value

        if n % 2 == 1:              # If n is odd
            return sorted_vector[midpoint]
        else:                       # If n is even, take average of two center values
            return (sorted_vector[midpoint] + sorted_vector[midpoint - 1]) / 2

    def vector_quantile(self, vector, q):
        """
        Returns the pth percentile value in the input vector.
        """
        validate_vector(vector)
        return self._vector_quantile_(vector=vector, q=q)

    def _vector_quantile_(self, vector, q):
        """
        Returns the pth percentile value in the input vector.

        For example, the value returned for a p value of 0.25, 25% of the data points would be below the returned value,
        and 75% would be greater than the returned value.

        """
        q_index = int(q * self._num_points_(vector=vector))
        return sorted(vector)[q_index]

    def vector_mode(self, vector):
        """
        Returns the most common value (or values) in the vector as a list (since there can be more than one).
        """
        validate_vector(vector)
        return self._vector_mode_(vector)

    def _vector_mode_(self, vector):
        """
        Returns the most common value (or values) in the vector as a list.
        """
        counts = Counter(vector)
        max_count = max(counts.values())
        return [x for x, count in counts.items() if count == max_count]

    def vector_range(self, vector):
        """
        Returns the dispersion (maximum value - the minimum value) of the input vector.
        """
        validate_vector(vector)
        return self._vector_range_(vector=vector)

    def _vector_range_(self, vector):
        """
        Returns the dispersion (maximum value - the minimum value) of the input vector.
        """
        return self._vector_max_(vector=vector) - self._vector_min_(vector=vector)

    def vector_de_mean(self, vector):
        """
        Returns a new vector in which the vector mean has been subtracted from each element, so that the mean of the
        new vector is 0. In other words, translate the vector by its mean.
        """
        validate_vector(vector)
        return self._vector_de_mean_(vector=vector)

    def _vector_de_mean_(self, vector):
        """
        Returns a new vector in which the vector mean has been subtracted from each element, so that the mean of the
        new vector is 0. In other words, translate the vector by its mean.
        """
        mu = self._vector_mean_(vector=vector)
        return [x - mu for x in vector]

    def vector_variance(self, vector):
        """
        Returns the variance of the input vector, which is assumed to have at least 2 elements.

        Note - We divide by n-1 instead of n because when the vector is a partial sampling from a much larger dataset,
        the mean of the sample is only an estimate of the mean of the full dataset. This means that on average the
        square of each elements deviation [(x - mu) ** 2 ] from the mean is underestimated, and we divide by (n - 1)
        in an attempt to remove that bias.

        https://en.wikipedia.org/wiki/Unbiased_estimation_of_standard_deviation
        """
        validate_vector(vector)
        return self._vector_variance_(vector=vector)

    def _vector_variance_(self, vector):
        """
        Returns the variance of the input vector, which is assumed to have at least 2 elements.
        """
        validate_vector(vector)
        return la()._sum_of_squares_(v=self._vector_de_mean_(vector=vector)) / (self._num_points_(vector=vector) - 1)

    def vector_standard_deviation(self, vector):
        """
        Returns the standard deviation of the input vector, calculated as the square root of the variance.
        """
        validate_vector(vector)
        return self._vector_standard_deviation_(vector=vector)

    def _vector_standard_deviation_(self, vector):
        """
        Returns the standard deviation of the input vector, calculated as the square root of the variance.
        """
        return sqrt(self._vector_variance_(vector=vector))

    def vector_covariance(self, v, w):
        """
        Returns the covariance of two input vectors. Te covariance measures how two variables vary in tandem from their
        means.

        Recall the dot product sums up the products of the corresponding pairs of elements, so the covariance is the sum
        of the products of the variances of the corresponding pairs of elements, divided by n - 1.

        """
        validate_matrix([v, w])
        return self._vector_covariance_(v=v, w=w)

    def _vector_covariance_(self, v, w):
        """
        Returns the covariance of two input vectors.
        """

        return la()._dot_product_(v=self._vector_de_mean_(vector=v),
                                  w=self._vector_de_mean_(vector=w)) / (self._num_points_(v) - 1)

    def vector_correlation(self, v, w):
        """
        Returns the correlation between the two input variables, calculated as the covariance of the two vectors divided
        by their respective standard deviations.

        Correlation will always be between -1 (perfect anti-correlation) and 1 (perfect correlation). The closer to 0,
        the weaker the correlation.

        """
        validate_matrix([v, w])
        return self._vector_correlation_(v=v, w=w)

    def _vector_correlation_(self, v, w):
        """
        Returns the correlation between the two input variables, calculated as the covariance of the two vectors divided
        by their respective standard deviations.

        """
        stdev_v = self._vector_standard_deviation_(vector=v)
        stdev_w = self._vector_standard_deviation_(vector=w)
        if stdev_v > 0 and stdev_w > 0:
            return self._vector_covariance_(v, w) / stdev_v / stdev_w
        else:
            return 0
