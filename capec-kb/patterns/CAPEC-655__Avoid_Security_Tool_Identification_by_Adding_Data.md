# CAPEC-655: Avoid Security Tool Identification by Adding Data

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/655.html  

## Description
An adversary adds data to a file to increase the file size beyond what security tools are capable of handling in an attempt to mask their actions. In addition to this, adding data to a file also changes the file's hash, frustrating security tools that look for known bad files by their hash.

## Related Attack Patterns
- ChildOf: CAPEC-572

## Consequences
- Scope: Accountability; Impact: Hide Activities, Bypass Protection Mechanism
- Scope: Integrity; Impact: Modify Data
