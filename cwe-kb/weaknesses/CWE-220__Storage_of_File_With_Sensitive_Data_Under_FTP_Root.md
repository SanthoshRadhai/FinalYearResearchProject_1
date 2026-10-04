# CWE-220: Storage of File With Sensitive Data Under FTP Root

**Abstraction:** Variant  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/220.html  

## Description
The product stores sensitive data under the FTP server root with insufficient access control, which might make it accessible to untrusted parties.

## Related Weaknesses
- ChildOf: CWE-552

## Common Consequences
- Scope: Confidentiality; Impact: Read Application Data

## Potential Mitigations
- [Implementation, System Configuration] Avoid storing information under the FTP root directory.
- [System Configuration] Access control permissions should be set to prevent reading/writing of sensitive files inside/outside of the FTP directory.
