# CAPEC-195: Principal Spoof

**Abstraction:** Standard  
**Status:** Draft  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/195.html  

## Description
A Principal Spoof is a form of Identity Spoofing where an adversary pretends to be some other person in an interaction. This is often accomplished by crafting a message (either written, verbal, or visual) that appears to come from a person other than the adversary. Phishing and Pharming attacks often attempt to do this so that their attempts to gather sensitive information appear to come from a legitimate source. A Principal Spoof does not use stolen or spoofed authentication credentials, instead relying on the appearance and content of the message to reflect identity.

## Related Attack Patterns
- ChildOf: CAPEC-151

## Prerequisites
- The target must associate data or activities with a person's identity and the adversary must be able to modify this identity without detection.

## Resources Required
- None: No specialized resources are required to execute this type of attack.
