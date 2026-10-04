# CAPEC-559: Orbital Jamming

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/559.html  

## Description
In this attack pattern, the adversary sends disruptive signals at a target satellite using a rogue uplink station to disrupt the intended transmission. Those within the satellite's footprint are prevented from reaching the satellite's targeted or neighboring channels. The satellite's footprint size depends upon its position in the sky; higher orbital satellites cover multiple continents.

## Related Attack Patterns
- ChildOf: CAPEC-601

## Prerequisites
- This attack requires the knowledge of the satellite's coordinates for targeting.

## Resources Required
- A satellite uplink station.

## Consequences
- Scope: Availability; Impact: Other
