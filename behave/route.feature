Feature: Enter Route

Scenario: Enter a route of 10 cities
    Given 10 different cities
    When cities are added to route
    Then cities will be saved in route