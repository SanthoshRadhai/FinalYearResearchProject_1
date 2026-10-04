# CAPEC-618: Cellular Broadcast Message Request

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/618.html  

## Description
In this attack scenario, the attacker uses knowledge of the target’s mobile phone number (i.e., the number associated with the SIM used in the retransmission device) to cause the cellular network to send broadcast messages to alert the mobile device. Since the network knows which cell tower the target’s mobile device is attached to, the broadcast messages are only sent in the Location Area Code (LAC) where the target is currently located. By triggering the cellular broadcast message and then listening for the presence or absence of that message, an attacker could verify that the target is in (or not in) a given location.

## Related Attack Patterns
- ChildOf: CAPEC-292

## Prerequisites
- The attacker must have knowledge of the target’s mobile phone number.

## Skills Required
- [Low] Open source and commercial tools are available for this attack.

## Consequences
- Scope: Other; Impact: Other

## Mitigations
- Frequent changing of mobile number.

## Related Weaknesses (CWE)
- CWE-201
