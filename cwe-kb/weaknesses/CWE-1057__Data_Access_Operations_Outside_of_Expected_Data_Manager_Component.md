# CWE-1057: Data Access Operations Outside of Expected Data Manager Component

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/1057.html  

## Description
The product uses a dedicated, central data manager component as required by design, but it contains code that performs data-access operations that do not use this data manager.

## Related Weaknesses
- ChildOf: CWE-1061

## Common Consequences
- Scope: Availability; Impact: Reduce Performance — This issue can make the product perform more slowly than intended, since the intended central data manager may have been explicitly optimized for performance or other quality characteristics. If the relevant code is reachable by an attacker, then this performance problem might introduce a vulnerability.
