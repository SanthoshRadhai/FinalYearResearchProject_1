# CAPEC-701: Browser in the Middle (BiTM)

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/701.html  

## Description
An adversary exploits the inherent functionalities of a web browser, in order to establish an unnoticed remote desktop connection in the victim's browser to the adversary's system. The adversary must deploy a web client with a remote desktop session that the victim can access.

## Related Attack Patterns
- ChildOf: CAPEC-94
- CanPrecede: CAPEC-151
- CanPrecede: CAPEC-148
- CanFollow: CAPEC-98

## Prerequisites
- The adversary must create a convincing web client to establish the connection. The victim then needs to be lured onto the adversary's webpage. In addition, the victim's machine must not use local authentication APIs, a hardware token, or a Trusted Platform Module (TPM) to authenticate.

## Resources Required
- A web application with a client is needed to enable the victim's browser to establish a remote desktop connection to the system of the adversary.

## Consequences
- Scope: Confidentiality, Access Control, Authentication; Impact: Gain Privileges
- Scope: Confidentiality, Authorization; Impact: Read Data
- Scope: Integrity; Impact: Modify Data

## Mitigations
- Implementation: Use strong, mutual authentication to fully authenticate with both ends of any communications channel

## Related Weaknesses (CWE)
- CWE-294
- CWE-345
