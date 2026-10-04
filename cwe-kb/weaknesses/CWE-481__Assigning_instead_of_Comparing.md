# CWE-481: Assigning instead of Comparing

**Abstraction:** Variant  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/481.html  

## Description
The code uses an operator for assignment when the intention was to perform a comparison.

## Extended Description
In many languages the compare statement is very close in appearance to the assignment statement and are often confused. This bug is generally the result of a typo and usually causes obvious problems with program execution. If the comparison is in an if statement, the if statement will usually evaluate the value of the right-hand side of the predicate.

## Related Weaknesses
- ChildOf: CWE-480
- CanPrecede: CWE-697

## Common Consequences
- Scope: Other; Impact: Alter Execution Logic

## Potential Mitigations
- [Implementation] Place constants on the left. If one attempts to assign a constant with a variable, the compiler will produce an error.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)
- [Automated Static Analysis - Source Code] An Integrated Development Environment (IDE) or linter can report or highlight this weaknesses.

## Demonstrative Examples (summary)
- The following C/C++ and C# examples attempt to validate an int input parameter against the integer value 100.
- In this example, we show how assigning instead of comparing can impact code when values are being passed by reference instead of by value. Consider a scenario in which a string is being processed from user input. Assume the string has already been formatted such that different user inputs are concatenated with the colon character. When the processString function is called, the test for the colon character will result in an insertion of the colon character instead, adding new input separators. Since the string was passed by reference, the data sentinels will be inserted in the original string (CWE-464), and further processing of the inputs will be altered, possibly malformed.
- The following Java example attempts to perform some processing based on the boolean value of the input parameter. However, the expression to be evaluated in the if statement uses the assignment operator "=" rather than the comparison operator "==". As with the previous examples, the variable will be reassigned locally and the expression in the if statement will evaluate to true and unintended processing may occur.
- The following example demonstrates the weakness.
