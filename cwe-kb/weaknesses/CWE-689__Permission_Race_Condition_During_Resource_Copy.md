# CWE-689: Permission Race Condition During Resource Copy

**Abstraction:** Compound  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/689.html  

## Description
The product, while copying or cloning a resource, does not set the resource's permissions or access control until the copy is complete, leaving the resource exposed to other spheres while the copy is taking place.

## Related Weaknesses
- ChildOf: CWE-362
- Requires: CWE-362
- Requires: CWE-732

## Common Consequences
- Scope: Confidentiality, Integrity; Impact: Read Application Data, Modify Application Data
