# CWE-195: Signed to Unsigned Conversion Error

**Abstraction:** Variant  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/195.html  

## Description
The product uses a signed primitive and performs a cast to an unsigned primitive, which can produce an unexpected value if the value of the signed primitive can not be represented using an unsigned primitive.

## Extended Description
It is dangerous to rely on implicit casts between signed and unsigned numbers because the result can take on an unexpected value and violate assumptions made by the program. Often, functions will return negative values to indicate a failure. When the result of a function is to be used as a size parameter, using these negative return values can have unexpected results. For example, if negative size values are passed to the standard memory copy or allocation functions they will be implicitly cast to a large unsigned value. This may lead to an exploitable buffer overflow or underflow condition.

## Related Weaknesses
- ChildOf: CWE-681
- ChildOf: CWE-681
- ChildOf: CWE-681
- CanPrecede: CWE-119

## Common Consequences
- Scope: Integrity; Impact: Unexpected State — Conversion between signed and unsigned values can lead to a variety of errors, but from a security standpoint is most commonly associated with integer overflow and buffer overflow vulnerabilities.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- In this example the variable amount can hold a negative value when it is returned. Because the function is declared to return an unsigned int, amount will be implicitly converted to unsigned.
- In this example, depending on the return value of accecssmainframe(), the variable amount can hold a negative value when it is returned. Because the function is declared to return an unsigned value, amount will be implicitly cast to an unsigned number.
- The following code is intended to read an incoming packet from a socket and extract one or more headers.
- This example processes user input comprised of a series of variable-length structures. The first 2 bytes of input dictate the size of the structure to be processed.
- In the following example, it is possible to request that memcpy move a much larger segment of memory than assumed:
- This example shows a typical attempt to parse a string with an error resulting from a difference in assumptions between the caller to a function and the function's action.
