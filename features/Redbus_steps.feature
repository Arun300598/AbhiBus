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
        | Chennai | Trichy | Parveen Travels | 560 |
        | Chennai | Bangalore | IntrCity SmartBus | 1375 |


