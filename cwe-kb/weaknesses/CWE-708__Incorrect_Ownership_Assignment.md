# CWE-708: Incorrect Ownership Assignment

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/708.html  

## Description
The product assigns an owner to a resource, but the owner is outside of the intended control sphere.

## Extended Description
This may allow the resource to be manipulated by actors outside of the intended control sphere.

## Related Weaknesses
- ChildOf: CWE-282
- CanAlsoBe: CWE-345

## Common Consequences
- Scope: Confidentiality, Integrity; Impact: Read Application Data, Modify Application Data — An attacker could read and modify data for which they do not have permissions to access directly.

## Potential Mitigations
- [Policy] Periodically review the privileges and their owners.

## Detection Methods
- [Automated Analysis] Use automated tools to check for privilege settings.
