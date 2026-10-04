# CWE-1193: Power-On of Untrusted Execution Core Before Enabling Fabric Access Control

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/1193.html  

## Description
The product enables components that contain untrusted firmware before memory and fabric access controls have been enabled.

## Extended Description
After initial reset, System-on-Chip (SoC) fabric access controls and other security features need to be programmed by trusted firmware as part of the boot sequence. If untrusted IPs or peripheral microcontrollers are enabled first, then the untrusted component can master transactions on the hardware bus and target memory or other assets to compromise the SoC boot firmware.

## Related Weaknesses
- ChildOf: CWE-696

## Common Consequences
- Scope: Access Control; Impact: Bypass Protection Mechanism — An untrusted component can master transactions on the HW bus and target memory or other assets to compromise the SoC boot firmware.

## Potential Mitigations
- [Architecture and Design] The boot sequence should enable fabric access controls and memory protections before enabling third-party hardware IPs and peripheral microcontrollers that use untrusted firmware.
