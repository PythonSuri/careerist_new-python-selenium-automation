Feature: Tests for target Help page

  Scenario: Verify Target Help title
    Given   Open Target help page
    Then    Verify target help title


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


  Scenario: User can select Help topic Promotions & Coupons
    Given   Open Help page for Returns
    Then    Verify help Returns page opened
    When    Select Help topic Promotions & Coupons
    Then    Verify help Current promotions page opened

  Scenario: User can select Help topic Target Circle
    Given   Open Help page for Returns
    Then    Verify help Returns page opened
    When    Select Help topic Target Circle™
    Then    Verify help About Target Circle page opened

  Scenario: User can select Help topic Target Circle
    Given   Open Help page for Returns
    Then    Verify help Returns page opened
    When    Select Help topic Delivery & Pickup
    Then    Verify help Drive Up & Order Pickup page opened