Feature: Setting a HDD size

Scenario: Setting HDD size to 100 GB
    Given a size
    When the size is 100
    Then the current hdd size should be 100