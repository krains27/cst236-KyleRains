Feature: New city

Scenario: Creating a new city
    Given city not in list of cities
    When city is entered
    Then city will be added to list of cities

Scenario: Adding city to city file
    Given city not in list of cities (file)
    When city is entered (file)
    Then city will be written to city file