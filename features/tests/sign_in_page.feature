Feature: Tests for Sign In functionality

  Scenario: A logged out user can navigate to Sign In
     Given  Open Target main page
     When   Click on Sign In
     When   From right side navigation menu click Sign In
     Then   Verify Sign In form opened


  Scenario: User can open and close Terms and Conditions from sign in page
     Given  Open Target main page
     When   Click on Sign In
     When   From right side navigation menu click Sign In
     When   Store original window
     And    Click on Target terms and conditions link
     And    Switch to the newly opened window
     Then   Verify Terms and Conditions page is opened
     And    Close a new window and switch back to original