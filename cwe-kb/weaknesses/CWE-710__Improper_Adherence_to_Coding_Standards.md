# CWE-710: Improper Adherence to Coding Standards

**Abstraction:** Pillar  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/710.html  

## Description
The product does not follow certain coding rules for development, which can lead to resultant weaknesses or increase the severity of the associated vulnerabilities.

## Common Consequences
- Scope: Other; Impact: Other

## Potential Mitigations
- [Policy] Select and require coding standards. Ensure that they include security concerns.
- [Implementation] Closely follow coding standards, possibly enforcing them upon checkin of the code into a source control system or with periodic analyses.

## Detection Methods
- [Automated Static Analysis] Automated tools can detect violations of many code standards.
