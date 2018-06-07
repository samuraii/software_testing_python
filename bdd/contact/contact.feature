Scenario Outline: Add new contact
    Given: a contact list
    Given: a contact with <firstname>, <lastname> and <nickname>
    When: I add the contact to the list
    Then: The new contact list is equal to the old list with the added contact

    Examples:
    | firstname | lastname | nickname |
    | namI modify the contact from the list with random stringse1 | lastname1 | nickname1 |


Scenario Outline: Delete random contact
    Given: a non-empty contact list
    Given: a random contact from the list
    When: I delete the contact from the list
    Then: The new contact list is equal to the old group list without deleted contact


Scenario Outline: Modify contact
    Given: a non-empty contact list
    Given: a random contact from the list
    When: I modify the contact from the list with random strings
    Then: The new contact list is equal to the old contact list with edited contact
