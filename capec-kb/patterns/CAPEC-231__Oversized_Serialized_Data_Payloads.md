# CAPEC-231: Oversized Serialized Data Payloads

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/231.html  

## Description
An adversary injects oversized serialized data payloads into a parser during data processing to produce adverse effects upon the parser such as exhausting system resources and arbitrary code execution.

## Related Attack Patterns
- ChildOf: CAPEC-130

## Prerequisites
- An application uses an parser for serialized data to perform transformation on user-controllable data.
- An application does not perform sufficient validation to ensure that user-controllable data is safe for a data parser.

## Skills Required
- [Low] Denial of service
- [High] Arbitrary code execution

## Consequences
- Scope: Availability; Impact: Resource Consumption
- Scope: Confidentiality; Impact: Read Data
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges

## Mitigations
- Carefully validate and sanitize all user-controllable serialized data prior to passing it to the parser routine. Ensure that the resultant data is safe to pass to the parser.
- Perform validation on canonical data.
- Pick a robust implementation of the serialized data parser.
- Validate data against a valid schema or DTD prior to parsing.

## Related Weaknesses (CWE)
- CWE-112
- CWE-20
- CWE-674
- CWE-770
