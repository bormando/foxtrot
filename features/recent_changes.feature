Feature: Recent Changes

    Scenario Outline: Show selected number of changes
        When open main page
        And go to recent changes page
        And select <number> changes to show
        Then <number> changes shown

        Examples:
            | number |
            | 50     |
            | 100    |
