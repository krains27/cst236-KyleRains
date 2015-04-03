"""
:mod:`source.verify_shape` -- Determines if a shape is a
square or rectangle
========================================================

The following code determines if a set of 4 sides of a shape is a rectangle or a square
"""


def get_shape_type(angles=[], a=0, b=0, c=0, d=0):
    """
    Determine if the given shape is a rectangle or a square

    :param angles: The angles of the shape
    :type angles: list

    :param a: line a
    :type a: float or int or tuple or list or dict

    :param b: line b
    :type b: float or int

    :param c: line c
    :type c: float or int

    :param d: line d
    :type d: float or int

    :return: "square", "rectangle", "invalid", "disconnected", "rhombus"
    :type: str
    """
    shape_type = ''
    perp_angles = False

    if isinstance(a, (tuple, list)) and len(a) == 4:
        d = a[3]
        c = a[2]
        b = a[1]
        a = a[0]

    if isinstance(a, dict) and len(a.keys()) == 4:
        values = []
        for value in a.values():
            values.append(value)
        a = values[0]
        b = values[1]
        c = values[2]
        d = values[3]

    if not (isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float))):
        return "invalid"

    if a <= 0 or b <= 0 or c <= 0 or d <= 0:
        return "invalid"

    if a == b and b == c and c == d:
        shape_type = "square"

    elif a == c and b == d:
        shape_type = "rectangle"

    else:
        return "invalid"

    if angles:  # Are there angles to check?

        if isinstance(angles, (list, tuple)) and len(angles) == 4:

            angle_a = angles[0]
            angle_b = angles[1]
            angle_c = angles[2]
            angle_d = angles[3]

            if angle_a + angle_b == 180 and angle_c + angle_d == 180:
                perp_angles = True

            if shape_type == 'square':  # Rhombus fits square form
                if angle_a == angle_c and angle_b == angle_d and perp_angles:
                    shape_type = 'rhombus'
                else:
                    shape_type = 'disconnect'
            else:
                shape_type = 'disconnect'
        else:
            return 'invalid'

    return shape_type
