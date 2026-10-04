# CWE-832: Unlock of a Resource that is not Locked

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/832.html  

## Description
The product attempts to unlock a resource that is not locked.

## Extended Description
Depending on the locking functionality, an unlock of a non-locked resource might cause memory corruption or other modification to the resource (or its associated metadata that is used for tracking locks).

## Related Weaknesses
- ChildOf: CWE-667

## Common Consequences
- Scope: Integrity, Confidentiality, Availability, Other; Impact: DoS: Crash, Exit, or Restart, Execute Unauthorized Code or Commands, Modify Memory, Other — Depending on the locking being used, an unlock operation might not have any adverse effects. When effects exist, the most common consequence will be a corruption of the state of the product, possibly leading to a crash or exit; depending on the implementation of the unlocking, memory corruption or code execution could occur.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)
