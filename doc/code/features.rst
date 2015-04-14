System Features
===============

Feature: Selecting a preset driving speed
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Scenario: Selecting Porsche preset
    Given Porsche preset speed equals 100
    When Porsche preset selected
    Then driving speed will be 100

Scenario: Selecting Bus preset
    Given Bus preset speed equals 65
    When Bus preset selected
    Then driving speed will be 65

Scenario: Selecting Cement Truck preset
    Given Cement Truck preset speed equals 55
    When Cement Truck preset selected
    Then driving speed will be 55

Scenario: Selecting Swallow preset
    Given Swallow preset speed equals 10
    When Swallow preset selected
    Then driving speed will be 10

Feature: Selecting an estimate speed
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Scenario: Selecting an estimated speed of 50
    Given an estimated speed
    When estimated speed is selected
    Then estimated speed will be used in calculation

Feature: Calculating faster method
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Scenario: Transfer is faster
    Given Seattle, 100 mb/sec and 100 GB of data
    When time between traveling to Seattle and transferring are calculated
    Then transferring is faster

Scenario: Driving is faster
    Given Salem, 50 mb/sec and 500 GB of data
    When time between traveling to Salem and transferring are calculated
    Then driving is faster

Feature: Reading cities, distances and connection speeds from a file
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Scenario: Reading cities from a file
    Given a city text file
    When the cities are read
    Then my app should contain the cities read

Scenario: Reading distances from a file
    Given a distance text file
    When the distances are read
    Then my app should contain the distances read

Scenario: Reading speeds from a file
    Given a speed text file
    When the speeds are read
    Then my app should contain the speeds read


Feature: Setting a HDD size
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Scenario: Setting HDD size to 100 GB
    Given a size
    When the size is 100
    Then the current hdd size should be 100

Feature: Hard Drive Speed
^^^^^^^^^^^^^^^^^^^^^^^^^

Scenario: Account for hard drive speed
    Given a hard drive speed
    When transfer time is calculated (hdd)
    Then the calculation will account for the hard drive speed

Feature: Network Latency
^^^^^^^^^^^^^^^^^^^^^^^^

Scenario: Account for network latency
    Given a latency
    When transfer time is calculated
    Then the calculation will account for the latency

Feature: New city
^^^^^^^^^^^^^^^^^

Scenario: Creating a new city
    Given city not in list of cities
    When city is entered
    Then city will be added to list of cities

Scenario: Adding city to city file
    Given city not in list of cities (file)
    When city is entered (file)
    Then city will be written to city file

Feature: Enter Route
^^^^^^^^^^^^^^^^^^^^

Scenario: Enter a route of 10 cities
    Given 10 different cities
    When cities are added to route
    Then cities will be saved in route

Feature: Enter starting city
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Scenario: Enter starting city
    Given a city
    When starting city is set to city
    Then starting city will be given city

Feature: Calculating time difference
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Scenario: Transfer is faster
    Given Seattle, 100 mb/sec and 100 GB of data (difference)
    When differnce between traveling to Seattle and transferring are calculated
    Then difference equals ~1.72 hours

