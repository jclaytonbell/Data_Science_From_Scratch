# CHAPTER 4: LINEAR ALGEBRA
import math

class LinearAlgebra():
    """
    A class to define linear algebra vector and matrix operations.
    """

    def __init__(self):
        """
        Initialize class.
        """

    def distance(self, v, w):
        """
        Returns the distance between two vectors of the same dimensions, i.e., the magnitude of the vector created by
        subtracting the two input vectors.

        distance = sqrt( (v_1 - w_1) ^ 2 + (v_2 - w_2) ^ 2 + ..... + (v_n - w_n) ^ 2 )

        """
        return self.vector_magnitude(v=self.vector_subtract(v, w))

    def squared_distance(self, v, w):
        """
        Returns the sum of the squared differences between two vectors of the same dimensions.

        squared_distance = (v_1 - w_1) ^ 2 + (v_2 - w_2) ^ 2 + ..... + (v_n - w_n) ^ 2

        """
        return self.sum_of_squares(v=self.vector_subtract(v, w))

    def vector_magnitude(self, v):
        """
        Returns the magnitude of a vector, i.e., the square root of the dot product of a vector and itself.

        magnitude = sqrt(v_1 ^ 2 + v_2 ^ 2 + ..... + v_n ^ 2)

        """
        self._validate_vector_(vector=v)
        return math.sqrt(self.sum_of_squares(v=v))

    def sum_of_squares(self, v):
        """
        Returns the sum of squares of a vector, i.e., the dot product of a vector and itself.

        sum_of_squares = v_1 ^ 2 + v_2 ^ 2 + ..... + v_n ^ 2

        """
        self._validate_vector_(vector=v)
        return self.dot_product(v=v, w=v)

    def dot_product(self, v, w):
        """
        Returns the dot product of two vectors, i.e., the sum of the products of the vector elements:

        dot_product = v_1 * w_1 + v_2 * w_2 + ..... + v_n * w_n

        """
        self._validate_vectors_same_length_(vector_list=[v, w])
        return sum(v_i * w_i for v_i, w_i in zip(v, w))

    def vector_mean(self, vector_list):
        """
        Return a new vector created by summing a list of vectors of the same dimensions, and dividing each element by
        the number of the input vectors (i.e., returns the average of each vector element)

        n = len(vector_list)
        x = [(v[0] + w[0]) / n, (v[1] + w[1]) / n,....(v[n] + w[n]) / n]

        """
        self._validate_vectors_same_length_(vector_list=vector_list)
        n = len(vector_list)
        return self.scalar_multiply(1 / n, self.vector_sum(vector_list=vector_list))

    def scalar_multiply(self, c, v):
        """
        Returns the a new vector created by multiplying the input vector by a scalar.

        x = [c * v[0], c * v[1],....c * v[n]]

        """
        self._validate_scalar_(scalar=c)
        self._validate_vector_(vector=v)
        return [c * v_i for v_i in v]

    def vector_sum(self, vector_list):
        """
        Return a new vector created by summing a list of vectors of the same dimensions.
        """
        result = vector_list[0]
        for v in vector_list[1:]:
            result = self.vector_add(v=result, w=v)
        return result

    def vector_add(self, v, w):
        """
        Return a new vector created by adding two input vectors (v and w) of the same dimensions.

        x = [v[0] + w[0], v[1] + w[1],....v[n] + w[n]]

        """
        vector_list = [v, w]
        self._validate_vectors_same_length_(vector_list=vector_list)
        return [v_i + w_i for v_i, w_i in zip(v, w)]

    def vector_subtract(self, v, w):
        """
        Return a new vector created by the difference of two input vectors (v and w) of the same dimensions.

        x = [v[0] - w[0], v[1] - w[1],....v[n] - w[n]]

        """
        vector_list = [v, w]
        self._validate_vectors_same_length_(vector_list=vector_list)
        return [v_i - w_i for v_i, w_i in zip(v, w)]

    def _validate_vectors_same_length_(self, vector_list):
        """
        Return True if inputs are vectors of the same length
        """
        if self._validate_vectors_(vector_list=vector_list):
            a = len(vector_list[0])
            if all(len(i) == a for i in vector_list):
                return True
            else:
                raise AssertionError("Vectors are not the same length.")

    def _validate_vectors_(self, vector_list):
        """
        Return True if input is a list of valid vectors.
        """
        if isinstance(vector_list, list):
            if all([self._validate_vector_(vector=i) for i in vector_list]):
                return True
        else:
            raise ValueError("Vectors must be represented by a list of numeric values.")

    @staticmethod
    def _validate_vector_(vector):
        """
        Return True if input is a list of numbers.
        """
        if isinstance(vector, list):
            if all([isinstance(i, (int, float)) for i in vector]):
                return True
        else:
            raise ValueError("Vectors must be represented by a list of numeric values.")

    @staticmethod
    def _validate_scalar_(scalar):
        """
        Return True if input is a number.
        """
        if isinstance(scalar, (int, float)):
            return True
        else:
            raise ValueError("Scalars must be numeric values.")

