# Created by willsterling at 2/11/23
Feature: CureSkin search tests

  Scenario: User can search for a product on CureSkin app
    Given Open shop_cureskin main page
    When Close popup window
    When Click search icon
    When Input text into main-search-bar CureSkin gel
    Then Verify search results are showing 2 elements

  Scenario: User can search for a product on CureSkin app in mobile
    Given Open shop_cureskin main page
    When Close popup window
    When Click search icon
    When Input text into main-search-bar CureSkin gel
    Then Verify search results are showing 2 elements
