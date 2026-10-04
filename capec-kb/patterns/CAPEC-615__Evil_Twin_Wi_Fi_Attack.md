# CAPEC-615: Evil Twin Wi-Fi Attack

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/615.html  

## Description
Adversaries install Wi-Fi equipment that acts as a legitimate Wi-Fi network access point. When a device connects to this access point, Wi-Fi data traffic is intercepted, captured, and analyzed. This also allows the adversary to use "adversary-in-the-middle" (CAPEC-94) for all communications.

## Related Attack Patterns
- ChildOf: CAPEC-616

## Prerequisites
- None

## Consequences
- Scope: Confidentiality; Impact: Read Data

## Mitigations
- Commercial defensive technology that monitors for rogue Wi-Fi access points, adversary-in-the-middle attacks, and anomalous activity with the mobile device baseband radios.

## Related Weaknesses (CWE)
- CWE-300
