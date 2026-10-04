# CAPEC-221: Data Serialization External Entities Blowup

**Abstraction:** Detailed  
**Status:** Draft  
**Reference:** https://capec.mitre.org/data/definitions/221.html  

## Description
This attack takes advantage of the entity replacement property of certain data serialization languages (e.g., XML, YAML, etc.) where the value of the replacement is a URI. A well-crafted file could have the entity refer to a URI that consumes a large amount of resources to create a denial of service condition. This can cause the system to either freeze, crash, or execute arbitrary code depending on the URI.

## Related Attack Patterns
- ChildOf: CAPEC-231
- ChildOf: CAPEC-278

## Prerequisites
- A server that has an implementation that accepts entities containing URI values.

## Consequences
- Scope: Availability; Impact: Resource Consumption
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands

## Mitigations
- This attack may be mitigated by tweaking the XML parser to not resolve external entities. If external entities are needed, then implement a custom XmlResolver that has a request timeout, data retrieval limit, and restrict resources it can retrieve locally.
- This attack may be mitigated by tweaking the serialized data parser to not resolve external entities. If external entities are needed, then implement a custom resolver that has a request timeout, data retrieval limit, and restrict resources it can retrieve locally.

## Related Weaknesses (CWE)
- CWE-611
