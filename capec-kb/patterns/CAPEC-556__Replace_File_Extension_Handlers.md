# CAPEC-556: Replace File Extension Handlers

**Abstraction:** Detailed  
**Status:** Draft  
**Reference:** https://capec.mitre.org/data/definitions/556.html  

## Description
When a file is opened, its file handler is checked to determine which program opens the file. File handlers are configuration properties of many operating systems. Applications can modify the file handler for a given file extension to call an arbitrary program when a file with the given extension is opened.

## Related Attack Patterns
- ChildOf: CAPEC-542

## Mitigations
- Inspect registry for changes. Limit privileges of user accounts so changes to default file handlers can only be performed by authorized administrators.

## Related Weaknesses (CWE)
- CWE-284
