# CWE-317: Cleartext Storage of Sensitive Information in GUI

**Abstraction:** Variant  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/317.html  

## Description
The product stores sensitive information in cleartext within the GUI.

## Extended Description
An attacker can often obtain data from a GUI, even if hidden, by using an API to directly access GUI objects such as windows and menus. Even if the information is encoded in a way that is not human-readable, certain techniques could determine which encoding is being used, then decode the information.

## Related Weaknesses
- ChildOf: CWE-312

## Common Consequences
- Scope: Confidentiality; Impact: Read Memory, Read Application Data
