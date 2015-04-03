Verify Shape
=============

Verify Shape provides functions for describing a four sided shape.

Determining Shape Type
^^^^^^^^^^^^^^^^^^^^^^

The function :func:`source.verify_shape.get_shape_type` allows users to enter four sides 
that correspond to the sides of the shape. A user can also add a list of four angles to
determine if the shape is a rhombus or disconnected. The function will return 
"square", "rectangle", or "invalid" if angles are not included. The function will return "rhombus",
"disconnected", or "invalid" if the angles are included. 

Square Example
^^^^^^^^^^^^^^

>>> from source.verify_shape import get_shape_type
>>> get_shape_type(a=1, b=1, c=1, d=1)
'square'

Rectangle Example
^^^^^^^^^^^^^^^^^

.. testsetup:: *

    from source.verify_shape import get_shape_type
    rect_list = [1,2,1,2]
    
.. testcode:: rectangle

    get_shape_type(a=rect_list)

.. testoutput::

    'rectangle'


Module Reference
^^^^^^^^^^^^^^^^

.. automodule:: source.verify_shape
    :members: