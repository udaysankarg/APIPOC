@APITest
Feature: Validate the API responses according to the Acceptance Criteria

Background: Set base url and headers
    Given I set base URL to "context.base_url"

@smoke
Scenario: To validate the status code and status message
    When I make a "GET" request to "/Categories/6327/Details.json?catalogue=false"
    Then the response status code should equal "200"
    And the response status message should equal "OK"

