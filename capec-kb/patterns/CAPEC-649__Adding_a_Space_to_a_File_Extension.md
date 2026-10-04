# CAPEC-649: Adding a Space to a File Extension

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/649.html  

## Description
An adversary adds a space character to the end of a file extension and takes advantage of an application that does not properly neutralize trailing special elements in file names. This extra space, which can be difficult for a user to notice, affects which default application is used to operate on the file and can be leveraged by the adversary to control execution.

## Related Attack Patterns
- ChildOf: CAPEC-635

## Prerequisites
- The use of the file must be controlled by the file extension.

## Consequences
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands

## Mitigations
- File extensions should be checked to see if non-visible characters are being included.

## Related Weaknesses (CWE)
- CWE-46
