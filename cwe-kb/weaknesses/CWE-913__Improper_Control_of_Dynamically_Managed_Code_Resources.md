# CWE-913: Improper Control of Dynamically-Managed Code Resources

**Abstraction:** Class  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/913.html  

## Description
The product does not properly restrict reading from or writing to dynamically-managed code resources such as variables, objects, classes, attributes, functions, or executable instructions or statements.

## Extended Description
Many languages offer powerful features that allow the programmer to dynamically create or modify existing code, or resources used by code such as variables and objects. While these features can offer significant flexibility and reduce development time, they can be extremely dangerous if attackers can directly influence these code resources in unexpected ways.

## Related Weaknesses
- ChildOf: CWE-664

## Common Consequences
- Scope: Integrity; Impact: Execute Unauthorized Code or Commands
- Scope: Other, Integrity; Impact: Varies by Context, Alter Execution Logic

## Potential Mitigations
- [Implementation] For any externally-influenced input, check the input against an allowlist of acceptable values.
- [Implementation, Architecture and Design] Refactor the code so that it does not need to be dynamically managed.

## Detection Methods
- [Fuzzing] Fuzz testing (fuzzing) is a powerful technique for generating large numbers of diverse inputs - either randomly or algorithmically - and dynamically invoking the code with those inputs. Even with random inputs, it is often capable of generating unexpected results such as crashes, memory corruption, or resource consumption. Fuzzing effectively produces repeatable test cases that clearly indicate bugs, which helps developers to diagnose the issues.

## Demonstrative Examples (summary)
- This example attempts to write user messages to a message file and allow users to view them.
- A common reason that programmers use the reflection API is to implement their own command dispatcher. The following example shows a command dispatcher that does not use reflection:
