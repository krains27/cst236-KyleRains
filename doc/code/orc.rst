Orc
===

Orc provides functions for describing orcs that will be attacking. 

Orc Properties
^^^^^^^^^^^^^^

Once an orc is created, there are some properties that can be set to further define your orc.

Setting Orc Distance
^^^^^^^^^^^^^^^^^^^^
You can set the distance away from the kindom (0 is within perimeter)

>>> from source.orc import Orc
>>> test_orc = Orc()
>>> test_orc.distance = 15
>>> test_orc.distance
15

Setting Orc Velocity
^^^^^^^^^^^^^^^^^^^^
You can set the velocity of the orc which will describe how fast the orc is moving towards the kingdom.

>>> from source.orc import Orc
>>> test_orc = Orc()
>>> test_orc.velocity = 42
>>> test_orc.velocity
42

Setting Orc Priority
^^^^^^^^^^^^^^^^^^^^
You can set the priority of the orc, so defense will know how to attack first.

>>> from source.orc import Orc
>>> test_orc = Orc()
>>> test_orc.priority = 'HIGH'
>>> test_orc.priority
'HIGH'

Module Reference
^^^^^^^^^^^^^^^^

.. automodule:: source.orc
    :members: