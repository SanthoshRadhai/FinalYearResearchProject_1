# CAPEC-610: Cellular Data Injection

**Abstraction:** Standard  
**Status:** Stable  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/610.html  

## Description
Adversaries inject data into mobile technology traffic (data flows or signaling data) to disrupt communications or conduct additional surveillance operations.

## Related Attack Patterns
- ChildOf: CAPEC-240

## Prerequisites
- None

## Skills Required
- [High] Often achieved by nation states in conjunction with commercial cellular providers to conduct cellular traffic intercept and possible traffic injection.

## Consequences
- Scope: Availability; Impact: Resource Consumption
- Scope: Availability; Impact: Modify Data

## Mitigations
- Commercial defensive technology to detect and alert to any attempts to modify mobile technology data flows or to inject new data into existing data flows and signaling data.
