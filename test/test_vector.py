import unittest
from linear_algebra.vectors import Vector

NAME1 = 'test_vector'
NAME2 = 'renamed_vector'
VALS1 = [1, 2, 3.5, 4.]
VALS2 = [4, 3.5, 2, 1.]

class Test_Polygon(unittest.TestCase):

    def setUp(self):
        self.vector = Vector(name=NAME1, val_list=VALS1)

    def test_set_name(self):
        """Test set_name method."""
        self.vector.set_name(name=NAME2)
        self.assertTrue(self.vector.name == NAME2)

    def test_get_name(self):
        """Test get_name method."""
        self.assertTrue(self.vector.get_name() == NAME1)

    def test_set_values(self):
        """Test set_values method."""
        self.vector.set_values(val_list=VALS2)
        self.assertListEqual(self.vector.values, VALS2)

    def test_get_values(self):
        """Test get_values method."""
        self.assertListEqual(self.vector.get_values(), VALS1)

    def test_validate_name_(self):
        """Test _validate_name_ method."""
        self.assertTrue(self.vector._validate_name_(NAME1))
        with self.assertRaises(ValueError):
            self.vector._validate_name_(VALS1)
            self.vector._validate_name_(1)
            self.vector._validate_name_(1.234)
            self.vector._validate_name_(None)

    def test_validate_values_(self):
        """Test _validate_values_ method."""
        self.assertTrue(self.vector._validate_values_(VALS2))
        with self.assertRaises(ValueError):
            self.vector._validate_values_(NAME1)
            self.vector._validate_values_(['2'])
            self.vector._validate_values_(1.234)
            self.vector._validate_values_(1)
            self.vector._validate_values_([])
            self.vector._validate_values_(None)
