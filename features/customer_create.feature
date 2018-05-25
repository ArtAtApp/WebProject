Feature: Create an user of role artist
    In order to create a new user as an Artist
    As a new member of the application
    I want to create a new account

    Scenario: Create a new Customer
        Given I am in the sign up page
        When I'll fill all the fields correctly
            | role     | username   | password  | email       | dni       | firstname | lastname    | phonenumber | bank_account
            | Customer | user       | password  | def@def.com | 48004800C | Goldsberg | Shekelstein | 657282716   | 7856325962
        Then my user is created successfully
