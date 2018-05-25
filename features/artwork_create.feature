Feature: Create Artwork
  In order to show my artworks
  As an artist
  I want to post an artwork

  Background: There is a registered user
    Given Exists a registered artist "user" with password "password" and role "Artist"
    Then I log in
    And I go to the create artwork page

  Scenario: Post an artwork
    When I post artwork
      | name        | artist        | date        | price        | image             | state        | art_type        |
      | KH          | user          | 12/5/2018   | 10           | /artworks/udl.png | 1            | Painting        |
    Then I'm viewing the details page for artworks by "user"
      | name        |
      | KH  |
    And There are 1 artworks
