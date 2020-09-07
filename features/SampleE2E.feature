Feature: Example feature for E2E flow

  Scenario: This is a login example scenario
    Given The user is on the Home Page
    When The user requests for login with username "testuser@yopmail.com" and password "123456"
    Then The user should see the Welcome Page