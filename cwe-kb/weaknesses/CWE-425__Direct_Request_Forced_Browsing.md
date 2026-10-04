# CWE-425: Direct Request ('Forced Browsing')

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/425.html  

## Description
The web application does not adequately enforce appropriate authorization on all restricted URLs, scripts, or files.

## Related Weaknesses
- ChildOf: CWE-862
- ChildOf: CWE-862
- ChildOf: CWE-288
- ChildOf: CWE-424
- CanPrecede: CWE-471
- CanPrecede: CWE-98

## Common Consequences
- Scope: Confidentiality, Integrity, Availability, Access Control; Impact: Read Application Data, Modify Application Data, Execute Unauthorized Code or Commands, Gain Privileges or Assume Identity

## Potential Mitigations
- [Architecture and Design, Operation] Apply appropriate access control authorizations for each access to all restricted URLs, scripts or files.
- [Architecture and Design] Consider using MVC based frameworks such as Struts.

## Demonstrative Examples (summary)
- If forced browsing is possible, an attacker may be able to directly access a sensitive page by entering a URL similar to the following.
