# CAPEC-669: Alteration of a Software Update

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/669.html  

## Description
An adversary with access to an organization’s software update infrastructure inserts malware into the content of an outgoing update to fielded systems where a wide range of malicious effects are possible. With the same level of access, the adversary can alter a software update to perform specific malicious acts including granting the adversary control over the software’s normal functionality.

## Related Attack Patterns
- ChildOf: CAPEC-184
- CanPrecede: CAPEC-673

## Prerequisites
- An adversary would need to have penetrated an organization’s software update infrastructure including gaining access to components supporting the configuration management of software versions and updates related to the software maintenance of customer systems.

## Skills Required
- [High] Skills required include the ability to infiltrate the organization’s software update infrastructure either from the Internet or from within the organization, including subcontractors, and be able to change software being delivered to customer/user systems in an undetected manner.

## Consequences
- Scope: Access Control; Impact: Gain Privileges
- Scope: Authorization; Impact: Execute Unauthorized Commands
- Scope: Integrity; Impact: Modify Data
- Scope: Confidentiality; Impact: Read Data

## Mitigations
- Have a Software Assurance Plan that includes maintaining strict configuration management control of source code, object code and software development, build and distribution tools; manual code reviews and static code analysis for developmental software; and tracking of all storage and movement of code.
- Require elevated privileges for distribution of software and software updates.
