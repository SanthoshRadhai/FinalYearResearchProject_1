# CWE-694: Use of Multiple Resources with Duplicate Identifier

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/694.html  

## Description
The product uses multiple resources that can have the same identifier, in a context in which unique identifiers are required.

## Extended Description
If the product assumes that each resource has a unique identifier, the product could operate on the wrong resource if attackers can cause multiple resources to be associated with the same identifier.

## Related Weaknesses
- ChildOf: CWE-99
- ChildOf: CWE-573

## Common Consequences
- Scope: Access Control; Impact: Bypass Protection Mechanism — If unique identifiers are assumed when protecting sensitive resources, then duplicate identifiers might allow attackers to bypass the protection.
- Scope: Other; Impact: Quality Degradation

## Potential Mitigations
- [Architecture and Design] Where possible, use unique identifiers. If non-unique identifiers are detected, then do not operate any resource with a non-unique identifier and report the error appropriately.

## Demonstrative Examples (summary)
- These two Struts validation forms have the same name.
