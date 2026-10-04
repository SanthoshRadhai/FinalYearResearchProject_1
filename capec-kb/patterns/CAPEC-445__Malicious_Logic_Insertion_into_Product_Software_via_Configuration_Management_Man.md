# CAPEC-445: Malicious Logic Insertion into Product Software via Configuration Management Manipulation

**Abstraction:** Detailed  
**Status:** Stable  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/445.html  

## Description
An adversary exploits a configuration management system so that malicious logic is inserted into a software products build, update or deployed environment. If an adversary can control the elements included in a product's configuration management for build they can potentially replace, modify or insert code files containing malicious logic. If an adversary can control elements of a product's ongoing operational configuration management baseline they can potentially force clients receiving updates from the system to install insecure software when receiving updates from the server.

## Related Attack Patterns
- ChildOf: CAPEC-444

## Prerequisites
- Access to the configuration management system during deployment or currently deployed at a victim location. This access is often obtained via insider access or by leveraging another attack pattern to gain permissions that the adversary wouldn't normally have.

## Consequences
- Scope: Authorization; Impact: Execute Unauthorized Commands

## Mitigations
- Assess software during development and prior to deployment to ensure that it functions as intended and without any malicious functionality.
- Leverage anti-virus products to detect and quarantine software with known virus.
