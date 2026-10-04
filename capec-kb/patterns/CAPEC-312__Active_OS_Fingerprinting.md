# CAPEC-312: Active OS Fingerprinting

**Abstraction:** Standard  
**Status:** Stable  
**Likelihood of Attack:** Medium  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/312.html  

## Description
An adversary engages in activity to detect the operating system or firmware version of a remote target by interrogating a device, server, or platform with a probe designed to solicit behavior that will reveal information about the operating systems or firmware in the environment. Operating System detection is possible because implementations of common protocols (Such as IP or TCP) differ in distinct ways. While the implementation differences are not sufficient to 'break' compatibility with the protocol the differences are detectable because the target will respond in unique ways to specific probing activity that breaks the semantic or logical rules of packet construction for a protocol. Different operating systems will have a unique response to the anomalous input, providing the basis to fingerprint the OS behavior. This type of OS fingerprinting can distinguish between operating system types and versions.

## Related Attack Patterns
- ChildOf: CAPEC-224

## Prerequisites
- The ability to monitor and interact with network communications.Access to at least one host, and the privileges to interface with the network interface card.

## Resources Required
- Any type of active probing that involves non-standard packet headers requires the use of raw sockets, which is not available on particular operating systems (Microsoft Windows XP SP 2, for example). Raw socket manipulation on Unix/Linux requires root privileges. A tool capable of sending and receiving packets from a remote system.

## Consequences
- Scope: Confidentiality; Impact: Read Data
- Scope: Confidentiality, Access Control, Authorization; Impact: Hide Activities

## Related Weaknesses (CWE)
- CWE-200
