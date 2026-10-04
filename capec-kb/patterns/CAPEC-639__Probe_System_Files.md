# CAPEC-639: Probe System Files

**Abstraction:** Detailed  
**Status:** Stable  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/639.html  

## Description
An adversary obtains unauthorized information due to improperly protected files. If an application stores sensitive information in a file that is not protected by proper access control, then an adversary can access the file and search for sensitive information.

## Related Attack Patterns
- ChildOf: CAPEC-545

## Prerequisites
- An adversary has access to the file system of a system.

## Consequences
- Scope: Confidentiality; Impact: Read Data

## Mitigations
- Verify that files have proper access controls set, and reduce the storage of sensitive information to only what is necessary.

## Related Weaknesses (CWE)
- CWE-552
