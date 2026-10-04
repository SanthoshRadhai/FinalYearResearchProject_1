# CWE-393: Return of Wrong Status Code

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/393.html  

## Description
A function or operation returns an incorrect return value or status code that does not indicate the true result of execution, causing the product to modify its behavior based on the incorrect result.

## Extended Description
This can lead to unpredictable behavior. If the function is used to make security-critical decisions or provide security-critical information, then the wrong status code can cause the product to assume that an action is safe or correct, even when it is not.

## Related Weaknesses
- ChildOf: CWE-684
- ChildOf: CWE-703

## Common Consequences
- Scope: Integrity, Other; Impact: Unexpected State, Alter Execution Logic — This weakness could place the system in a state that could lead unexpected logic to be executed or other unintended behaviors.

## Detection Methods
- [Fuzzing] Fuzz testing (fuzzing) is a powerful technique for generating large numbers of diverse inputs - either randomly or algorithmically - and dynamically invoking the code with those inputs. Even with random inputs, it is often capable of generating unexpected results such as crashes, memory corruption, or resource consumption. Fuzzing effectively produces repeatable test cases that clearly indicate bugs, which helps developers to diagnose the issues.

## Demonstrative Examples (summary)
- In the following example, an HTTP 404 status code is returned in the event of an IOException encountered in a Java servlet. A 404 code is typically meant to indicate a non-existent resource and would be somewhat misleading in this case.
