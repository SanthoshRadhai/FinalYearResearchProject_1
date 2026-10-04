# CWE-538: Insertion of Sensitive Information into Externally-Accessible File or Directory

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/538.html  

## Description
The product places sensitive information into files or directories that are accessible to actors who are allowed to have access to the files, but not to the sensitive information.

## Related Weaknesses
- ChildOf: CWE-200

## Common Consequences
- Scope: Confidentiality; Impact: Read Files or Directories

## Potential Mitigations
- [Architecture and Design, Operation, System Configuration] Do not expose file and directory information to the user.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- In the following code snippet, a user's full name and credit card number are written to a log file.
