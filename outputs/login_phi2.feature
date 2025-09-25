Feature: As a user, I want to be able to log in using my phone number and OTP verification so that I can access my account securely.
Acceptance Criteria:
- Given I am on the login page
  When I enter my phone number and OTP
  And I tap on the login button
  Then I should see a welcome message with my name
- Given I am on the login page
  When I enter an invalid phone number or OTP
  And I tap on the login button
  Then I should see an error message saying "Invalid credentials"
- Given I am on the login page
  When I tap on the forgot password link
  Then I should see a form to reset my password
- Given I am on the login page
  When I tap on the forgot password link
  And I enter a valid email address
