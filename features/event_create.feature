Feature: Create Event
  In order to create an event
  As an organizer
  I want to create an event

  Background: There is a registered user
    Given Exists an organizer "user1" with password "password" and role "Organizer"
    Then I do the login

  Scenario: Create an event
    Given I'm logged as user "user1" with password "password"
    When I post events
      | name        | ini_date        | end_date        | Type       | created_by |
      | KH          | 12/5/2018       | 12/6/2018       | Painting   | user1      |
    Then I get redirected to create event
