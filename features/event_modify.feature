Feature: Modify Event
  In order to update my events
  As an organizer
  I want to modify an event

  Background: There is a registered organizer with 1 event
    Given Exists a registered organizer "usero" with password "password" with 1 event
    Then I log in as an organizer
    And I go to my events detail page

  Scenario: Modify an event
    Given an event
    | name        | created_by        | ini_date        | end_date        | type             |
    | KH          | usero             | 12/5/2018       | 12/6/2018       | Painting         |
    When I click on the button "modify" of the event
    Then I get redirected to modify event page
    And I change it's name to
    | name                   |
    | KingdomHearts          |
    And I got redirected to my events page
    And I check the event's name has been modified
