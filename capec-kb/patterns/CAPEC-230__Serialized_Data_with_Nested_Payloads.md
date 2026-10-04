# CAPEC-230: Serialized Data with Nested Payloads

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/230.html  

## Description
Applications often need to transform data in and out of a data format (e.g., XML and YAML) by using a parser. It may be possible for an adversary to inject data that may have an adverse effect on the parser when it is being processed. Many data format languages allow the definition of macro-like structures that can be used to simplify the creation of complex structures. By nesting these structures, causing the data to be repeatedly substituted, an adversary can cause the parser to consume more resources while processing, causing excessive memory consumption and CPU utilization.

## Related Attack Patterns
- ChildOf: CAPEC-130

## Prerequisites
- An application's user-controllable data is expressed in a language that supports subsitution.
- An application does not perform sufficient validation to ensure that user-controllable data is not malicious.

## Consequences
- Scope: Availability; Impact: Resource Consumption
- Scope: Confidentiality; Impact: Read Data
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges

## Mitigations
- Carefully validate and sanitize all user-controllable data prior to passing it to the data parser routine. Ensure that the resultant data is safe to pass to the data parser.
- Perform validation on canonical data.
- Pick a robust implementation of the data parser.

## Related Weaknesses (CWE)
- CWE-112
- CWE-20
- CWE-674
- CWE-770
