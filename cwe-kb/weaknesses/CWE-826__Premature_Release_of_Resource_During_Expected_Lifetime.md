# CWE-826: Premature Release of Resource During Expected Lifetime

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/826.html  

## Description
The product releases a resource that is still intended to be used by itself or another actor.

## Extended Description
This weakness focuses on errors in which the product should not release a resource, but performs the release anyway. This is different than a weakness in which the product releases a resource at the appropriate time, but it maintains a reference to the resource, which it later accesses. For this weakness, the resource should still be valid upon the subsequent access. When a product releases a resource that is still being used, it is possible that operations will still be taken on this resource, which may have been repurposed in the meantime, leading to issues similar to CWE-825. Consequences may include denial of service, information exposure, or code execution.

## Related Weaknesses
- ChildOf: CWE-666
- CanPrecede: CWE-672

## Common Consequences
- Scope: Confidentiality; Impact: Read Application Data, Read Memory — If the released resource is subsequently reused or reallocated, then a read operation on the original resource might access sensitive data that is associated with a different user or entity.
- Scope: Availability; Impact: DoS: Crash, Exit, or Restart — When the resource is released, the software might modify some of its structure, or close associated channels (such as a file descriptor). When the software later accesses the resource as if it is valid, the resource might not be in an expected state, leading to resultant errors that may lead to a crash.
- Scope: Integrity, Confidentiality, Availability; Impact: Execute Unauthorized Code or Commands, Modify Application Data, Modify Memory — When the resource is released, the software might modify some of its structure. This might affect logic in the sections of code that still assume the resource is active. If the released resource is related to memory and is used in a function call, or points to unexpected data in a write operation, then code execution may be possible upon subsequent accesses.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)
