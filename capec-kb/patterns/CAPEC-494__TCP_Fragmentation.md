# CAPEC-494: TCP Fragmentation

**Abstraction:** Standard  
**Status:** Draft  
**Reference:** https://capec.mitre.org/data/definitions/494.html  

## Description
An adversary may execute a TCP Fragmentation attack against a target with the intention of avoiding filtering rules of network controls, by attempting to fragment the TCP packet such that the headers flag field is pushed into the second fragment which typically is not filtered.

## Related Attack Patterns
- ChildOf: CAPEC-130

## Prerequisites
- This type of an attack requires the target system to be running a vulnerable implementation of IP, and the adversary needs to ability to send TCP packets of arbitrary size with crafted data.

## Mitigations
- This attack may be mitigated by enforcing rules at the router following the guidance of RFC1858. The essential part of the guidance is creating the following rule "IF FO=1 and PROTOCOL=TCP then DROP PACKET" as this mitigated both tiny fragment and overlapping fragment attacks in IPv4. In IPv6 overlapping(RFC5722) additional steps may be required such as deep packet inspection. The delayed fragments may be mitigated by enforcing a timeout on the transmission to receive all packets by a certain time since the first packet is received. According to RFC2460 IPv6 implementations should enforce a rule to discard all fragments if the fragments are not ALL received within 60 seconds of the FIRST arriving fragment.

## Related Weaknesses (CWE)
- CWE-770
- CWE-404
