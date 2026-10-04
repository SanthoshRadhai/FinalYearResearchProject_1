# CWE-528: Exposure of Core Dump File to an Unauthorized Control Sphere

**Abstraction:** Variant  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/528.html  

## Description
The product generates a core dump file in a directory, archive, or other resource that is stored, transferred, or otherwise made accessible to unauthorized actors.

## Related Weaknesses
- ChildOf: CWE-552

## Common Consequences
- Scope: Confidentiality; Impact: Read Application Data, Read Files or Directories

## Potential Mitigations
- [System Configuration] Protect the core dump files from unauthorized access.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)
