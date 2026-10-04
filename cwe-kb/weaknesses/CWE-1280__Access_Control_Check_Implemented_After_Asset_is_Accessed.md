# CWE-1280: Access Control Check Implemented After Asset is Accessed

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/1280.html  

## Description
A product's hardware-based access control check occurs after the asset has been accessed.

## Extended Description
The product implements a hardware-based access control check. The asset should be accessible only after the check is successful. If, however, this operation is not atomic and the asset is accessed before the check is complete, the security of the system may be compromised.

## Related Weaknesses
- ChildOf: CWE-696
- ChildOf: CWE-284

## Common Consequences
- Scope: Access Control, Confidentiality, Integrity; Impact: Modify Memory, Read Memory, Modify Application Data, Read Application Data, Gain Privileges or Assume Identity, Bypass Protection Mechanism

## Potential Mitigations
- [Implementation] Implement the access control check first. Access should only be given to asset if agent is authorized.

## Demonstrative Examples (summary)
- Assume that the module foo_bar implements a protected register. The register content is the asset. Only transactions made by user id (indicated by signal usr_id) 0x4 are allowed to modify the register contents. The signal grant_access is used to provide access.
