Feature: As a user, I want to be able to log in using my phone number and OTP verification so that I can access my account securely.
Scenario: User logs in using phone number and OTP
  Given the user is on the login screen
  When the user enters a valid phone number and correct OTP
  Then the user should be logged in successfully and redirected to the home screen
    Given the user is on the login screen
    When the user enters a valid phone number
    And the user enters the correct OTP
    Then the user should be logged in successfully
    And redirected to the home screen
