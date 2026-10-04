# CAPEC-240: Resource Injection

**Abstraction:** Meta  
**Status:** Stable  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/240.html  

## Description
An adversary exploits weaknesses in input validation by manipulating resource identifiers enabling the unintended modification or specification of a resource.

## Prerequisites
- The target application allows the user to both specify the identifier used to access a system resource. Through this permission, the user gains the capability to perform actions on that resource (e.g., overwrite the file)

## Consequences
- Scope: Confidentiality; Impact: Read Data
- Scope: Integrity; Impact: Modify Data

## Mitigations
- Ensure all input content that is delivered to client is sanitized against an acceptable content specification.
- Perform input validation for all content.
- Enforce regular patching of software.

## Related Weaknesses (CWE)
- CWE-99
