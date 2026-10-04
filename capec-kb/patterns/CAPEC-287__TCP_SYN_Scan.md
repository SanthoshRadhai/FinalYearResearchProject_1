# CAPEC-287: TCP SYN Scan

**Abstraction:** Detailed  
**Status:** Stable  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/287.html  

## Description
An adversary uses a SYN scan to determine the status of ports on the remote target. SYN scanning is the most common type of port scanning that is used because of its many advantages and few drawbacks. As a result, novice attackers tend to overly rely on the SYN scan while performing system reconnaissance. As a scanning method, the primary advantages of SYN scanning are its universality and speed.

## Related Attack Patterns
- ChildOf: CAPEC-300

## Prerequisites
- This scan type is not possible with some operating systems (Windows XP SP 2). On Linux and Unix systems it requires root privileges to use raw sockets.

## Resources Required
- The ability to send TCP SYN segments to a host during network reconnaissance via the use of a network mapper or scanner, or via raw socket programming in a scripting language. Packet injection tools are also useful for this purpose. Depending upon the method used it may be necessary to sniff the network in order to see the response.

## Consequences
- Scope: Confidentiality; Impact: Other
- Scope: Confidentiality, Access Control, Authorization; Impact: Bypass Protection Mechanism, Hide Activities

## Related Weaknesses (CWE)
- CWE-200
