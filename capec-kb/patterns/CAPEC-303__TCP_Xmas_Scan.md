# CAPEC-303: TCP Xmas Scan

**Abstraction:** Detailed  
**Status:** Stable  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/303.html  

## Description
An adversary uses a TCP XMAS scan to determine if ports are closed on the target machine. This scan type is accomplished by sending TCP segments with all possible flags set in the packet header, generating packets that are illegal based on RFC 793. The RFC 793 expected behavior is that any TCP segment with an out-of-state Flag sent to an open port is discarded, whereas segments with out-of-state flags sent to closed ports should be handled with a RST in response. This behavior should allow an attacker to scan for closed ports by sending certain types of rule-breaking packets (out of sync or disallowed by the TCB) and detect closed ports via RST packets.

## Related Attack Patterns
- ChildOf: CAPEC-300

## Prerequisites
- The adversary needs logical access to the target network. XMAS scanning requires the use of raw sockets, and thus cannot be performed from some Windows systems (Windows XP SP 2, for example). On Unix and Linux, raw socket manipulations require root privileges.

## Resources Required
- This attack can be carried out with a network mapper or scanner, or via raw socket programming in a scripting language. Packet injection tools are also useful for this purpose. Depending upon the method used it may be necessary to sniff the network in order to see the response.

## Consequences
- Scope: Confidentiality; Impact: Other
- Scope: Confidentiality, Access Control, Authorization; Impact: Bypass Protection Mechanism, Hide Activities
- Scope: Availability; Impact: Unreliable Execution

## Mitigations
- Employ a robust network defensive posture that includes a managed IDS/IPS.

## Related Weaknesses (CWE)
- CWE-200
