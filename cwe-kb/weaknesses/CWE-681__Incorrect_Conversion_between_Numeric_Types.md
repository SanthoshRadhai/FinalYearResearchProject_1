# CWE-681: Incorrect Conversion between Numeric Types

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/681.html  

## Description
When converting from one data type to another, such as long to integer, data can be omitted or translated in a way that produces unexpected values. If the resulting values are used in a sensitive context, then dangerous behaviors may occur.

## Related Weaknesses
- ChildOf: CWE-704
- ChildOf: CWE-704
- CanPrecede: CWE-682

## Common Consequences
- Scope: Other, Integrity; Impact: Unexpected State, Quality Degradation — The program could wind up using the wrong number and generate incorrect results. If the number is used to allocate resources or make a security decision, then this could introduce a vulnerability.

## Potential Mitigations
- [Implementation] Avoid making conversion between numeric types. Always check for the allowed ranges.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- In the following Java example, a float literal is cast to an integer, thus causing a loss of precision.
- This code adds a float and an integer together, casting the result to an integer.
- In this example the variable amount can hold a negative value when it is returned. Because the function is declared to return an unsigned int, amount will be implicitly converted to unsigned.
- In this example, depending on the return value of accecssmainframe(), the variable amount can hold a negative value when it is returned. Because the function is declared to return an unsigned value, amount will be implicitly cast to an unsigned number.
