# CWE-340: Generation of Predictable Numbers or Identifiers

**Abstraction:** Class  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/340.html  

## Description
The product uses a scheme that generates numbers or identifiers that are more predictable than required.

## Related Weaknesses
- ChildOf: CWE-330
- CanPrecede: CWE-384

## Common Consequences
- Scope: Other; Impact: Varies by Context

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- This code generates a unique random identifier for a user's session.
