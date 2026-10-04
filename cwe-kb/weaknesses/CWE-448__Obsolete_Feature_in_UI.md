# CWE-448: Obsolete Feature in UI

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/448.html  

## Description
A UI function is obsolete and the product does not warn the user.

## Related Weaknesses
- ChildOf: CWE-446

## Common Consequences
- Scope: Other; Impact: Quality Degradation, Varies by Context

## Potential Mitigations
- [Architecture and Design] Remove the obsolete feature from the UI. Warn the user that the feature is no longer supported.
