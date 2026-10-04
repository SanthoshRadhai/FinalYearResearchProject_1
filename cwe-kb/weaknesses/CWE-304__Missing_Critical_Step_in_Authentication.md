# CWE-304: Missing Critical Step in Authentication

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/304.html  

## Description
The product implements an authentication technique, but it skips a step that weakens the technique.

## Extended Description
Authentication techniques should follow the algorithms that define them exactly, otherwise authentication can be bypassed or more easily subjected to brute force attacks.

## Related Weaknesses
- ChildOf: CWE-303
- ChildOf: CWE-573

## Common Consequences
- Scope: Access Control, Integrity, Confidentiality; Impact: Bypass Protection Mechanism, Gain Privileges or Assume Identity, Read Application Data, Execute Unauthorized Code or Commands — This weakness can lead to the exposure of resources or functionality to unintended actors, possibly providing attackers with sensitive information or allowing attackers to execute arbitrary code.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)
