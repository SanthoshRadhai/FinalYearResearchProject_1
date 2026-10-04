# CAPEC-224: Fingerprinting

**Abstraction:** Meta  
**Status:** Stable  
**Likelihood of Attack:** High  
**Typical Severity:** Very Low  
**Reference:** https://capec.mitre.org/data/definitions/224.html  

## Description
An adversary compares output from a target system to known indicators that uniquely identify specific details about the target. Most commonly, fingerprinting is done to determine operating system and application versions. Fingerprinting can be done passively as well as actively. Fingerprinting by itself is not usually detrimental to the target. However, the information gathered through fingerprinting often enables an adversary to discover existing weaknesses in the target.

## Prerequisites
- A means by which to interact with the target system directly.

## Skills Required
- [Medium] Some fingerprinting activity requires very specific knowledge of how different operating systems respond to various TCP/IP requests. Application fingerprinting can be as easy as envoking the application with the correct command line argument, or mouse clicking in the appropriate place on the screen.

## Resources Required
- If on a network, the adversary needs a tool capable of viewing network communications at the packet level and with header information, like Mitmproxy, Wireshark, or Fiddler.

## Consequences
- Scope: Confidentiality; Impact: Read Data

## Mitigations
- While some information is shared by systems automatically based on standards and protocols, remove potentially sensitive information that is not necessary for the application's functionality as much as possible.

## Related Weaknesses (CWE)
- CWE-200
