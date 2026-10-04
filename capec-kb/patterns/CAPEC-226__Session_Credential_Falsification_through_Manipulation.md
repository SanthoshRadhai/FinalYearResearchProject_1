# CAPEC-226: Session Credential Falsification through Manipulation

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/226.html  

## Description
An attacker manipulates an existing credential in order to gain access to a target application. Session credentials allow users to identify themselves to a service after an initial authentication without needing to resend the authentication information (usually a username and password) with every message. An attacker may be able to manipulate a credential sniffed from an existing connection in order to gain access to a target server.

## Related Attack Patterns
- ChildOf: CAPEC-196

## Prerequisites
- The targeted application must use session credentials to identify legitimate users.

## Resources Required
- An attacker will need tools to sniff existing credentials (possibly their own) in order to retrieve a base credential for modification. They will need to understand how the components of the credential affect server behavior and how to manipulate this behavior by changing the credential. Finally, they will need tools to allow them to craft and transmit a modified credential.

## Related Weaknesses (CWE)
- CWE-565
- CWE-472
