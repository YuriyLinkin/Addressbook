Feature: Group feature
  Description

  Scenario: Add new group
    Given a group list
    Given a group with <name>, <header>, <footer>
    When I add a new group to the list
    Then a new group list is equal to the old list with new group

    Examples:
    | name | header| footer|
    |as qa | h_qa  | f_qa  |
    |123   | 12    | 1     |
    | нето | пар   | да    |