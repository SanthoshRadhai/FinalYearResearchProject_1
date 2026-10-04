# CWE-1041: Use of Redundant Code

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/1041.html  

## Description
The product has multiple functions, methods, procedures, macros, etc. that contain the same code.

## Related Weaknesses
- ChildOf: CWE-710

## Common Consequences
- Scope: Other; Impact: Reduce Maintainability — This issue makes it more difficult to maintain the product, which indirectly affects security by making it more difficult or time-consuming to find and/or fix vulnerabilities. For example, if there are two copies of the same code, the programmer might fix a weakness in one copy while forgetting to fix the same weakness in another copy.

## Potential Mitigations
- [Implementation] Merge common functionality into a single function and then call that function from across the entire code base.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- In the following Java example the code performs some complex math when specific test conditions are met. The math is the same in each case and the equations are repeated within the code. Unfortunately if a future change needs to be made then that change needs to be made in all locations. This opens the door to mistakes being made and the changes not being made in the same way in each instance.
