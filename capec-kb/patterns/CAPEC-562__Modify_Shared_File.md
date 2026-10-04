# CAPEC-562: Modify Shared File

**Abstraction:** Detailed  
**Status:** Draft  
**Reference:** https://capec.mitre.org/data/definitions/562.html  

## Description
An adversary manipulates the files in a shared location by adding malicious programs, scripts, or exploit code to valid content. Once a user opens the shared content, the tainted content is executed.

## Related Attack Patterns
- ChildOf: CAPEC-17

## Mitigations
- Disallow shared content. Protect shared folders by minimizing users that have write access. Use utilities that mitigate exploitation like the Microsoft Enhanced Mitigation Experience Toolkit (EMET) to prevent exploits from being run.

## Related Weaknesses (CWE)
- CWE-284
