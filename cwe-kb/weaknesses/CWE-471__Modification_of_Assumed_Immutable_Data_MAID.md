# CWE-471: Modification of Assumed-Immutable Data (MAID)

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/471.html  

## Description
The product does not properly protect an assumed-immutable element from being modified by an attacker.

## Extended Description
This occurs when a particular input is critical enough to the functioning of the application that it should not be modifiable at all, but it is. Certain resources are often assumed to be immutable when they are not, such as hidden form fields in web applications, cookies, and reverse DNS lookups.

## Related Weaknesses
- ChildOf: CWE-664

## Common Consequences
- Scope: Integrity; Impact: Modify Application Data — Common data types that are attacked are environment variables, web application parameters, and HTTP headers.
- Scope: Integrity; Impact: Unexpected State

## Potential Mitigations
- [Architecture and Design, Operation, Implementation] When the data is stored or transmitted through untrusted sources that could modify the data, implement integrity checks to detect unauthorized modification, or store/transmit the data in a trusted location that is free from external influence.

## Demonstrative Examples (summary)
- In the code excerpt below, an array returned by a Java method is modified despite the fact that arrays are mutable.
