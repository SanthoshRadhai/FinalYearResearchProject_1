# CWE-623: Unsafe ActiveX Control Marked Safe For Scripting

**Abstraction:** Variant  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/623.html  

## Description
An ActiveX control is intended for restricted use, but it has been marked as safe-for-scripting.

## Extended Description
This might allow attackers to use dangerous functionality via a web page that accesses the control, which can lead to different resultant vulnerabilities, depending on the control's behavior.

## Related Weaknesses
- ChildOf: CWE-267
- PeerOf: CWE-618

## Common Consequences
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Code or Commands

## Potential Mitigations
- [Architecture and Design] During development, do not mark it as safe for scripting.
- [System Configuration] After distribution, you can set the kill bit for the control so that it is not accessible from Internet Explorer.
