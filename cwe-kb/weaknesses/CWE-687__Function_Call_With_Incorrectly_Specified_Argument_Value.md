# CWE-687: Function Call With Incorrectly Specified Argument Value

**Abstraction:** Variant  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/687.html  

## Description
The product calls a function, procedure, or routine, but the caller specifies an argument that contains the wrong value, which may lead to resultant weaknesses.

## Related Weaknesses
- ChildOf: CWE-628

## Common Consequences
- Scope: Other; Impact: Quality Degradation

## Detection Methods
- [Manual Static Analysis] This might require an understanding of intended program behavior or design to determine whether the value is incorrect.

## Demonstrative Examples (summary)
- This Perl code intends to record whether a user authenticated successfully or not, and to exit if the user fails to authenticate. However, when it calls ReportAuth(), the third argument is specified as 0 instead of 1, so it does not exit.
