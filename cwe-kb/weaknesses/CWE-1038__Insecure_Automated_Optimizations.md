# CWE-1038: Insecure Automated Optimizations

**Abstraction:** Class  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/1038.html  

## Description
The product uses a mechanism that automatically optimizes code, e.g. to improve a characteristic such as performance, but the optimizations can have an unintended side effect that might violate an intended security assumption.

## Related Weaknesses
- ChildOf: CWE-435
- ChildOf: CWE-758

## Common Consequences
- Scope: Integrity; Impact: Alter Execution Logic — The optimizations alter the order of execution resulting in side effects that were not intended by the original developer.

## Demonstrative Examples (summary)
- The following code reads a password from the user, uses the password to connect to a back-end mainframe, and then attempts to scrub the password from memory using memset().
