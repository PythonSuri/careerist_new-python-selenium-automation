Feature: Tests for main page UI

  @smoke
  Scenario: Verify header in shown
    Given  Open Target main page
    Then   Verify header in shown

  @smoke
  Scenario: Verify header has correct amount links
    Given  Open Target main page
    Then   Verify header has 6 links

