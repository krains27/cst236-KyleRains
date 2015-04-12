Feature: Calculating time difference

Scenario: Transfer is faster
    Given Seattle, 100 mb/sec and 100 GB of data (difference)
    When differnce between traveling to Seattle and transferring are calculated
    Then difference equals ~1.72 hours