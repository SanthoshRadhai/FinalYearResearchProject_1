# CWE-1069: Empty Exception Block

**Abstraction:** Variant  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/1069.html  

## Description
An invokable code block contains an exception handling block that does not contain any code, i.e. is empty.

## Related Weaknesses
- ChildOf: CWE-1071

## Common Consequences
- Scope: Other; Impact: Reduce Reliability — When an exception handling block (such as a Catch and Finally block) is used, but that block is empty, this can prevent the product from running reliably. If the relevant code is reachable by an attacker, then this reliability problem might introduce a vulnerability.

## Potential Mitigations
- [Implementation] For every exception block add code that handles the specific exception in the way intended by the application.

## Demonstrative Examples (summary)
- In the following Java example, the code catches an ArithmeticException.
