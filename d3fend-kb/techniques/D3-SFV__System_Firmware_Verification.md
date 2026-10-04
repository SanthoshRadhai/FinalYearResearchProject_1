# D3-SFV: System Firmware Verification

**Reference:** https://d3fend.mitre.org/technique/D3-SFV/  

## Definition
Cryptographically verifying installed system firmware integrity.

## Parent Class(es)
- Firmware Verification

## Relationships
- **kb-reference:** Reference - Firmware Verification Eclypsium
- **kb-reference:** Reference - Platform Firmware Resiliency Guidelines - NIST
- **verifies:** System Firmware

## Knowledge Base Article
## How it works
Cryptographic hash values are computed for system firmware. The hash values are compared against precomputed firmware hash values to determine if the firmware has been tampered with.

When system firmware verification fails a set of predefined responses is typically invoked. The responses may direct the system to disable some devices or operations.

## Considerations
* Requires the use of system provided security modules
* Secure hash values will need to be computed for firmware
