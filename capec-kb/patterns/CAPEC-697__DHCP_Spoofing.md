# CAPEC-697: DHCP Spoofing

**Abstraction:** Standard  
**Status:** Stable  
**Likelihood of Attack:** Low  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/697.html  

## Description
An adversary masquerades as a legitimate Dynamic Host Configuration Protocol (DHCP) server by spoofing DHCP traffic, with the goal of redirecting network traffic or denying service to DHCP.

## Related Attack Patterns
- ChildOf: CAPEC-194
- CanPrecede: CAPEC-158
- CanPrecede: CAPEC-94

## Prerequisites
- The adversary must have access to a machine within the target LAN which can send DHCP offers to the target.

## Skills Required
- [Medium] The adversary must identify potential targets for DHCP Spoofing and craft network configurations to obtain the desired results.

## Resources Required
- The adversary requires access to a machine within the target LAN on a network which does not secure its DHCP traffic through MAC-Forced Forwarding, port security, etc.

## Consequences
- Scope: Confidentiality, Access Control; Impact: Read Data
- Scope: Integrity, Access Control; Impact: Modify Data, Execute Unauthorized Commands
- Scope: Availability; Impact: Resource Consumption

## Mitigations
- Design: MAC-Forced Forwarding
- Implementation: Port Security and DHCP snooping
- Implementation: Network-based Intrusion Detection Systems

## Related Weaknesses (CWE)
- CWE-923
