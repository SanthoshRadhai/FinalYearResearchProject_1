# CAPEC-619: Signal Strength Tracking

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/619.html  

## Description
In this attack scenario, the attacker passively monitors the signal strength of the target’s cellular RF signal or WiFi RF signal and uses the strength of the signal (with directional antennas and/or from multiple listening points at once) to identify the source location of the signal. Obtaining the signal of the target can be accomplished through multiple techniques such as through Cellular Broadcast Message Request or through the use of IMSI Tracking or WiFi MAC Address Tracking.

## Related Attack Patterns
- ChildOf: CAPEC-292

## Skills Required
- [Low] Commercial tools are available.

## Related Weaknesses (CWE)
- CWE-201
