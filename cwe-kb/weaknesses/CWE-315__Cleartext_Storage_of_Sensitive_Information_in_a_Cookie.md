# CWE-315: Cleartext Storage of Sensitive Information in a Cookie

**Abstraction:** Variant  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/315.html  

## Description
The product stores sensitive information in cleartext in a cookie.

## Extended Description
Attackers can use widely-available tools to view the cookie and read the sensitive information. Even if the information is encoded in a way that is not human-readable, certain techniques could determine which encoding is being used, then decode the information.

## Related Weaknesses
- ChildOf: CWE-312

## Common Consequences
- Scope: Confidentiality; Impact: Read Application Data

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- The following code excerpt stores a plaintext user account ID in a browser cookie.
