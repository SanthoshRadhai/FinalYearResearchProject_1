# CWE-1024: Comparison of Incompatible Types

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/1024.html  

## Description
The product performs a comparison between two entities, but the entities are of different, incompatible types that cannot be guaranteed to provide correct results when they are directly compared.

## Related Weaknesses
- ChildOf: CWE-697

## Common Consequences
- Scope: Other; Impact: Varies by Context

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)
- [Manual Static Analysis] Thoroughly test the comparison scheme before deploying code into production. Perform positive testing as well as negative testing.
