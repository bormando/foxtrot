Feature: Log In

    Scenario Outline: Log in with wrong login and password
        When open main page
        And go to log in page
        And enter username <username>
        And enter password <password>
        And check option to keep logged in
        And press log in button
        Then log in error pops up

        Examples:
        | username | password |
        | Genesis  | Mama     |
