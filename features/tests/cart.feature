Feature: Cart tests

  Scenario: User can see Cart Empty message
    Given Open target main page
    When Click on cart icon
    Then Verify Cart Empty message shown

    Scenario: User can add a product to the cart
      Given Open target main page
      When Search for a product "laptop"
      And Select the first product from search results
      And  Add the product to the cart
      And Click on the cart icon
      Then Verify the product is in the cart
