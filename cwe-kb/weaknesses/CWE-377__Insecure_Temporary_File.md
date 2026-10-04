# CWE-377: Insecure Temporary File

**Abstraction:** Class  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/377.html  

## Description
Creating and using insecure temporary files can leave application and system data vulnerable to attack.

## Related Weaknesses
- ChildOf: CWE-668

## Common Consequences
- Scope: Confidentiality, Integrity; Impact: Read Files or Directories, Modify Files or Directories

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- The following code uses a temporary file for storing intermediate data gathered from the network before it is processed.
