# CAPEC-662: Adversary in the Browser (AiTB)

**Abstraction:** Standard  
**Status:** Stable  
**Likelihood of Attack:** High  
**Typical Severity:** Very High  
**Reference:** https://capec.mitre.org/data/definitions/662.html  

## Description
An adversary exploits security vulnerabilities or inherent functionalities of a web browser, in order to manipulate traffic between two endpoints.

## Related Attack Patterns
- ChildOf: CAPEC-94

## Prerequisites
- The adversary must install or convince a user to install a Trojan.
- There are two components communicating with each other.
- An attacker is able to identify the nature and mechanism of communication between the two target components.
- Strong mutual authentication is not used between the two target components yielding opportunity for adversarial interposition.
- For browser pivoting, the SeDebugPrivilege and a high-integrity process must both exist to execute this attack.

## Skills Required
- [Medium] Tricking the victim into installing the Trojan is often the most difficult aspect of this attack. Afterwards, the remainder of this attack is fairly trivial.

## Consequences
- Scope: Integrity; Impact: Modify Data
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges
- Scope: Confidentiality; Impact: Read Data

## Mitigations
- Ensure software and applications are only downloaded from legitimate and reputable sources, in addition to conducting integrity checks on the downloaded component.
- Leverage anti-malware tools, which can detect Trojan Horse malware.
- Use strong, out-of-band mutual authentication to always fully authenticate both ends of any communications channel.
- Limit user permissions to prevent browser pivoting.
- Ensure browser sessions are regularly terminated and when their effective lifetime ends.

## Related Weaknesses (CWE)
- CWE-300
- CWE-494
