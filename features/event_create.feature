Feature: Create Event
  In order to create an event
  As an organizer
  I want to create an event

  Background: There is a registered user
    Given Exists an artist "user1" with password "password" and role "Organizer"

  Scenario: Create an event
    Given I'm loged as user "user1" with password "password"
    When I post events
      | name        | ini_date        | end_date        | Type       | created_by |
      | KH          | 12/5/2018       | 12/6/2018       | Painting   | user1      |
    Then I'm viewing the details page for events by "user1"
      | name        |
      | KH          |
    And There are 1 events
