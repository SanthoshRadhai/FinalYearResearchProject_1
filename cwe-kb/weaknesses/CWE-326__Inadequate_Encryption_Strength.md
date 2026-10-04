# CWE-326: Inadequate Encryption Strength

**Abstraction:** Class  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/326.html  

## Description
The product stores or transmits sensitive data using an encryption scheme that is theoretically sound, but is not strong enough for the level of protection required.

## Extended Description
A weak encryption scheme can be subjected to brute force attacks that have a reasonable chance of succeeding using current attack methods and resources.

## Related Weaknesses
- ChildOf: CWE-693

## Common Consequences
- Scope: Access Control, Confidentiality; Impact: Bypass Protection Mechanism, Read Application Data — An attacker may be able to decrypt the data using brute force attacks.

## Potential Mitigations
- [Architecture and Design] Use an encryption scheme that is currently considered to be strong by experts in the field.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)
