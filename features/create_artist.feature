Feature: Create a new Artist
    In order to create a new user with role Artist
    As a new user
    I want to register a new Artist

    Scenario: Create a new user Artist
        Given I enter the fields:
            | username   | password | email       | dni       | firstname | lastname | phonenumber | bank_account  |
            | new_artist | 123pass  | def@def.com | 48484848K | Donald    | Trump    | 650202320   | 7894563211485 |
        And I click to create button

        Then I get redirected to my homepage
