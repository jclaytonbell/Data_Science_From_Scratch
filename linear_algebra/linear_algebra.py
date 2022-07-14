# CHAPTER 4: LINEAR ALGEBRA
from util import validate_scalar, validate_vector, validate_matrix
from math import sqrt

class LinearAlgebra():
    """
    A class to define linear algebra vector and matrix operations.
    """

    def __init__(self):
        """
        Initialize class.
        """

    def is_diagonal(self, i, j):
        """
        Returns 1 when i == j (i.e., the diagonal), other wise returns 0.
        """
        return 1 if i == j else 0

    def ones(self, i, j):
        """
        Returns 1 for all elements in the matrix.
        """
        return 1

    def zeroes(self, i, j):
        """
        Returns 1 for all elements in the matrix.
        """
        return 0

    def make_matrix(self, n_rows, n_columns, entry_fn=None):
        """
        Returns a new matrix with n_rows and n_columns, whose (i, j)th element is set by the given entry function
        entry_fn(i, j).
        """
        if not all([isinstance(i, int) and i > 0 for i in [n_rows, n_columns]]):
            raise ValueError("n_rows and n_columns must be positive integers.")
        if entry_fn is None:
            entry_fn = self.zeroes
        return [[entry_fn(i, j) for j in range(n_columns)] for i in range(n_rows)]

    def get_row(self, m, i):
        """
        Returns the ith row of the input matrix.
        """
        validate_matrix(m)
        return self._get_row_(m=m, i=i)

    def _get_row_(self, m, i):
        """
        Returns the ith row of the input matrix.
        """
        return m[i]

    def get_column(self, m, j):
        """
        Returns the jth column of the input matrix.
        """
        validate_matrix(m)
        return self._get_column_(m=m, j=j)

    def _get_column_(self, m, j):
        """
        Returns the jth column of the input matrix.
        """
        return [v[j] for v in m]

    def matrix_shape(self, m):
        """
        Return the shape of the input matrix (number of rows, number of columns).
        """
        validate_matrix(m)
        return self._matrix_shape_(m=m)

    def _matrix_shape_(self, m):
        """
        Return the shape of the input matrix (number of rows, number of columns).
        """
        return len(m), len(m[0])

    def distance(self, v, w):
        """
        Returns the distance between two vectors of the same dimensions, i.e., the magnitude of the vector created by
        subtracting the two input vectors.

        distance = sqrt( (v_1 - w_1) ^ 2 + (v_2 - w_2) ^ 2 + ..... + (v_n - w_n) ^ 2 )

        """
        validate_matrix(matrix=[v, w])
        return self._distance_(v=v, w=w)

    def _distance_(self, v, w):
        """
        Returns the distance between two vectors of the same dimensions, i.e., the magnitude of the vector created by
        subtracting the two input vectors.

        distance = sqrt( (v_1 - w_1) ^ 2 + (v_2 - w_2) ^ 2 + ..... + (v_n - w_n) ^ 2 )

        """
        return self._vector_magnitude_(v=self._vector_subtract_(v, w))

    def squared_distance(self, v, w):
        """
        Returns the sum of the squared differences between two vectors of the same dimensions.

        squared_distance = (v_1 - w_1) ^ 2 + (v_2 - w_2) ^ 2 + ..... + (v_n - w_n) ^ 2

        """
        validate_matrix(matrix=[v, w])
        return self._squared_distance_(v=v, w=w)

    def _squared_distance_(self, v, w):
        """
        Returns the sum of the squared differences between two vectors of the same dimensions.

        squared_distance = (v_1 - w_1) ^ 2 + (v_2 - w_2) ^ 2 + ..... + (v_n - w_n) ^ 2

        """
        return self._sum_of_squares_(v=self._vector_subtract_(v, w))

    def vector_magnitude(self, v):
        """
        Returns the magnitude of a vector, i.e., the square root of the dot product of a vector and itself.

        magnitude = sqrt(v_1 ^ 2 + v_2 ^ 2 + ..... + v_n ^ 2)

        """
        validate_vector(vector=v)
        return self._vector_magnitude_(v=v)

    def _vector_magnitude_(self, v):
        """
        Returns the magnitude of a vector, i.e., the square root of the dot product of a vector and itself.

        magnitude = sqrt(v_1 ^ 2 + v_2 ^ 2 + ..... + v_n ^ 2)

        """
        return sqrt(self._sum_of_squares_(v=v))

    def sum_of_squares(self, v):
        """
        Returns the sum of squares of a vector, i.e., the dot product of a vector and itself.

        sum_of_squares = v_1 ^ 2 + v_2 ^ 2 + ..... + v_n ^ 2

        """
        validate_vector(vector=v)
        return self._sum_of_squares_(v=v)

    def _sum_of_squares_(self, v):
        """
        Returns the sum of squares of a vector, i.e., the dot product of a vector and itself.

        sum_of_squares = v_1 ^ 2 + v_2 ^ 2 + ..... + v_n ^ 2

        """
        return self._dot_product_(v=v, w=v)

    def dot_product(self, v, w):
        """
        Returns the dot product of two vectors, i.e., the sum of the products of the vector elements:

        dot_product = v_1 * w_1 + v_2 * w_2 + ..... + v_n * w_n

        """
        validate_matrix(matrix=[v, w])
        return self._dot_product_(v=v, w=w)

    def _dot_product_(self, v, w):
        """
        Returns the dot product of two vectors, i.e., the sum of the products of the vector elements:

        dot_product = v_1 * w_1 + v_2 * w_2 + ..... + v_n * w_n

        """
        return sum(v_i * w_i for v_i, w_i in zip(v, w))

    def vector_mean(self, vector_list):
        """
        Return a new vector created by summing a list of vectors of the same dimensions, and dividing each element by
        the number of the input vectors (i.e., returns the average of each vector element)

        n = len(vector_list)
        x = [(v[0] + w[0]) / n, (v[1] + w[1]) / n,....(v[n] + w[n]) / n]

        """
        validate_matrix(matrix=vector_list)
        return self._vector_mean_(vector_list=vector_list)

    def _vector_mean_(self, vector_list):
        """
        Return a new vector created by summing a list of vectors of the same dimensions, and dividing each element by
        the number of the input vectors (i.e., returns the average of each vector element)

        n = len(vector_list)
        x = [(v[0] + w[0]) / n, (v[1] + w[1]) / n,....(v[n] + w[n]) / n]

        """
        return self.scalar_multiply(1 / len(vector_list), self._vector_sum_(vector_list=vector_list))

    def scalar_multiply(self, c, v):
        """
        Returns the a new vector created by multiplying the input vector by a scalar.

        x = [c * v[0], c * v[1],....c * v[n]]

        """
        validate_scalar(scalar=c)
        validate_vector(vector=v)
        return self._scalar_multiply_(c=c, v=v)

    def _scalar_multiply_(self, c, v):
        """
        Returns the a new vector created by multiplying the input vector by a scalar.

        x = [c * v[0], c * v[1],....c * v[n]]

        """
        return [c * v_i for v_i in v]

    def vector_sum(self, vector_list):
        """
        Return a new vector created by summing a list of vectors of the same dimensions.
        """
        validate_matrix(matrix=vector_list)
        return self._vector_sum_(vector_list=vector_list)

    def _vector_sum_(self, vector_list):
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
        validate_matrix(matrix=[v, w])
        return self._vector_add_(v=v, w=w)

    def _vector_add_(self, v, w):
        """
        Return a new vector created by adding two input vectors (v and w) of the same dimensions.

        x = [v[0] + w[0], v[1] + w[1],....v[n] + w[n]]

        """
        return [v_i + w_i for v_i, w_i in zip(v, w)]

    def vector_subtract(self, v, w):
        """
        Return a new vector created by the difference of two input vectors (v and w) of the same dimensions.

        x = [v[0] - w[0], v[1] - w[1],....v[n] - w[n]]

        """
        validate_matrix(matrix=[v, w])
        return self._vector_subtract_(v=v, w=w)

    def _vector_subtract_(self, v, w):
        """
        Return a new vector created by the difference of two input vectors (v and w) of the same dimensions.

        x = [v[0] - w[0], v[1] - w[1],....v[n] - w[n]]

        """
        return [v_i - w_i for v_i, w_i in zip(v, w)]





