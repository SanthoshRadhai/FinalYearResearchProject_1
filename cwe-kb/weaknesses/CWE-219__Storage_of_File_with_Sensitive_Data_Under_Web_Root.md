# CWE-219: Storage of File with Sensitive Data Under Web Root

**Abstraction:** Variant  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/219.html  

## Description
The product stores sensitive data under the web document root with insufficient access control, which might make it accessible to untrusted parties.

## Extended Description
Besides public-facing web pages and code, products may store sensitive data, code that is not directly invoked, or other files under the web document root of the web server. If the server is not configured or otherwise used to prevent direct access to those files, then attackers may obtain this sensitive data.

## Related Weaknesses
- ChildOf: CWE-552

## Common Consequences
- Scope: Confidentiality; Impact: Read Application Data

## Potential Mitigations
- [Implementation, System Configuration] Avoid storing information under the web root directory.
- [System Configuration] Access control permissions should be set to prevent reading/writing of sensitive files inside/outside of the web directory.
