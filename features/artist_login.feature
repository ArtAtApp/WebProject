Feature: Log in
    In order to log in successfully as an Artist
    As an already registered Artist
    I want to log in

    Background: There is a registered user
        Given Exists a user "user" with password "password"

    Scenario: Log in
        Given I am in the login page
        Given I login as user "user" with password "password"
        When I log in
          | username | password |
          | user     | password |
        Then I get redirected to the homepage
