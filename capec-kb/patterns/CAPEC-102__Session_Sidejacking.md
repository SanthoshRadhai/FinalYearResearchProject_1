# CAPEC-102: Session Sidejacking

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/102.html  

## Description
Session sidejacking takes advantage of an unencrypted communication channel between a victim and target system. The attacker sniffs traffic on a network looking for session tokens in unencrypted traffic. Once a session token is captured, the attacker performs malicious actions by using the stolen token with the targeted application to impersonate the victim. This attack is a specific method of session hijacking, which is exploiting a valid session token to gain unauthorized access to a target system or information. Other methods to perform a session hijacking are session fixation, cross-site scripting, or compromising a user or server machine and stealing the session token.

## Related Attack Patterns
- ChildOf: CAPEC-593

## Prerequisites
- An attacker and the victim are both using the same WiFi network.
- The victim has an active session with a target system.
- The victim is not using a secure channel to communicate with the target system (e.g. SSL, VPN, etc.)
- The victim initiated communication with a target system that requires transfer of the session token or the target application uses AJAX and thereby periodically "rings home" asynchronously using the session token

## Skills Required
- [Low] Easy to use tools exist to automate this attack.

## Resources Required
- A packet sniffing tool, such as wireshark, can be used to capture session information.

## Consequences
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges
- Scope: Integrity; Impact: Modify Data
- Scope: Confidentiality; Impact: Read Data
- Scope: Availability; Impact: Unreliable Execution

## Mitigations
- Make sure that HTTPS is used to communicate with the target system. Alternatively, use VPN if possible. It is important to ensure that all communication between the client and the server happens via an encrypted secure channel.
- Modify the session token with each transmission and protect it with cryptography. Add the idea of request sequencing that gives the server an ability to detect replay attacks.

## Related Weaknesses (CWE)
- CWE-294
- CWE-522
- CWE-523
- CWE-319
- CWE-614
