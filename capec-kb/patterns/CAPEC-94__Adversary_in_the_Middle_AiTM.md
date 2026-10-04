# CAPEC-94: Adversary in the Middle (AiTM)

**Abstraction:** Meta  
**Status:** Stable  
**Likelihood of Attack:** High  
**Typical Severity:** Very High  
**Reference:** https://capec.mitre.org/data/definitions/94.html  

## Description
An adversary targets the communication between two components (typically client and server), in order to alter or obtain data from transactions. A general approach entails the adversary placing themself within the communication channel between the two components.

## Related Attack Patterns
- CanPrecede: CAPEC-151
- CanPrecede: CAPEC-668

## Prerequisites
- There are two components communicating with each other.
- An attacker is able to identify the nature and mechanism of communication between the two target components.
- An attacker can eavesdrop on the communication between the target components.
- Strong mutual authentication is not used between the two target components yielding opportunity for attacker interposition.
- The communication occurs in clear (not encrypted) or with insufficient and spoofable encryption.

## Skills Required
- [Medium] This attack can get sophisticated since the attack may use cryptography.

## Consequences
- Scope: Integrity; Impact: Modify Data
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges
- Scope: Confidentiality; Impact: Read Data

## Mitigations
- Ensure Public Keys are signed by a Certificate Authority
- Encrypt communications using cryptography (e.g., SSL/TLS)
- Use Strong mutual authentication to always fully authenticate both ends of any communications channel.
- Exchange public keys using a secure channel

## Related Weaknesses (CWE)
- CWE-300
- CWE-290
- CWE-593
- CWE-287
- CWE-294
