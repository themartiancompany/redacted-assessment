# Discount Zone Optimization in E-Commerce

An e-commerce site has its own discount system
under which products can be placed in "discount zones".

Each zone has a particular discount percentage
over the total cost of products in that zone.

But there are tight rules to avoid misuse:

- Every product may appear in only one discount zone;
- Every zone should consist of between 2 and 4 products;
- The difference in total price between any two products
  in a zone should not be more than a limit `P`;
- The total percentage discount across all zones should
  not be more than a limit `M`;
- Products from the same category cannot be in the same
  zone (to promote variety).

Given a shopping cart of `N` items, every item
having a price, category, and highest discount allowed,
find the optimal method to put items into discount zones
so as to maximize total discount while all constraints
are respected.

# Function Specification

Implement this problem in Python by writing a
function `optimize_cart_discounts` which accepts
the following arguments:

- `N`: Items in cart (`2 ≤ N ≤ 100`);
- `P`: Maximum price difference threshold (`1 ≤ P ≤ 10000`);
- `M`: Maximum total discount percentage (`1 ≤ M ≤ 70`);
- `items`: List of N tuples, with each tuple including:
  - `price`: Item price (`1 ≤ price ≤ 5000`);
  - `category`: Item category ID (`1 ≤ category ≤ 20`);
  - `max_discount`: Maximum allowed discount
                    for this item (`1 ≤ max_discount ≤ 50`).

The method should return a list of lists,
with each inner list being the indices of items
in a discount zone.

The grouping should maximize the total discount
while fulfilling all constraints.

# Input Validation

If any of the following validations fail,
raise a `ValueError` with the message
"not valid input":

- Check `N`, `P`, and `M` are in valid ranges;
- Check items list contains exactly `N` entries;
- For every item, check:
  - Price is in valid range;
  - Category ID is valid;
  - Max discount is within limits;
  - Ensure at least one valid grouping is possible.

## Part 1: Strategy

What algorithm or strategy would you use to solve
this problem, and why is it the best fit given the constraints?

## Part 2: Test Case Instructions

Write 3 test cases:

a) Write a test case that should return a valid output;
b) Write a test case that should fail due to constraints;
c) Write a test case that should raise a `ValueError`.

## Part 3: Test Case Instructions

Write 3 test cases:

a) Write a test case that should return a valid output;
b) Write a test case that should fail due to constraints;
c) Write a test case that should raise a `ValueError`.
