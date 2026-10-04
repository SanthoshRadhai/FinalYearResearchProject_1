# CWE-529: Exposure of Access Control List Files to an Unauthorized Control Sphere

**Abstraction:** Variant  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/529.html  

## Description
The product stores access control list files in a directory or other container that is accessible to actors outside of the intended control sphere.

## Extended Description
Exposure of these access control list files may give the attacker information about the configuration of the site or system. This information may then be used to bypass the intended security policy or identify trusted systems from which an attack can be launched.

## Related Weaknesses
- ChildOf: CWE-552

## Common Consequences
- Scope: Confidentiality, Access Control; Impact: Read Application Data, Bypass Protection Mechanism

## Potential Mitigations
- [System Configuration] Protect access control list files.
