# CWE-1104: Use of Unmaintained Third Party Components

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/1104.html  

## Description
The product relies on third-party components that are not actively supported or maintained by the original developer or a trusted proxy for the original developer.

## Related Weaknesses
- ChildOf: CWE-1357

## Common Consequences
- Scope: Other; Impact: Reduce Maintainability, Varies by Context — Relying on unmaintained components makes it difficult or impossible to fix significant bugs and vulnerabilities, can render code obsolete, and undermine security by complicating maintenance and increasing the risk of new vulnerabilities.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)
