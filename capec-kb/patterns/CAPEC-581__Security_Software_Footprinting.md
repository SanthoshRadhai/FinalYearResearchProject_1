# CAPEC-581: Security Software Footprinting

**Abstraction:** Detailed  
**Status:** Draft  
**Reference:** https://capec.mitre.org/data/definitions/581.html  

## Description
Adversaries may attempt to get a listing of security tools that are installed on the system and their configurations. This may include security related system features (such as a built-in firewall or anti-spyware) as well as third-party security software.

## Related Attack Patterns
- ChildOf: CAPEC-580

## Mitigations
- Identify programs that may be used to acquire security tool information and block them by using a software restriction policy or tools that restrict program execution by using a process allowlist.
