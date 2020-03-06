# Stack as a Service

Implement an HTTP based service that has basic stack operations as http end points.

## Stack end-points

1. `/push?value=X`
    - pushs X (int number) to the stack.
1. `/pop`
    - will return the top value of the stack. If the stack is empty should return http error.
1. `/max`
    - Should return the max number value from the numbers in the stack
    - Implement the operation with O(1)

## Stress test

Implement a client app that stress tests this service. 
- Measure the time of pushing 10M integeres, and then poping them to empty stack.
- Measure the latency of calling `/max` on every 1000 pushes.
- 
## Acceptable languages
Go, Node.js, Java, Python, C++.
Preferred language: Go

## Criteria

The following are taken into consideration
 * Clean code
 * Proper comments in code (quality, not quantity)
 * Architecture
 * Documentation
 * Tests
 * Linters, CI configuration, .gitignore, test coverage reporting, etc are a bonus
 * Single command to start the solution
 * Single commands and/or documentation for other functionality (e.g. running tests, running linter)
