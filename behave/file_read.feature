Feature: Reading cities, distances and connection speeds from a file

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
