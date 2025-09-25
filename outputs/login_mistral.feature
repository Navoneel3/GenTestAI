Feature: As a user, I want to be able to log in using my phone number and OTP verification so that I can access my account securely.
Scenario: As a user, I want to be able to log in using my phone number and OTP verification so that I can access my account securely.

Given I am on the login page
When I enter my phone number and click on the "Send OTP" button
Then I should receive an OTP on my phone
And I should be able to enter the OTP on the login page
And I should be able to log in successfully

Acceptance Criteria:

* The user should be able to enter their phone number on the login page
* The user should be able to click on the "Send OTP" button to receive an OTP on their phone
* The user should be able to enter the OTP on the login page
* The user should be able to log in successfully with the entered phone number and OTP
* The user should not be able to log in without entering a valid phone number and OTP
