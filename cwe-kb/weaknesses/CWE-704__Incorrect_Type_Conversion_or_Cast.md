# CWE-704: Incorrect Type Conversion or Cast

**Abstraction:** Class  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/704.html  

## Description
The product does not correctly convert an object, resource, or structure from one type to a different type.

## Related Weaknesses
- ChildOf: CWE-664

## Common Consequences
- Scope: Other; Impact: Other

## Detection Methods
- [Fuzzing] Fuzz testing (fuzzing) is a powerful technique for generating large numbers of diverse inputs - either randomly or algorithmically - and dynamically invoking the code with those inputs. Even with random inputs, it is often capable of generating unexpected results such as crashes, memory corruption, or resource consumption. Fuzzing effectively produces repeatable test cases that clearly indicate bugs, which helps developers to diagnose the issues.

## Demonstrative Examples (summary)
- In this example, depending on the return value of accecssmainframe(), the variable amount can hold a negative value when it is returned. Because the function is declared to return an unsigned value, amount will be implicitly cast to an unsigned number.
- The following code uses a union to support the representation of different types of messages. It formats messages differently, depending on their type.
