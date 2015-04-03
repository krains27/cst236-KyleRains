"""
Test for source.verify_shape
"""
from source.verify_shape import get_shape_type
from unittest import TestCase

class TestGetShapeType(TestCase):

    def test_get_shape_square_all_int(self):
        result = get_shape_type(a=1, b=1, c=1, d=1)
        self.assertEqual(result, 'square')

    def test_get_shape_rect_all_int(self):
        result = get_shape_type(a=1, b=2, c=1, d=2)
        self.assertEqual(result, 'rectangle')

    def test_get_shape_invalid_a_neg(self):
        result = get_shape_type(a=-1, b=1, c=1, d=1)
        self.assertEqual(result, 'invalid')

    def test_get_shape_invalid_b_neg(self):
        result = get_shape_type(a=1, b=-1, c=1, d=1)
        self.assertEqual(result, 'invalid')

    def test_get_shape_invalid_c_neg(self):
        result = get_shape_type(a=1, b=1, c=-1, d=1)
        self.assertEqual(result, 'invalid')

    def test_get_shape_invalid_d_neg(self):
        result = get_shape_type(a=1, b=1, c=1, d=-1)
        self.assertEqual(result, 'invalid')

    def test_get_shape_invalid_all_int(self):
        result = get_shape_type(a=1, b=2, c=3, d=4)
        self.assertEqual(result, 'invalid')

    def test_get_shape_invalid_a_char(self):
        result = get_shape_type(a='a', b=1, c=1, d=1)
        self.assertEqual(result, 'invalid')

    def test_get_shape_invalid_b_char(self):
        result = get_shape_type(a=1, b='b', c=1, d=1)
        self.assertEqual(result, 'invalid')

    def test_get_shape_invalid_c_char(self):
        result = get_shape_type(a=1, b=1, c='c', d=1)
        self.assertEqual(result, 'invalid')

    def test_get_shape_invalid_d_char(self):
        result = get_shape_type(a=1, b=1, c=1, d='d')
        self.assertEqual(result, 'invalid')

    def test_get_shape_square_a_list(self):
        result = get_shape_type(a=[1, 1, 1, 1])
        self.assertEqual(result, 'square')

    def test_get_shape_square_a_dict(self):
        shape_dict = {'a': 1, 'b': 1, 'c': 1, 'd': 1}
        result = get_shape_type(a=shape_dict)
        self.assertEqual(result, 'square')

    def test_get_shape_rhombus_all_int(self):
        result = get_shape_type(angles=(106, 74, 106, 74), a=1, b=1, c=1, d=1)
        self.assertEqual(result, 'rhombus')

    def test_get_shape_disconnect_angles_all_int(self):
        result = get_shape_type(angles=(110, 74, 110, 74), a=1, b=1, c=1, d=1)
        self.assertEqual(result, 'disconnect')

    def test_get_shape_disconnect_sides_all_int(self):
        result = get_shape_type(angles=(106, 74, 106, 74), a=1, b=2, c=1, d=2)
        self.assertEqual(result, 'disconnect')

    def test_get_shape_invalid_less_angles(self):
        result = get_shape_type(angles=(106, 74, 106), a=1, b=2, c=1, d=2)
        self.assertEqual(result, 'invalid')