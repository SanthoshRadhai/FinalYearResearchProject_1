# CWE-344: Use of Invariant Value in Dynamically Changing Context

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/344.html  

## Description
The product uses a constant value, name, or reference, but this value can (or should) vary across different environments.

## Related Weaknesses
- ChildOf: CWE-330

## Common Consequences
- Scope: Other; Impact: Varies by Context

## Demonstrative Examples (summary)
- The following code is an example of an internal hard-coded password in the back-end:
- This code assumes a particular function will always be found at a particular address. It assigns a pointer to that address and calls the function.
