# CWE-733: Compiler Optimization Removal or Modification of Security-critical Code

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/733.html  

## Description
The developer builds a security-critical protection mechanism into the software, but the compiler optimizes the program such that the mechanism is removed or modified.

## Related Weaknesses
- ChildOf: CWE-1038

## Common Consequences
- Scope: Access Control, Other; Impact: Bypass Protection Mechanism, Alter Execution Logic

## Detection Methods
- [Black Box] This specific weakness is impossible to detect using black box methods. While an analyst could examine memory to see that it has not been scrubbed, an analysis of the executable would not be successful. This is because the compiler has already removed the relevant code. Only the source code shows whether the programmer intended to clear the memory or not, so this weakness is indistinguishable from others.
- [White Box] This weakness is only detectable using white box methods (see black box detection factor). Careful analysis is required to determine if the code is likely to be removed by the compiler.

## Demonstrative Examples (summary)
- The following code reads a password from the user, uses the password to connect to a back-end mainframe, and then attempts to scrub the password from memory using memset().
