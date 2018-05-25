Feature: Delete an artwork
    In order to delete an artwork
    As an artist
    I want to delete an artwork that I have created

    Background: There is a registered artist
      Given Exists a registered organizer "user" with password "password" with 1 artwork created
      Then I log in as an artist.
      And I go to my artwork page

    Scenario: Delete an artwork
      Given 1 artwork
      Then I click on the delete button of the artwork
      And there aren't more artwork
