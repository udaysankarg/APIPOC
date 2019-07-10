@APITest
Feature: Validate the details of "Carbon credits" farming industry from the API response
    For CategoryId:6327, Name should be Carbon credits
    CanRelist should be True and Gallery Promotion should have 2x larger image in the Description

Background: Setting base url
    Given I set base URL to "context.base_url"

@smoke
Scenario Outline: To validate the status code and status message
    When I make a "GET" request to "/Categories/<CategoryID>/Details.json?catalogue=false"
    Then the response status code should equal "<ResponseCode>"
    And the response status message should equal "<Status_msg>"

    Examples: Response code check @<CategoryID>
    |CategoryID|ResponseCode|Status_msg |
    |6327      |200         |OK         |
    |1234      |400         |Bad Request|

@Test
Scenario Outline: To validate the status code with different input parameters
    When I make a "GET" request to "/Categories/6327/Details.json" with <param>
    Then the response status code should equal "<ResponseCode>"
    And the response status message should equal "<Status_msg>"

    Examples: Response code check
    |param                  |ResponseCode|Status_msg |
    |{"catalogue":False }   |200         |OK         |
    |{"catalogue":True }    |200         |OK         |
    |{"catalogue":None }    |200         |OK         |

@Test @CarbonCredits @AC
Scenario: To validate whether details of Carbon credits under Business-farming-industry
    When I make a "GET" request to "/Categories/6327/Details.json?catalogue=false"
    Then the response status code should equal "200"
    And value at jsonpath ".CategoryId" in response should be "6327"
    And value at jsonpath ".Name" in response should be "Carbon credits"
    And value at jsonpath ".CanRelist" in response should be "True"
    And value at jsonpath ".Promotions(Name="Gallery").Description" in response should contain "2x larger image"

@Test @Promotion
Scenario Outline: To validate the Farming Industry Promotions Name and its Description
    When I make a "GET" request to "/Categories/<Category ID>/Details.json?catalogue=false"
    Then the response status code should equal "200"
    And value at jsonpath ".CategoryId" in response should be "<Category ID>"
    And value at jsonpath ".Name" in response should be "<Name>"
    And value at jsonpath ".Promotions(Name="<Promotion_Name>").Description" in response should contain "<Description>"

    Examples: Promotion Name @<Promotion_Name>
    | Category ID| Name           | Promotion_Name | Description                |
    | 6327       | Carbon credits |  Basic         |Lowest position in category |
    | 6327       | Carbon credits |  Gallery       |2x larger image             |
    | 6327       | Carbon credits |  Feature       |4x larger image             |
    | 6327       | Carbon credits |  Feature Combo |Includes benefits of Feature|