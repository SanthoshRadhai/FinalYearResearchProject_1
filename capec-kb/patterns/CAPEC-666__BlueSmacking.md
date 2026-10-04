# CAPEC-666: BlueSmacking

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** Medium  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/666.html  

## Description
An adversary uses Bluetooth flooding to transfer large packets to Bluetooth enabled devices over the L2CAP protocol with the goal of creating a DoS. This attack must be carried out within close proximity to a Bluetooth enabled device.

## Related Attack Patterns
- ChildOf: CAPEC-125

## Prerequisites
- The system/application has Bluetooth enabled.

## Skills Required
- [Low] An adversary only needs a Linux machine along with a Bluetooth adapter, which is extremely common.

## Consequences
- Scope: Availability; Impact: Unreliable Execution, Resource Consumption

## Mitigations
- Disable Bluetooth when not being used.
- When using Bluetooth, set it to hidden or non-discoverable mode.

## Related Weaknesses (CWE)
- CWE-404
