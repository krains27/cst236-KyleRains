IM Server
=========

IM Server provides functionality that routes messages from two connected user to each
other.

Starting the IM Server
^^^^^^^^^^^^^^^^^^^^^^
The IM server will need to be started before a user attempts to start an IM Client.
The IM Client will not be able to connect with another user without the server.

Starting Server example
^^^^^^^^^^^^^^^^^^^^^^^
.. code::

    from source.FinalProject.im_server import IMServer
    test_server = IMServer(addr='127.0.0.1')
    test_server.start()  # This will allow the server to start listening
    test_server.stop()  # This will allow the server to stop any active connections

The start() function
^^^^^^^^^^^^^^^^^^^^
The start function is a blocking function. This means that it will return from this function
until two users have been connected. So, the stop function can't be called unless two
users are actively engaged in a connection.

Module Reference
^^^^^^^^^^^^^^^^

.. automodule:: source.FinalProject.im_server
    :members: