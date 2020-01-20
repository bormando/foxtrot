Feature: Search

    Scenario Outline: Specific result found
        When open main page
        And search for <value>
        Then found <result>

        Examples:
        | value          | result                |
        | Schwarzenegger | Arnold Schwarzenegger |
