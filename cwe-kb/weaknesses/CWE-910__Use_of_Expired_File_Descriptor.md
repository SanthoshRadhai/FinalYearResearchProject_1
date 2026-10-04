# CWE-910: Use of Expired File Descriptor

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/910.html  

## Description
The product uses or accesses a file descriptor after it has been closed.

## Extended Description
After a file descriptor for a particular file or device has been released, it can be reused. The code might not write to the original file, since the reused file descriptor might reference a different file or device.

## Related Weaknesses
- ChildOf: CWE-672

## Common Consequences
- Scope: Confidentiality; Impact: Read Files or Directories — The program could read data from the wrong file.
- Scope: Availability; Impact: DoS: Crash, Exit, or Restart — Accessing a file descriptor that has been closed can cause a crash.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)
