# CAPEC-134: Email Injection

**Abstraction:** Standard  
**Status:** Draft  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/134.html  

## Description
An adversary manipulates the headers and content of an email message by injecting data via the use of delimiter characters native to the protocol.

## Related Attack Patterns
- ChildOf: CAPEC-137

## Prerequisites
- The target application must allow the user to send email to some recipient, to specify the content at least one header field in the message, and must fail to sanitize against the injection of command separators.
- The adversary must have the ability to access the target mail application.

## Resources Required
- None: No specialized resources are required to execute this type of attack.

## Related Weaknesses (CWE)
- CWE-150
