# CWE-597: Use of Wrong Operator in String Comparison

**Abstraction:** Variant  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/597.html  

## Description
The product uses the wrong operator when comparing a string, such as using "==" when the .equals() method should be used instead.

## Extended Description
In Java, using == or != to compare two strings for equality actually compares two objects for equality rather than their string values for equality. Chances are good that the two references will never be equal. While this weakness often only affects program correctness, if the equality is used for a security decision, the unintended comparison result could be leveraged to affect program security.

## Related Weaknesses
- ChildOf: CWE-595
- ChildOf: CWE-595
- ChildOf: CWE-480

## Common Consequences
- Scope: Other; Impact: Other

## Potential Mitigations
- [Implementation] Within Java, use .equals() to compare string values. Within JavaScript, use == to compare string values. Within PHP, use == to compare a numeric value to a string value. (PHP converts the string to a number.)

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- In the example below, two Java String objects are declared and initialized with the same string values. An if statement is used to determine if the strings are equivalent.
- In the example below, three JavaScript variables are declared and initialized with the same values. Note that JavaScript will change a value between numeric and string as needed, which is the reason an integer is included with the strings. An if statement is used to determine whether the values are the same.
- In the example below, two PHP variables are declared and initialized with the same numbers - one as a string, the other as an integer. Note that PHP will change the string value to a number for a comparison. An if statement is used to determine whether the values are the same.
