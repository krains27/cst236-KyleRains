Kingdom
=======

Kingdom provides functions for describing the kingdom to defend. 

Adding an orc
^^^^^^^^^^^^^

The function :func:`source.kingdom.add_orc` allows a user to add a list of orcs to the list of attacking orcs. 

Adding Orc Example
^^^^^^^^^^^^^^^^^^

>>> from source.kingdom import Kingdom
>>> from source.orc import Orc
>>> test_kingdom = Kingdom()
>>> test_orc = Orc()
>>> test_kingdom.add_orc([test_orc])
>>> len(test_kingdom.orcs)
1

Clearing the orcs
^^^^^^^^^^^^^^^^^

The function :func:`source.kingdom.clear_orcs` allows a user to clear all the orcs that are currently attacking. 

Clearing Orcs Example
^^^^^^^^^^^^^^^^^^^^^

>>> from source.kingdom import Kingdom
>>> from source.orc import Orc
>>> test_kingdom = Kingdom()
>>> test_orc = Orc()
>>> test_kingdom.add_orc([test_orc])
>>> len(test_kingdom.orcs)
1
>>> test_kingdom.clear_orcs()
>>> len(test_kingdom.orcs)
0

Removing an Orc
^^^^^^^^^^^^^^^

The function :func:`source.kingdom.remove_orc` allows a user to remove a specific orc from the list
of attacking orcs. 

Removing Orc Example
^^^^^^^^^^^^^^^^^^^^

>>> from source.kingdom import Kingdom
>>> from source.orc import Orc
>>> test_kingdom = Kingdom()
>>> test_orc = Orc()
>>> test_kingdom.add_orc([test_orc])
>>> len(test_kingdom.orcs)
1
>>> test_kingdom.remove_orc(test_orc)
>>> len(test_kingdom.orcs)
0

Module Reference
^^^^^^^^^^^^^^^^

.. automodule:: source.kingdom
    :members: