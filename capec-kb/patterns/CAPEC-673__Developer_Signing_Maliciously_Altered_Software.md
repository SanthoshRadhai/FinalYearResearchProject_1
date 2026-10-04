# CAPEC-673: Developer Signing Maliciously Altered Software

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/673.html  

## Description
Software produced by a reputable developer is clandestinely infected with malicious code and then digitally signed by the unsuspecting developer, where the software has been altered via a compromised software development or build process prior to being signed. The receiver or user of the software has no reason to believe that it is anything but legitimate and proceeds to deploy it to organizational systems. This attack differs from CAPEC-206, since the developer is inadvertently signing malicious code they believe to be legitimate and which they are unware of any malicious modifications.

## Related Attack Patterns
- ChildOf: CAPEC-444

## Prerequisites
- An adversary would need to have access to a targeted developer’s software development environment, including to their software build processes, where the adversary could ensure code maliciously tainted prior to a build process is included in software packages built.

## Skills Required
- [High] The adversary must have the skills to infiltrate a developer’s software development/build environment and to implant malicious code in developmental software code, a build server, or a software repository containing dependency code, which would be referenced to be included during the software build process.

## Consequences
- Scope: Integrity, Confidentiality; Impact: Read Data, Modify Data
- Scope: Access Control, Authorization; Impact: Gain Privileges, Execute Unauthorized Commands

## Mitigations
- Have a security concept of operations (CONOPS) for the IDE that includes: Protecting the IDE via logical isolation using firewall and DMZ technologies/architectures; Maintaining strict security administration and configuration management of configuration management tools, developmental software and dependency code repositories, compilers, and system build tools.
- Employ intrusion detection and malware detection capabilities on IDE systems where feasible.
