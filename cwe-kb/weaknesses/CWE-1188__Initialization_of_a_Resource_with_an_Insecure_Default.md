# CWE-1188: Initialization of a Resource with an Insecure Default

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/1188.html  

## Description
The product initializes or sets a resource with a default that is intended to be changed by the product's installer, administrator, or maintainer, but the default is not secure.

## Related Weaknesses
- ChildOf: CWE-1419
- ChildOf: CWE-344
- ChildOf: CWE-665

## Common Consequences
- Scope: Other; Impact: Varies by Context — The impact of insecure defaults varies widely depending on the functionality that the product controls.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- This code attempts to login a user using credentials from a POST request:
