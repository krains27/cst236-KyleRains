"""
Test for source.source1
"""
from source.source1 import get_triangle_type
from unittest import TestCase

class TestGetTriangleType(TestCase):

    def test_get_triangle_equilateral_all_int(self):
        result = get_triangle_type(1, 1, 1)
        self.assertEqual(result, 'equilateral')

    def test_get_triangle_scalene_all_int(self):
        result = get_triangle_type(1, 2, 3)
        self.assertEqual(result, 'scalene')

    def test_get_triangle_invalid_a_neg(self):
        result = get_triangle_type(a=-1, b=1, c=1)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_invalid_b_neg(self):
        result = get_triangle_type(a=1, b=-1, c=1)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_invalid_c_neg(self):
        result = get_triangle_type(a=1, b=1, c=-1)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_invalid_a_char(self):
        result = get_triangle_type(a='a', b=1, c=1)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_invalid_b_char(self):
        result = get_triangle_type(a=1, b='b', c=1)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_invalid_c_char(self):
        result = get_triangle_type(a=1, b=1, c='c')
        self.assertEqual(result, 'invalid')

    def test_get_triangle_isosceles_all_int(self):
        result = get_triangle_type(a=1, b=1, c=2)
        self.assertEqual(result, 'isosceles')

    def test_get_triangle_equilateral_a_list(self):
        result = get_triangle_type(a=[1, 1, 1])
        self.assertEqual(result, 'equilateral')

    def test_get_triangle_equilateral_a_dict(self):
        tri_dict = {'a': 1, 'b': 1, 'c': 1}
        result = get_triangle_type(a=tri_dict)
        self.assertEqual(result, 'equilateral')