# CWE-500: Public Static Field Not Marked Final

**Abstraction:** Variant  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/500.html  

## Description
An object contains a public static field that is not marked final, which might allow it to be modified in unexpected ways.

## Extended Description
Public static variables can be read without an accessor and changed without a mutator by any classes in the application.

## Related Weaknesses
- ChildOf: CWE-493

## Common Consequences
- Scope: Integrity; Impact: Modify Application Data — The object could potentially be tampered with.
- Scope: Confidentiality; Impact: Read Application Data — The object could potentially allow the object to be read.

## Potential Mitigations
- [Architecture and Design] Clearly identify the scope for all critical data elements, including whether they should be regarded as static.
- [Implementation] Make any static fields private and constant. A constant field is denoted by the keyword 'const' in C/C++ and ' final' in Java

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- The following examples use of a public static String variable to contain the name of a property/configuration file for the application.
