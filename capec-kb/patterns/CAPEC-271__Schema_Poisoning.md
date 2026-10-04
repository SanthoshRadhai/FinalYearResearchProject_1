# CAPEC-271: Schema Poisoning

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/271.html  

## Description
An adversary corrupts or modifies the content of a schema for the purpose of undermining the security of the target. Schemas provide the structure and content definitions for resources used by an application. By replacing or modifying a schema, the adversary can affect how the application handles or interprets a resource, often leading to possible denial of service, entering into an unexpected state, or recording incomplete data.

## Related Attack Patterns
- ChildOf: CAPEC-176
- CanFollow: CAPEC-94

## Prerequisites
- Some level of access to modify the target schema.
- The schema used by the target application must be improperly secured against unauthorized modification and manipulation.

## Resources Required
- Access to the schema and the knowledge and ability modify it. Ability to replace or redirect access to the modified schema.

## Consequences
- Scope: Availability; Impact: Unreliable Execution, Resource Consumption
- Scope: Integrity; Impact: Modify Data
- Scope: Confidentiality; Impact: Read Data

## Mitigations
- Design: Protect the schema against unauthorized modification.
- Implementation: For applications that use a known schema, use a local copy or a known good repository instead of the schema reference supplied in the schema document.
- Implementation: For applications that leverage remote schemas, use the HTTPS protocol to prevent modification of traffic in transit and to avoid unauthorized modification.

## Related Weaknesses (CWE)
- CWE-15
