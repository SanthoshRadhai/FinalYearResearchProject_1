# CWE-480: Use of Incorrect Operator

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/480.html  

## Description
The product accidentally uses the wrong operator, which changes the logic in security-relevant ways.

## Extended Description
These types of errors are generally the result of a typo by the programmer.

## Related Weaknesses
- ChildOf: CWE-670

## Common Consequences
- Scope: Other; Impact: Alter Execution Logic — This weakness can cause unintended logic to be executed and other unexpected application behavior.

## Detection Methods
- [Automated Static Analysis] This weakness can be found easily using static analysis. However in some cases an operator might appear to be incorrect, but is actually correct and reflects unusual logic within the program.
- [Manual Static Analysis] This weakness can be found easily using static analysis. However in some cases an operator might appear to be incorrect, but is actually correct and reflects unusual logic within the program.

## Demonstrative Examples (summary)
- The following C/C++ and C# examples attempt to validate an int input parameter against the integer value 100.
- The following C/C++ example shows a simple implementation of a stack that includes methods for adding and removing integer values from the stack. The example uses pointers to add and remove integer values to the stack array variable.
- The example code below is taken from the CVA6 processor core of the HACK@DAC'21 buggy OpenPiton SoC. Debug access allows users to access internal hardware registers that are otherwise not exposed for user access or restricted access through access control protocols. Hence, requests to enter debug mode are checked and authorized only if the processor has sufficient privileges. In addition, debug accesses are also locked behind password checkers. Thus, the processor enters debug mode only when the privilege level requirement is met, and the correct debug password is provided.
