# CAPEC-617: Cellular Rogue Base Station

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/617.html  

## Description
In this attack scenario, the attacker imitates a cellular base station with their own "rogue" base station equipment. Since cellular devices connect to whatever station has the strongest signal, the attacker can easily convince a targeted cellular device (e.g. the retransmission device) to talk to the rogue base station.

## Related Attack Patterns
- ChildOf: CAPEC-616

## Prerequisites
- None

## Skills Required
- [Low] This technique has been demonstrated by amateur hackers and commercial tools and open source projects are available to automate the attack.

## Consequences
- Scope: Confidentiality; Impact: Read Data

## Mitigations
- Passively monitor cellular network connection for real-time threat detection and logging for manual review.
