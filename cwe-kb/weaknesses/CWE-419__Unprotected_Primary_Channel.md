# CWE-419: Unprotected Primary Channel

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/419.html  

## Description
The product uses a primary channel for administration or restricted functionality, but it does not properly protect the channel.

## Related Weaknesses
- ChildOf: CWE-923

## Common Consequences
- Scope: Access Control; Impact: Gain Privileges or Assume Identity, Bypass Protection Mechanism

## Potential Mitigations
- [Architecture and Design] Do not expose administrative functionnality on the user UI.
- [Architecture and Design] Protect the administrative/restricted functionality with a strong authentication mechanism.
