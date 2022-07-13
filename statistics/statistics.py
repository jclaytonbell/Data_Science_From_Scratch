# CHAPTER 5: STATISTICS
from util import validate_scalar, validate_vector

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