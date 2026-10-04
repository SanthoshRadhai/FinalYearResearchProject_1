# CAPEC-551: Modify Existing Service

**Abstraction:** Detailed  
**Status:** Draft  
**Reference:** https://capec.mitre.org/data/definitions/551.html  

## Description
When an operating system starts, it also starts programs called services or daemons. Modifying existing services may break existing services or may enable services that are disabled/not commonly used.

## Related Attack Patterns
- ChildOf: CAPEC-542

## Mitigations
- Limit privileges of user accounts so service changes can only be performed by authorized administrators. Also monitor any service changes that may occur inadvertently.

## Related Weaknesses (CWE)
- CWE-284
- CWE-522
