# CAPEC-552: Install Rootkit 

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/552.html  

## Description
An adversary exploits a weakness in authentication to install malware that alters the functionality and information provide by targeted operating system API calls. Often referred to as rootkits, it is often used to hide the presence of programs, files, network connections, services, drivers, and other system components.

## Related Attack Patterns
- ChildOf: CAPEC-542

## Mitigations
- Prevent adversary access to privileged accounts necessary to install rootkits.

## Related Weaknesses (CWE)
- CWE-284
