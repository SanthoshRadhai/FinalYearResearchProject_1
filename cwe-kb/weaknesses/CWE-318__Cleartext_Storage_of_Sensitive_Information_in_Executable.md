# CWE-318: Cleartext Storage of Sensitive Information in Executable

**Abstraction:** Variant  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/318.html  

## Description
The product stores sensitive information in cleartext in an executable.

## Extended Description
Attackers can reverse engineer binary code to obtain secret data. This is especially easy when the cleartext is plain ASCII. Even if the information is encoded in a way that is not human-readable, certain techniques could determine which encoding is being used, then decode the information.

## Related Weaknesses
- ChildOf: CWE-312

## Common Consequences
- Scope: Confidentiality; Impact: Read Application Data
