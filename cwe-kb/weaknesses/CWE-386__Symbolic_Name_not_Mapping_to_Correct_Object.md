# CWE-386: Symbolic Name not Mapping to Correct Object

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/386.html  

## Description
A constant symbolic reference to an object is used, even though the reference can resolve to a different object over time.

## Related Weaknesses
- ChildOf: CWE-706
- PeerOf: CWE-367
- PeerOf: CWE-610
- PeerOf: CWE-486

## Common Consequences
- Scope: Access Control; Impact: Gain Privileges or Assume Identity — The attacker can gain access to otherwise unauthorized resources.
- Scope: Integrity, Confidentiality, Other; Impact: Modify Application Data, Modify Files or Directories, Read Application Data, Read Files or Directories, Other — Race conditions such as this kind may be employed to gain read or write access to resources not normally readable or writable by the user in question.
- Scope: Integrity, Other; Impact: Modify Application Data, Other — The resource in question, or other resources (through the corrupted one) may be changed in undesirable ways by a malicious user.
- Scope: Non-Repudiation; Impact: Hide Activities — If a file or other resource is written in this method, as opposed to a valid way, logging of the activity may not occur.
- Scope: Non-Repudiation, Integrity; Impact: Modify Files or Directories — In some cases it may be possible to delete files that a malicious user might not otherwise have access to -- such as log files.
