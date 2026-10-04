# CWE-110: Struts: Validator Without Form Field

**Abstraction:** Variant  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/110.html  

## Description
Validation fields that do not appear in forms they are associated with indicate that the validation logic is out of date.

## Extended Description
It is easy for developers to forget to update validation logic when they make changes to an ActionForm class. One indication that validation logic is not being properly maintained is inconsistencies between the action form and the validation form. Although J2EE applications are not generally susceptible to memory corruption attacks, if a J2EE application interfaces with native code that does not perform array bounds checking, an attacker may be able to use an input validation mistake in the J2EE application to launch a buffer overflow attack.

## Related Weaknesses
- ChildOf: CWE-1164
- ChildOf: CWE-20

## Common Consequences
- Scope: Other; Impact: Other — It is critically important that validation logic be maintained and kept in sync with the rest of the application. Unchecked input is the root cause of some of today's worst and most common software security problems. Cross-site scripting, SQL injection, and process control vulnerabilities all stem from incomplete or absent input validation.

## Detection Methods
- [Automated Static Analysis] To find the issue in the implementation, manual checks or automated static analysis could be applied to the XML configuration files.
- [Manual Static Analysis] To find the issue in the implementation, manual checks or automated static analysis could be applied to the XML configuration files.

## Demonstrative Examples (summary)
- This example shows an inconsistency between an action form and a validation form. with a third field.
