# CWE-108: Struts: Unvalidated Action Form

**Abstraction:** Variant  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/108.html  

## Description
Every Action Form must have a corresponding validation form.

## Extended Description
If a Struts Action Form Mapping specifies a form, it must have a validation form defined under the Struts Validator.

## Related Weaknesses
- ChildOf: CWE-1173
- ChildOf: CWE-20

## Common Consequences
- Scope: Other; Impact: Other — If an action form mapping does not have a validation form defined, it may be vulnerable to a number of attacks that rely on unchecked input. Unchecked input is the root cause of some of today's worst and most common software security problems. Cross-site scripting, SQL injection, and process control vulnerabilities all stem from incomplete or absent input validation.
- Scope: Confidentiality, Integrity, Availability, Other; Impact: Other — Although J2EE applications are not generally susceptible to memory corruption attacks, if a J2EE application interfaces with native code that does not perform array bounds checking, an attacker may be able to use an input validation mistake in the J2EE application to launch a buffer overflow attack.

## Potential Mitigations
- [Implementation] Map every Action Form to a corresponding validation form. An action or a form may perform validation in other ways, but the Struts Validator provides an excellent way to verify that all input receives at least a basic level of validation. Without this approach, it is difficult, and often impossible, to establish with a high level of confidence that all input is validated.
