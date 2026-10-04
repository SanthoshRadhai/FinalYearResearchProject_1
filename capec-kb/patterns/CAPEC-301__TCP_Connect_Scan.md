# CAPEC-301: TCP Connect Scan

**Abstraction:** Detailed  
**Status:** Stable  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/301.html  

## Description
An adversary uses full TCP connection attempts to determine if a port is open on the target system. The scanning process involves completing a 'three-way handshake' with a remote port, and reports the port as closed if the full handshake cannot be established. An advantage of TCP connect scanning is that it works against any TCP/IP stack.

## Related Attack Patterns
- ChildOf: CAPEC-300

## Prerequisites
- The adversary requires logical access to the target network. The TCP connect Scan requires the ability to connect to an available port and complete a 'three-way-handshake' This scanning technique does not require any special privileges in order to perform. This type of scan works against all TCP/IP stack implementations.

## Resources Required
- The adversary can leverage a network mapper or scanner, or perform this attack via routine socket programming in a scripting language. Packet injection tools are also useful for this purpose. Depending upon the method used it may be necessary to sniff the network to see the response.

## Consequences
- Scope: Confidentiality; Impact: Read Data

## Mitigations
- Employ a robust network defense posture that includes an IDS/IPS system.

## Related Weaknesses (CWE)
- CWE-200
