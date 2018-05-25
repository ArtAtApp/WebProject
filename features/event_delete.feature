Feature: Delete an event
    In order to solve my mistakes
    As an organizer
    I want to delete an event that I have created

    Background: There is a registered organizer
      Given Exists a registered organizer "orga" with password "password" and role "Organizer" with 1 event created
      Then I log in.
      And I go to my events page

    Scenario: Delete an event
      Given 1 event
      Then I click on the delete button
      And there aren't more events
