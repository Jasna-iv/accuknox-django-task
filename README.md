 
README.md
 
# Django Signals and Python Iterator Task
 
## Django Signals
 
### Question 1
 
Django signals execute synchronously by default.
 
Proof:
The execution waits until the signal finishes execution.
 
---
 
### Question 2
 
Signals execute in the same thread by default.
 
Proof:
The thread IDs printed from both caller and signal are identical.
 
---
 
### Question 3
 
Signals work inside the same database transaction.
 
Proof:
When an exception occurs inside transaction.atomic(),
database operations are rolled back.
 
---
 
## Python Iterator
 
The Box class supports iteration using __iter__().
 
Example Output:
 
{'height': 20}
{'breadth': 8}