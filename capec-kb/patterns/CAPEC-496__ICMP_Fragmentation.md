# CAPEC-496: ICMP Fragmentation

**Abstraction:** Standard  
**Status:** Draft  
**Reference:** https://capec.mitre.org/data/definitions/496.html  

## Description
An attacker may execute a ICMP Fragmentation attack against a target with the intention of consuming resources or causing a crash. The attacker crafts a large number of identical fragmented IP packets containing a portion of a fragmented ICMP message. The attacker these sends these messages to a target host which causes the host to become non-responsive. Another vector may be sending a fragmented ICMP message to a target host with incorrect sizes in the header which causes the host to hang.

## Related Attack Patterns
- ChildOf: CAPEC-130

## Prerequisites
- This type of an attack requires the target system to be running a vulnerable implementation of IP, and the attacker needs to ability to send arbitrary sized ICMP packets to the target.

## Mitigations
- This attack may be mitigated through egress filtering based on ICMP payload so a network is a "good neighbor" to other networks. Bad IP implementations become patched, so using the proper version of a browser or OS is recommended.

## Related Weaknesses (CWE)
- CWE-770
- CWE-404
