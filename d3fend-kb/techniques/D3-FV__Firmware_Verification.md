# D3-FV: Firmware Verification

**Reference:** https://d3fend.mitre.org/technique/D3-FV/  

## Definition
Cryptographically verifying firmware integrity.

## Parent Class(es)
- Platform Monitoring

## Relationships
- **kb-reference:** Reference - Firmware Verification Eclypsium
- **kb-reference:** Reference - Firmware Verification Trapezoid
- **kb-reference:** Reference - Platform Firmware Resiliency Guidelines - NIST
- **verifies:** Firmware

## Knowledge Base Article
## How it works
Cryptographic hash values are computed for system and peripheral firmware. The hash values are compared against precomputed hash values for the identified firmware. A hash value mismatch may indicate that the firmware may have been tampered with or updated with a non-current release indicating a misconfiguration for the system.

## Considerations
* Requires cryptographically computed hash values of firmware
* Requires storage of precomputed firmware hash values
