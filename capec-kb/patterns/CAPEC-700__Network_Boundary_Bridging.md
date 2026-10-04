# CAPEC-700: Network Boundary Bridging

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/700.html  

## Description
An adversary which has gained elevated access to network boundary devices may use these devices to create a channel to bridge trusted and untrusted networks. Boundary devices do not necessarily have to be on the network’s edge, but rather must serve to segment portions of the target network the adversary wishes to cross into.

## Related Attack Patterns
- ChildOf: CAPEC-161
- CanFollow: CAPEC-70
- CanFollow: CAPEC-560

## Prerequisites
- The adversary must have control of a network boundary device.

## Skills Required
- [Medium] The adversary must understand how to manage the target network device to create or edit policies which will bridge networks.

## Resources Required
- The adversary requires either high privileges or full control of a boundary device on a target network.

## Consequences
- Scope: Confidentiality, Access Control; Impact: Read Data, Bypass Protection Mechanism
- Scope: Integrity, Authorization; Impact: Alter Execution Logic, Hide Activities

## Mitigations
- Design: Ensure network devices are storing credentials in encrypted stores
- Design: Follow the principle of least privilege and restrict administrative duties to as few accounts as possible. Ensure these privileged accounts are secured with strong credentials which do not overlap with other network devices.
- Configuration: When possible, configure network boundary devices to use MFA.
- Configuration: Change the default configuration for network devices to harden their security profiles. Default configurations are often enabled with insecure features to allow ease of installation and management. However, these configurations can be easily discovered and exploited by adversaries.
- Implementation: Perform integrity checks on audit logs for network device management and review them to identify abnormalities in configurations.
- Implementation: Prevent network boundary devices from being physically accessed by unauthorized personnel to prevent tampering.
