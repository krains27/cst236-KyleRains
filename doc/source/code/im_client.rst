IM Client
=========

IM Client provides the functionality to allow a user to connect to another user and
send messages back and forth.

Starting the IM Client
^^^^^^^^^^^^^^^^^^^^^^
The IM Client will require a server IP address, a friend name to connect to, and the
username of the connecting user. Without these values, the connection will fail and log
an error to the screen.

Starting Client example
^^^^^^^^^^^^^^^^^^^^^^^
.. code::

    from source.FinalProject.im_client import IMClient
    test_client = IMClient()
    test_client.server_addr = '127.0.0.1'
    test_client.username = 'krains27'
    test_client.friend = 'friend'
    test_client.connect()  # Attempt to connect to the server
    test_client.stop()  # Attempt to close the connection to the server

Setting the properties
^^^^^^^^^^^^^^^^^^^^^^
There are a number of properties that can be set for the IMClient class. Some of the
properties provide verification before the value is set.

Property: friend_name
^^^^^^^^^^^^^^^^^^^^^

>>> from source.FinalProject.im_client import IMClient
>>> test_client = IMClient()
>>> test_client.friend_name = 4.5  # Not string, will fail
>>> test_client.friend_name

>>> test_client.friend_name = 'This name will be too long for sure'  # Too long, will fail
>>> test_client.friend_name

>>> test_client.friend_name = 'friend'  # Valid
>>> test_client.friend_name
'friend'

Property: server_addr
^^^^^^^^^^^^^^^^^^^^^

>>> from source.FinalProject.im_client import IMClient
>>> test_client = IMClient()
>>> test_client.server_addr = 4.5  # Not string, will fail
>>> test_client.server_addr

>>> test_client.server_addr = 'localhost'  # Improper format, will fail
>>> test_client.server_addr

>>> test_client.server_addr = '127.0.0.1'  # Valid
>>> test_client.server_addr
'127.0.0.1'

Property: username
^^^^^^^^^^^^^^^^^^

>>> from source.FinalProject.im_client import IMClient
>>> test_client = IMClient()
>>> test_client.username = 4.5  # Not string, will fail
>>> test_client.username

>>> test_client.username = 'This name will be too long for sure'  # Too long, will fail
>>> test_client.username

>>> test_client.username = 'krains27'  # Valid
>>> test_client.username
'krains27'


Module Reference
^^^^^^^^^^^^^^^^

.. automodule:: source.FinalProject.im_client
    :members: