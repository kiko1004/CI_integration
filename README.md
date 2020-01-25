# Stack as a Service

Implement http based service that has simple simple stack operations as http end points.

## Stack end-points

1. `/push?value=(number)`
    - push a number value to the stack in the service
2. `/pop`
    - will return the top value of the stack. If the stack is empty should return 400 (no-content)
3. `/max`
    - Should return the max number value from the numbers in the stack
    - Implement the operation with O(1) no matters how big is the stack

## Stress test

Implement a client app that stress tests this service. 
- Measure the time of pushing 10M integeres, and then poping them to empty stack.
- Measure the latency of calling `/max` on every 1000 pushes.