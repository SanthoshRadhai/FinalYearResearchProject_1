# CAPEC-612: WiFi MAC Address Tracking

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/612.html  

## Description
In this attack scenario, the attacker passively listens for WiFi messages and logs the associated Media Access Control (MAC) addresses. These addresses are intended to be unique to each wireless device (although they can be configured and changed by software). Once the attacker is able to associate a MAC address with a particular user or set of users (for example, when attending a public event), the attacker can then scan for that MAC address to track that user in the future.

## Related Attack Patterns
- ChildOf: CAPEC-292

## Prerequisites
- None

## Skills Required
- [Low] Open source and commercial software tools are available and several commercial advertising companies routinely set up tools to collect and monitor MAC addresses.

## Mitigations
- Automatic randomization of WiFi MAC addresses
- Frequent changing of handset and retransmission device

## Related Weaknesses (CWE)
- CWE-201
- CWE-300
