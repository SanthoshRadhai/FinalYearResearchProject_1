# CWE-1047: Modules with Circular Dependencies

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/1047.html  

## Description
The product contains modules in which one module has references that cycle back to itself, i.e., there are circular dependencies.

## Extended Description
As an example, with Java, this weakness might indicate cycles between packages.

## Related Weaknesses
- ChildOf: CWE-1120

## Common Consequences
- Scope: Other; Impact: Reduce Maintainability — This issue makes it more difficult to maintain the product due to insufficient modularity, which indirectly affects security by making it more difficult or time-consuming to find and/or fix vulnerabilities. It can also prevent the product from running reliably. If the relevant code is reachable by an attacker, then this reliability problem might introduce a vulnerability.
