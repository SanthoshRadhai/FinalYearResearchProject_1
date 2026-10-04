# CWE-109: Struts: Validator Turned Off

**Abstraction:** Variant  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/109.html  

## Description
Automatic filtering via a Struts bean has been turned off, which disables the Struts Validator and custom validation logic. This exposes the application to other weaknesses related to insufficient input validation.

## Related Weaknesses
- ChildOf: CWE-1173
- ChildOf: CWE-20

## Common Consequences
- Scope: Access Control; Impact: Bypass Protection Mechanism

## Potential Mitigations
- [Implementation] Ensure that an action form mapping enables validation. Set the validate field to true.

## Demonstrative Examples (summary)
- This mapping defines an action for a download form:
