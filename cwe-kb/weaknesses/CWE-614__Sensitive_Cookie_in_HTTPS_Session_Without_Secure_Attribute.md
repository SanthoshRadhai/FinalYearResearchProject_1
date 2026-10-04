# CWE-614: Sensitive Cookie in HTTPS Session Without 'Secure' Attribute

**Abstraction:** Variant  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/614.html  

## Description
The Secure attribute for sensitive cookies in HTTPS sessions is not set.

## Related Weaknesses
- ChildOf: CWE-319

## Common Consequences
- Scope: Confidentiality; Impact: Read Application Data — Omitting the secure flag makes it possible for the user agent to send the cookies in plaintext over an HTTP session.

## Potential Mitigations
- [Implementation] Always set the secure attribute when the cookie should be sent via HTTPS only.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- The snippet of code below, taken from a servlet doPost() method, sets an accountID cookie (sensitive) without calling setSecure(true).
