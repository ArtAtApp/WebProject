
Feature: Log in
    In order to log in successfully as an Artist
    As an already registered Artist
    I want to log in

    Background: There is a registered user
        Given Exists a user "default_artist" with password "123pass"

    Scenario: Log in
        Given I login as user "user" with password "password"
        When I log in
          | username       | password |
          | default_artist | 123pass  |
        Then I get redirected to the homepage
