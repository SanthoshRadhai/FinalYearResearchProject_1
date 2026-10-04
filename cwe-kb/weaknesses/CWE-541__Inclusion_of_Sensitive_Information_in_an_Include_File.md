# CWE-541: Inclusion of Sensitive Information in an Include File

**Abstraction:** Variant  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/541.html  

## Description
If an include file source is accessible, the file can contain usernames and passwords, as well as sensitive information pertaining to the application and system.

## Related Weaknesses
- ChildOf: CWE-540

## Common Consequences
- Scope: Confidentiality; Impact: Read Application Data

## Potential Mitigations
- [Architecture and Design] Do not store sensitive information in include files.
- [Architecture and Design, System Configuration] Protect include files from being exposed.

## Demonstrative Examples (summary)
- The following code uses an include file to store database credentials:
