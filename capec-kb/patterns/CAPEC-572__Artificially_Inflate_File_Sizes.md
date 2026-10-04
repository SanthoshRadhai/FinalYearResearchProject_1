# CAPEC-572: Artificially Inflate File Sizes

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/572.html  

## Description
An adversary modifies file contents by adding data to files for several reasons. Many different attacks could “follow” this pattern resulting in numerous outcomes. Adding data to a file could also result in a Denial of Service condition for devices with limited storage capacity.

## Related Attack Patterns
- ChildOf: CAPEC-165

## Consequences
- Scope: Availability; Impact: Resource Consumption
- Scope: Integrity; Impact: Modify Data
