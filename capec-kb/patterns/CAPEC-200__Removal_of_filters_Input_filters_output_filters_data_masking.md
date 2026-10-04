# CAPEC-200: Removal of filters: Input filters, output filters, data masking

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/200.html  

## Description
An attacker removes or disables filtering mechanisms on the target application. Input filters prevent invalid data from being sent to an application (for example, overly large inputs that might cause a buffer overflow or other malformed inputs that may not be correctly handled by an application). Input filters might also be designed to constrained executable content.

## Related Attack Patterns
- ChildOf: CAPEC-207

## Prerequisites
- The target application must utilize some sort of filtering mechanism (input, output, or data masking).

## Resources Required
- None: No specialized resources are required to execute this type of attack.
