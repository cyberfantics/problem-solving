# Lemonade Change

## Problem Statement

At a lemonade stand, each lemonade costs $5. Customers are standing in a queue to buy from you and order one at a time (in the order specified by the array `bills`). Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill. You must provide the correct change to each customer so that the net transaction is that the customer pays $5.

Note that you do not have any change in hand at first.

Given an integer array `bills` where `bills[i]` is the bill the `i-th` customer pays, return `true` if you can provide every customer with the correct change, or `false` otherwise.

## Examples

### Example 1:
**Input:** 
```python
bills = [5, 5, 5, 10, 20]
```
**Output:** 
```python
true
```
**Explanation:**
- From the first 3 customers, we collect three $5 bills in order.
- From the fourth customer, we collect a $10 bill and give back a $5 bill.
- From the fifth customer, we give a $10 bill and a $5 bill.
- Since all customers received the correct change, the output is `true`.

### Example 2:
**Input:** 
```python
bills = [5, 5, 10, 10, 20]
```
**Output:** 
```python
false
```
**Explanation:**
- From the first two customers, we collect two $5 bills.
- For the next two customers, we collect two $10 bills and give back two $5 bills.
- For the last customer, we cannot give the change of $15 back because we only have two $10 bills.
- Since not every customer received the correct change, the output is `false`.

## Constraints

- `1 <= bills.length <= 10^5`
- `bills[i]` is either $5, $10, or $20.