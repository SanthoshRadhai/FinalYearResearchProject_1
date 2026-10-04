# CAPEC-677: Server Motherboard Compromise

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/677.html  

## Description
Malware is inserted in a server motherboard (e.g., in the flash memory) in order to alter server functionality from that intended. The development environment or hardware/software support activity environment is susceptible to an adversary inserting malicious software into hardware components during development or update.

## Related Attack Patterns
- ChildOf: CAPEC-534

## Prerequisites
- An adversary with access to hardware/software processes and tools within the development or hardware/software support environment can insert malicious software into hardware components during development or update/maintenance.

## Consequences
- Scope: Integrity; Impact: Execute Unauthorized Commands

## Mitigations
- Purchase IT systems, components and parts from government approved vendors whenever possible.
- Establish diversity among suppliers.
- Conduct rigorous threat assessments of suppliers.
- Require that Bills of Material (BoM) for critical parts and components be certified.
- Utilize contract language requiring contractors and subcontractors to flow down to subcontractors and suppliers SCRM and SCRA (Supply Chain Risk Assessment) requirements.
- Establish trusted supplier networks.
