# CWE-115: Misinterpretation of Input

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/115.html  

## Description
The product misinterprets an input, whether from an attacker or another product, in a security-relevant fashion.

## Related Weaknesses
- ChildOf: CWE-436

## Common Consequences
- Scope: Integrity; Impact: Unexpected State

## Detection Methods
- [Fuzzing] Fuzz testing (fuzzing) is a powerful technique for generating large numbers of diverse inputs - either randomly or algorithmically - and dynamically invoking the code with those inputs. Even with random inputs, it is often capable of generating unexpected results such as crashes, memory corruption, or resource consumption. Fuzzing effectively produces repeatable test cases that clearly indicate bugs, which helps developers to diagnose the issues.
