Feature: Modify Artwork
  In order to update my artworks
  As an artist
  I want to modify an artwork

  Background: There is a registered artist with 1 artwork
    Given Exists a registered artist "user" with password "password" with 1 artwork
    Then I log in with my credentials
    And I go to my artworks page

  Scenario: Modify an artwork
    Given an artwork
    | name        | artist        | date        | price        | image             | state        | art_type        |
    | KH          | user          | 12/5/2018   | 10           | /artworks/udl.png | 1            | Painting        |
    When I click on the button "modify"
    Then I get redirected to modify artwork page
    And I change it's name
    | name                   |
    | KingdomHearts          |
    And I got redirected to my artworks page
    And I check the artwork's name has been modified
