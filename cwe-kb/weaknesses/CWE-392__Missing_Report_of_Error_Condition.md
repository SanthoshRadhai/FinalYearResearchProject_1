# CWE-392: Missing Report of Error Condition

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/392.html  

## Description
The product encounters an error but does not provide a status code or return value to indicate that an error has occurred.

## Related Weaknesses
- ChildOf: CWE-755
- ChildOf: CWE-684
- ChildOf: CWE-703
- ChildOf: CWE-703

## Common Consequences
- Scope: Integrity, Other; Impact: Varies by Context, Unexpected State — Errors that are not properly reported could place the system in an unexpected state that could lead to unintended behaviors.

## Demonstrative Examples (summary)
- In the following snippet from a doPost() servlet method, the server returns "200 OK" (default) even if an error occurs.
