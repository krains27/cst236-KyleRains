Feature: Hard Drive Speed

Scenario: Account for hard drive speed
    Given a hard drive speed
    When transfer time is calculated (hdd)
    Then the calculation will account for the hard drive speed