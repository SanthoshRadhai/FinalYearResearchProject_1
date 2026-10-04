# CAPEC-306: TCP Window Scan

**Abstraction:** Detailed  
**Status:** Stable  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/306.html  

## Description
An adversary engages in TCP Window scanning to analyze port status and operating system type. TCP Window scanning uses the ACK scanning method but examine the TCP Window Size field of response RST packets to make certain inferences. While TCP Window Scans are fast and relatively stealthy, they work against fewer TCP stack implementations than any other type of scan. Some operating systems return a positive TCP window size when a RST packet is sent from an open port, and a negative value when the RST originates from a closed port. TCP Window scanning is one of the most complex scan types, and its results are difficult to interpret. Window scanning alone rarely yields useful information, but when combined with other types of scanning is more useful. It is a generally more reliable means of making inference about operating system versions than port status.

## Related Attack Patterns
- ChildOf: CAPEC-300

## Prerequisites
- TCP Window scanning requires the use of raw sockets, and thus cannot be performed from some Windows systems (Windows XP SP 2, for example). On Unix and Linux, raw socket manipulations require root privileges.

## Resources Required
- The ability to send TCP segments with a custom window size to a host during network reconnaissance. This can be achieved via the use of a network mapper or scanner, or via raw socket programming in a scripting language. Packet injection tools are also useful for this purpose. Depending upon the method used it may be necessary to sniff the network in order to see the response.

## Consequences
- Scope: Confidentiality; Impact: Other
- Scope: Confidentiality, Access Control, Authorization; Impact: Bypass Protection Mechanism, Hide Activities

## Related Weaknesses (CWE)
- CWE-200
