# CWE-595: Comparison of Object References Instead of Object Contents

**Abstraction:** Variant  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/595.html  

## Description
The product compares object references instead of the contents of the objects themselves, preventing it from detecting equivalent objects.

## Extended Description
For example, in Java, comparing objects using == usually produces deceptive results, since the == operator compares object references rather than values; often, this means that using == for strings is actually comparing the strings' references, not their values.

## Related Weaknesses
- ChildOf: CWE-1025

## Common Consequences
- Scope: Other; Impact: Varies by Context — This weakness can lead to erroneous results that can cause unexpected application behaviors.

## Potential Mitigations
- [Implementation] In Java, use the equals() method to compare objects instead of the == operator. If using ==, it is important for performance reasons that your objects are created by a static factory, not by a constructor.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- In the example below, two Java String objects are declared and initialized with the same string values. An if statement is used to determine if the strings are equivalent.
- In the following Java example, two BankAccount objects are compared in the isSameAccount method using the == operator.
