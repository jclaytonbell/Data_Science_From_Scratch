# CHAPTER 4: LINEAR ALGEBRA

class LinearAlgebra():
    """
    A class to define linear algebra vector and matrix operations.
    """

    def __init__(self):
        """
        Initialize class
        """

    def vector_add(self, v, w):
        """
        Return a new vector created by the sum of two input vectors (v and w) of the same dimensions.

        x = [v[0] + w[0], v[1] + w[1],....v[n] + w[n]]

        """
        vector_list = [v, w]
        self._validate_vectors_same_length_(vector_list=vector_list)
        return [v_i + w_i for v_i, w_i in zip(v, w)]

    def _validate_vectors_same_length_(self, vector_list):
        """
        Return True if inputs are vectors of the same length
        """
        if self._validate_vectors_(vector_list=vector_list):
            a = len(vector_list[0])
            if all(len(i) == a for i in vector_list):
                return True
            else:
                raise ValueError("Vectors are not the same length.")

    def _validate_vectors_(self, vector_list):
        """
        Return True if input is a list of valid vectors.
        """
        if isinstance(vector_list, list):
            if all([self._validate_vector_(i) for i in vector_list]):
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

