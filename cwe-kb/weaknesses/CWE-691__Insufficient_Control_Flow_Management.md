# CWE-691: Insufficient Control Flow Management

**Abstraction:** Pillar  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/691.html  

## Description
The code does not sufficiently manage its control flow during execution, creating conditions in which the control flow can be modified in unexpected ways.

## Common Consequences
- Scope: Other; Impact: Alter Execution Logic

## Demonstrative Examples (summary)
- The following function attempts to acquire a lock in order to perform operations on a shared resource.
- In this example, the programmer has indented the statements to call Do_X() and Do_Y(), as if the intention is that these functions are only called when the condition is true. However, because there are no braces to signify the block, Do_Y() will always be executed, even if the condition is false.
- This function prints the contents of a specified file requested by a user.
