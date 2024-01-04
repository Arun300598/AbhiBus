Feature: RedBus
  Scenario: Verify the title
    Given Launch the chrome Browser
    When Open Abhibus page
    Then Verify the title of webpage
    And close the browser

  Scenario Outline: Verify the bus price
    Given Launch the chrome Browser
    When Open Abhibus page
    And Enter from "<From>" and To "<To>"
    And click today button and click search
    And search for bus name "<Busname>"
    Then verify the bus fare as "<Busfare>"
    And close the browser


    Examples:
      | From | To | Busname | Busfare |
      | Chennai | Trichy | Parveen Travels | 620 |
      | Chennai | Bangalore | IntrCity SmartBus | 912 |



  Scenario Outline: Verify Bus is listed
    Given Launch the chrome Browser
    When Open Abhibus page
    And Enter from "<From>" and To "<To>"
    And click today button and click search
    Then Verify Bus name "<Busname>" is present

    Examples:
      | From    | To        | Busname           |
      | Chennai | Trichy    | Parveen Travels   |
      | Chennai | Bangalore | IntrCity SmartBus |

  @Filter
  Scenario Outline: Verify Non AC buses are listed for Non AC filter and AC buses are listed for AC filter
    Given Launch the chrome Browser
    When Open Abhibus page
    And Enter from "<From>" and To "<To>"
    And click today button and click search
    And click on filter "<Filter>"
    Then Verify buses listed are as per the filter "<Filter>"

    Examples:
      | From    | To        | Filter |
      | Chennai | Bangalore | Non-AC |
      | Chennai | Bangalore | AC |






