# CAPEC-146: XML Schema Poisoning

**Abstraction:** Detailed  
**Status:** Stable  
**Likelihood of Attack:** Low  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/146.html  

## Description
An adversary corrupts or modifies the content of XML schema information passed between a client and server for the purpose of undermining the security of the target. XML Schemas provide the structure and content definitions for XML documents. Schema poisoning is the ability to manipulate a schema either by replacing or modifying it to compromise the programs that process documents that use this schema.

## Related Attack Patterns
- ChildOf: CAPEC-271

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
- Implementation: For applications that use a known schema, use a local copy or a known good repository instead of the schema reference supplied in the XML document. Additionally, ensure that the proper permissions are set on local files to avoid unauthorized modification.
- Implementation: For applications that leverage remote schemas, use the HTTPS protocol to prevent modification of traffic in transit and to avoid unauthorized modification.

## Related Weaknesses (CWE)
- CWE-15
- CWE-472
