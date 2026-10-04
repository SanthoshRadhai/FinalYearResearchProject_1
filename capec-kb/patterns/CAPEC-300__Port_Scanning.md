# CAPEC-300: Port Scanning

**Abstraction:** Standard  
**Status:** Stable  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/300.html  

## Description
An adversary uses a combination of techniques to determine the state of the ports on a remote target. Any service or application available for TCP or UDP networking will have a port open for communications over the network.

## Related Attack Patterns
- ChildOf: CAPEC-169

## Prerequisites
- The adversary requires logical access to the target's network in order to carry out this type of attack.

## Resources Required
- The adversary requires a network mapping/scanning tool, or must conduct socket programming on the command line. Packet injection tools are also useful for this purpose. Depending upon the method used it may be necessary to sniff the network in order to see the response.

## Consequences
- Scope: Confidentiality; Impact: Other
- Scope: Confidentiality, Access Control, Authorization; Impact: Bypass Protection Mechanism, Hide Activities

## Related Weaknesses (CWE)
- CWE-200
