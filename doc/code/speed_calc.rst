Speed Calculator
================

Speed Calculator provides functions for determining whether it's quicker to 
drive a hard drive or transfer over network.

Adding a Cities to a route
^^^^^^^^^^^^^^^^^^^^^^^^^^

The function :func:`source.speed_calculator.add_to_route` allows a user to add a city to the current route. 

Adding City to route Example
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

>>> from source.speed_calculator import SpeedCalculator
>>> test_calc = SpeedCalculator()
>>> test_calc.add_to_route('Portland')
>>> test_calc.add_to_route('Seattle')
>>> len(test_calc.route)
2

Calculate Driving Time
^^^^^^^^^^^^^^^^^^^^^^

The function :func:`source.speed_calculator.calculate_driving_time` allows a user to calculate how long it would take to drive to
a specific city with a hard drive.
    

Calculate Transfer Time
^^^^^^^^^^^^^^^^^^^^^^^

The function :func:`source.speed_calculator.calculate_transfer_time` allows a user to calculate how long it would take to transfer 
data across the network.

Determine Faster Method
^^^^^^^^^^^^^^^^^^^^^^^

The function :func:`source.speed_calculator.determine_faster_method` allows a user to calculate which is faster, driving a hard
drive or transferring data across the network. 

Determine Time Difference
^^^^^^^^^^^^^^^^^^^^^^^^^

The function :func:`source.speed_calculator.determine_time_difference` allows a user to calculate the difference in time between
driving a hard drive or transferring data across network. 

Reading a File
^^^^^^^^^^^^^^

The function :func:`source.speed_calculator.read_file` allows a user to pass a file handle into the program. This file can hold
either cities, transfer speeds, or distances. 

Class Properties
^^^^^^^^^^^^^^^^

The SpeedCalculator class has a number of properties available to allow a user to change the values used for the calculations. 

City Property Example
^^^^^^^^^^^^^^^^^^^^^

>>> from source.speed_calculator import SpeedCalculator
>>> test_calc = SpeedCalculator()
>>> test_calc.city = 'Portland'
>>> test_calc.city
'Portland'

Hard Drive Speed Property Example
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

>>> from source.speed_calculator import SpeedCalculator
>>> test_calc = SpeedCalculator()
>>> test_calc.drive_speed = 52
>>> test_calc.drive_speed
52

Network Latency Property Example
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

>>> from source.speed_calculator import SpeedCalculator
>>> test_calc = SpeedCalculator()
>>> test_calc.latency = 300
>>> test_calc.latency
300

Starting City Property Example
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

>>> from source.speed_calculator import SpeedCalculator
>>> test_calc = SpeedCalculator()
>>> test_calc.starting_city = 'Keizer'
>>> test_calc.starting_city
'Keizer'

Network Transfer Speed Property Example
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

>>> from source.speed_calculator import SpeedCalculator
>>> test_calc = SpeedCalculator()
>>> test_calc.transfer_speed = 50
>>> test_calc.transfer_speed
50

Hard Drive Size Property Example
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

>>> from source.speed_calculator import SpeedCalculator
>>> test_calc = SpeedCalculator()
>>> test_calc.hdd_size = 500
>>> test_calc.hdd_size
500

Module Reference
^^^^^^^^^^^^^^^^

.. automodule:: source.speed_calculator
    :members: