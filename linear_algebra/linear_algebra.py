# CHAPTER 4: LINEAR ALGEBRA



class LinearAlgebra():
    """
    A class of Linear Algebra operations on Vectors and Matrices.
    """

    def __init__(self, name, val_list):
        if self._validate_name_(name):
            self.name = name
        if self._validate_values_(val_list):
            self.values = val_list

    def set_name(self, name):
        """
        Set vector name
        """
        self.name = name

    def get_name(self):
        """
        Get vector name
        """
        return self.name

    def set_values(self, val_list):
        """
        Set vector values
        """
        self.values = val_list

    def get_values(self):
        """
        Get vector values
        """
        return self.values

    @staticmethod
    def _validate_name_(name):
        """
        Return True if input is a string
        """
        if isinstance(name, str):
            return True
        else:
            raise ValueError("Vector name must be a string.")

    @staticmethod
    def _validate_values_(val_list):
        """
        Return True if input is a list of numbers
        """
        if all([isinstance(i, (int, float)) for i in val_list]):
            return True
        else:
            raise ValueError("Vector values must be a list of numeric values.")

