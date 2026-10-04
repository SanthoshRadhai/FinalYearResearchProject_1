# CWE-314: Cleartext Storage in the Registry

**Abstraction:** Variant  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/314.html  

## Description
The product stores sensitive information in cleartext in the registry.

## Extended Description
Attackers can read the information by accessing the registry key. Even if the information is encoded in a way that is not human-readable, certain techniques could determine which encoding is being used, then decode the information.

## Related Weaknesses
- ChildOf: CWE-312

## Common Consequences
- Scope: Confidentiality; Impact: Read Application Data
