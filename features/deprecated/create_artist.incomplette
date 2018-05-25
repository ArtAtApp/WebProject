Feature: Create a new Artist
    In order to create a new Artist
    As a new user
    I want to register as a new Artist

    Scenario: Create a new Artist user
        When I fill the fields:
            | role   | username   | password  | email       | dni       | firstname | lastname | phonenumber | bank_account
            | Artist | user       | password  | def@def.com | 48004800C | Default   | Artist   | 657282716   | 7856325962

        And I click on create user:

        Then I get redirected to my homepage
