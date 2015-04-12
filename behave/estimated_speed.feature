Feature: Selecting an estimate speed

Scenario: Selecting an estimated speed of 50
    Given an estimated speed
    When estimated speed is selected
    Then estimated speed will be used in calculation