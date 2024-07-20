Feature: Tests for target help page

  Scenario: Verify Target Help title
    Given  Open Target help page
    Then   Verify target help title


  Scenario Outline: Verify search help functionality
    Given   Open Target help page
    When    Text <question> in search bar
    Then    Verify search returns <relevant_result>
    Examples:
    |question          |relevant_result     |
    |return policy     |return policy       |
    |shipping          |shipping            |


 Scenario: Verify page displays correct number of help boxes
    Given   Open Target help page
    Then    Verify page displays 7 help boxes


 Scenario: Verify page shows correct number of info cells
    Given  Open Target help page
    Then   Verify page shows 3 info cells
