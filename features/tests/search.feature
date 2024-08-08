Feature: Target main page search tests

  Scenario: User can search for coffee
    Given  Open Target main page
    When   Search for coffee
    Then   Verify search results shown for coffee
    Then   Verify correct search results URL opens for coffee


  Scenario: User can search for chair
    Given  Open Target main page
    When   Search for chair
    Then   Verify search results shown for chair
    Then   Verify correct search results URL opens for chair

  Scenario: User can search for ipad
    Given  Open Target main page
    When   Search for ipad
    Then   Verify search results shown for ipad
    Then   Verify correct search results URL opens for ipad


  Scenario Outline: User can search for a product
    Given  Open Target main page
    When   Search for <product>
    Then   Verify search results shown for <expected_result>
    Then   Verify correct search results URL opens for <expected_result>
    Examples:
    |product    |expected_result     |
    |coffee     |coffee              |
    |candle     |candle              |
    |ipad       |ipad                |


  Scenario: User can add a product to cart
    Given   Open target main page
    When    Search for tea
    And     Click on Add to Cart button
    And     Store product name
    And     Confirm Add to Cart button from side navigation
    And     Open cart page
    Then    Verify cart contains 1 item(s)


  Scenario: Verify that user can see product names and images
    Given   Open target main page
    When    Search for PlayStation
    Then    Verify that every product has a name and an image


  Scenario: User can see favorites tooltip for search results
    Given   Open target main page
    When    Search for tea
    And     Hover favorites icon
    Then    Favorites tooltip is shown