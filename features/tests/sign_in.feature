Feature: Tests for Sign In functionality

  Scenario: A logged out user can navigate to Sign In
     Given  Open Target main page
     When   Click on Sign In
     When   From right side navigation menu click Sign In
     Then   Verify Sign In form opened