# CWE-553: Command Shell in Externally Accessible Directory

**Abstraction:** Variant  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/553.html  

## Description
A possible shell file exists in /cgi-bin/ or other accessible directories. This is extremely dangerous and can be used by an attacker to execute commands on the web server.

## Related Weaknesses
- ChildOf: CWE-552

## Common Consequences
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Code or Commands

## Potential Mitigations
- [Installation, System Configuration] Remove any Shells accessible under the web root folder and children directories.
