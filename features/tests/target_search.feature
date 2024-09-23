Feature: Tests for Target Search functionality

  Scenario: User can search for a coffee
    Given Open target main page
    When Search for a coffee
    Then Verify that correct search results shown

  Scenario: User can search for a tea
    Given Open target main page
    When Search for a tea
    Then Verify that correct search results shown

