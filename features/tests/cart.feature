Feature: Tests for Cart Functionality

  Scenario: User can see message by clicking on the cart icon
     Given Open Target main page
     When  Click on Cart icon
     Then  Verify Your cart is empty message is shown

