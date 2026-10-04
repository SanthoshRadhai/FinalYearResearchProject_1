# CAPEC-583: Disabling Network Hardware

**Abstraction:** Detailed  
**Status:** Draft  
**Reference:** https://capec.mitre.org/data/definitions/583.html  

## Description
In this attack pattern, an adversary physically disables networking hardware by powering it down or disconnecting critical equipment. Disabling or shutting off critical system resources prevents them from performing their service as intended, which can have direct and indirect consequences on other systems. This attack pattern is considerably less technical than the selective blocking used in most obstruction attacks.

## Related Attack Patterns
- ChildOf: CAPEC-582

## Prerequisites
- The adversary requires physical access to the targeted communications equipment (networking devices, cables, etc.), which may be spread over a wide area.

## Consequences
- Scope: Availability; Impact: Other

## Mitigations
- Ensure rigorous physical defensive measures to keep the adversary from accessing critical systems..
