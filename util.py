
def validate_vector(v):
    """
    Return True if input is a list of numbers.
    """
    err_msg = "Vectors must be represented by a list of numeric values."
    if isinstance(v, list):
        if not len(v) > 0:
            raise ValueError(err_msg)
        if all([isinstance(i, (int, float)) for i in v]):
            return True
        else:
            raise ValueError(err_msg)
    else:
        raise ValueError(err_msg)

def validate_scalar(scalar):
    """
    Return True if input is a number.
    """
    if isinstance(scalar, (int, float)):
        return True
    else:
        raise ValueError("Scalars must be numeric values.")

def validate_positive_scalar(scalar):
    """
    Return True if input is a positive number.
    """
    if isinstance(scalar, (int, float)) and (scalar >= 0):
        return True
    else:
        raise ValueError("Must be a positive number.")

def validate_positive_integer(i):
    """
    Return True if input is a positive integer.
    """
    if isinstance(i, int) and (i >= 0):
        return True
    else:
        raise ValueError("Must be a positive integer.")

def validate_probability(scalar):
    """
    Return True if input is a real number between 0.0 and 1.0
    """
    if isinstance(scalar, (int, float)) and (1 >= scalar >= 0):
        return True
    else:
        raise ValueError("Must be a real number between 0.0 and 1.0")

def validate_vectors(vector_list):
    """
    Return True if input is a list of valid vectors.
    """
    if isinstance(vector_list, list):
        if all([validate_vector(v=i) for i in vector_list]):
            return True
    else:
        raise ValueError("Vectors must be represented by a list of numeric values.")

def validate_matrix(matrix):
    """
    Return True if inputs are vectors of the same length
    """
    if validate_vectors(vector_list=matrix):
        if not len(matrix) > 0:
            raise ValueError("Input is not a list of lists.")
        a = len(matrix[0])
        if all(len(i) == a for i in matrix):
            return True
        else:
            raise AssertionError("Vectors are not the same length.")