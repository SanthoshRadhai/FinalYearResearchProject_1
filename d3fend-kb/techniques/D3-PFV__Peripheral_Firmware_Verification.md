# D3-PFV: Peripheral Firmware Verification

**Reference:** https://d3fend.mitre.org/technique/D3-PFV/  

## Definition
Cryptographically verifying peripheral firmware integrity.

## Parent Class(es)
- Firmware Verification

## Relationships
- **kb-reference:** Reference - Firmware Verification Eclypsium
- **kb-reference:** Reference - Firmware Verification Trapezoid
- **verifies:** Peripheral Firmware

## Knowledge Base Article
# How it works
Peripheral firmware is collected and  analyzed on a host either periodically or on demand. This information may be collected for future comparisons.

Changes in firmware hash values may indicate that the firmware has been tampered with or that firmware images are not maintained to current baselined versions, or even known vulnerable versions are deployed.

## Considerations
* Trust baselines will need to be generated for specific devices
* Changes to trusted configurations will need to be managed across the enterprise
