Feature: Target main page search tests

  Scenario: User can search for a product on target
    Given  Open Target main page
    When   Search for product
    Then   Verify search worked

  Scenario: User can see message by clicking on the cart icon
     Given Open Target main page
     When  Click on Cart icon
     Then  Verify Your cart is empty message is shown

  Scenario: A logged out user can navigate to Sign In
     Given Open Target main page
     When   Click on Sign In
     When   From right side navigation menu click Sign In
     Then   Verify Sign In form opened




