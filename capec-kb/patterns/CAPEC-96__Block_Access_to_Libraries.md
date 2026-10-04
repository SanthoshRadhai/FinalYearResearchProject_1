# CAPEC-96: Block Access to Libraries

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Medium  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/96.html  

## Description
An application typically makes calls to functions that are a part of libraries external to the application. These libraries may be part of the operating system or they may be third party libraries. It is possible that the application does not handle situations properly where access to these libraries has been blocked. Depending on the error handling within the application, blocked access to libraries may leave the system in an insecure state that could be leveraged by an attacker.

## Related Attack Patterns
- ChildOf: CAPEC-603

## Prerequisites
- An application requires access to external libraries.
- An attacker has the privileges to block application access to external libraries.

## Skills Required
- [Low] Knowledge of how to block access to libraries, as well as knowledge of how to leverage the resulting state of the application based on the failed call.

## Consequences
- Scope: Availability; Impact: Alter Execution Logic
- Scope: Confidentiality; Impact: Other
- Scope: Confidentiality, Access Control, Authorization; Impact: Bypass Protection Mechanism

## Mitigations
- Ensure that application handles situations where access to APIs in external libraries is not available securely. If the application cannot continue its execution safely it should fail in a consistent and secure fashion.

## Related Weaknesses (CWE)
- CWE-589
