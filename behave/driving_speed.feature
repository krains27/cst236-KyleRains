Feature: Selecting a preset driving speed

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