@APITest
Feature: Validate the API responses according to the Acceptance Criteria

Background: Set base url and headers
    Given I set base URL to "context.base_url"

@smoke
Scenario: To validate the status code and status message
    When I make a "GET" request to "/Categories/6327/Details.json?catalogue=false"
    Then the response status code should equal "200"
    And the response status message should equal "OK"

Scenario: To validate whether Carbon credits is present in response
    When I make a "GET" request to "/Categories/6327/Details.json?catalogue=false"
    Then the response status code should equal "200"
    And value at jsonpath ".Name" in response should be "Carbon credits"

Scenario: To validate whether CanRelist is true
    When I make a "GET" request to "/Categories/6327/Details.json?catalogue=false"
    Then the response status code should equal "200"
    And value at jsonpath ".CanRelist" in response should be "True"


Scenario: To validate whether CanRelist is true
    When I make a "GET" request to "/Categories/6327/Details.json?catalogue=false"
    Then the response status code should equal "200"
    And value at jsonpath ".Promotions(Name="Gallery").Description" in response should contain "2x larger image"
