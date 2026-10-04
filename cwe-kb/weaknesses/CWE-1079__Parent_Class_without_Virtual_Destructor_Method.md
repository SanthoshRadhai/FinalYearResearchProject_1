# CWE-1079: Parent Class without Virtual Destructor Method

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/1079.html  

## Description
A parent class contains one or more child classes, but the parent class does not have a virtual destructor method.

## Related Weaknesses
- ChildOf: CWE-1076

## Common Consequences
- Scope: Other; Impact: Reduce Reliability — This issue can prevent the product from running reliably due to undefined or unexpected behaviors. If the relevant code is reachable by an attacker, then this reliability problem might introduce a vulnerability.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)
