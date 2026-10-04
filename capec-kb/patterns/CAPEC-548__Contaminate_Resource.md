# CAPEC-548: Contaminate Resource

**Abstraction:** Meta  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/548.html  

## Description
An adversary contaminates organizational information systems (including devices and networks) by causing them to handle information of a classification/sensitivity for which they have not been authorized. When this happens, the contaminated information system, device, or network must be brought offline to investigate and mitigate the data spill, which denies availability of the system until the investigation is complete.

## Related Attack Patterns
- CanPrecede: CAPEC-607

## Prerequisites
- The adversary needs to have real or fake classified/sensitive information to place on a system

## Skills Required
- [Low] Knowledge of classification levels of systems
- [High] The ability to obtain a classified document or information
- [Low] The ability to fake a classified document

## Consequences
- Scope: Availability; Impact: Resource Consumption
- Scope: Confidentiality; Impact: Read Data

## Mitigations
- Properly safeguard classified/sensitive data. This includes training cleared individuals to ensure they are handling and disposing of this data properly, as well as ensuring systems only handle information of the classification level they are designed for.
- Design systems with redundancy in mind. This could mean creating backing servers that could be switched over to in the event that a server has to be taken down for investigation.
- Have a planned and efficient response plan to limit the amount of time a system is offline while the contamination is investigated.
