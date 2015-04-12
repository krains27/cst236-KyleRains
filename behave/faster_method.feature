Feature: Calculating faster method

Scenario: Transfer is faster
    Given Seattle, 100 mb/sec and 100 GB of data
    When time between traveling to Seattle and transferring are calculated
    Then transferring is faster

Scenario: Driving is faster
    Given Salem, 50 mb/sec and 500 GB of data
    When time between traveling to Salem and transferring are calculated
    Then driving is faster