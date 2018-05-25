Feature: Create Artwork
  In order to show my artworks
  As an artist
  I want to add an artwork to an event

  Background: There is a registered user
    Given Exists a registered artist "artiste" with password "password" with 1 artwork
    Then I log in as an artist

  Scenario: Add an artwork to an event
    When I'm in the current events page
    And there's 1 event
    And I enter in
    And there are not any artworks
    Then I go back to current events
    And I select add artwork to an event
      | name        | created_by        | ini_date        | end_date        | type             |
      | KH          | usero             | 12/5/2018       | 12/6/2018       | Painting         |
    Then I select one of my artworks of the same type as the event
      | name        | artist        | date        | price        | image             | state        | art_type        |
      | KH          | user          | 12/5/2018   | 10           | /artworks/udl.png | 1            | Painting        |
    And There are 1 artworks
