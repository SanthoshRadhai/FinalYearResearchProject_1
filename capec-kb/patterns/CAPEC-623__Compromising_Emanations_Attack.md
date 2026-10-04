# CAPEC-623: Compromising Emanations Attack

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/623.html  

## Description
Compromising Emanations (CE) are defined as unintentional signals which an attacker may intercept and analyze to disclose the information processed by the targeted equipment. Commercial mobile devices and retransmission devices have displays, buttons, microchips, and radios that emit mechanical emissions in the form of sound or vibrations. Capturing these emissions can help an adversary understand what the device is doing.

## Related Attack Patterns
- ChildOf: CAPEC-189

## Prerequisites
- Proximal access to the device.

## Skills Required
- [High] Sophisticated attack.

## Consequences
- Scope: Confidentiality; Impact: Read Data

## Mitigations
- None are known.

## Related Weaknesses (CWE)
- CWE-201
