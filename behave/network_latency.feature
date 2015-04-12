Feature: Network Latency

Scenario: Account for network latency
    Given a latency
    When transfer time is calculated
    Then the calculation will account for the latency