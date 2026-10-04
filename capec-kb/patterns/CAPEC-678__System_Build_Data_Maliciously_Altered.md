# CAPEC-678: System Build Data Maliciously Altered

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/678.html  

## Description
During the system build process, the system is deliberately misconfigured by the alteration of the build data. Access to system configuration data files and build processes is susceptible to deliberate misconfiguration of the system.

## Related Attack Patterns
- ChildOf: CAPEC-444

## Prerequisites
- An adversary has access to the data files and processes used for executing system configuration and performing the build.

## Consequences
- Scope: Integrity; Impact: Execute Unauthorized Commands
- Scope: Access Control; Impact: Gain Privileges
- Scope: Confidentiality; Impact: Modify Data, Read Data

## Mitigations
- Implement configuration management security practices that protect the integrity of software and associated data.
- Monitor and control access to the configuration management system.
- Harden centralized repositories against attack.
- Establish acceptance criteria for configuration management check-in to assure integrity.
- Plan for and audit the security of configuration management administration processes.
- Maintain configuration control over operational systems.
