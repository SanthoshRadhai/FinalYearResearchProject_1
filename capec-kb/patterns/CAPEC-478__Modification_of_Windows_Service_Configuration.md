# CAPEC-478: Modification of Windows Service Configuration

**Abstraction:** Detailed  
**Status:** Usable  
**Likelihood of Attack:** Low  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/478.html  

## Description
An adversary exploits a weakness in access control to modify the execution parameters of a Windows service. The goal of this attack is to execute a malicious binary in place of an existing service.

## Related Attack Patterns
- ChildOf: CAPEC-203

## Prerequisites
- The adversary must have the capability to write to the Windows Registry on the targeted system.

## Resources Required
- None: No specialized resources are required to execute this type of attack.

## Consequences
- Scope: Integrity; Impact: Execute Unauthorized Commands

## Mitigations
- Ensure proper permissions are set for Registry hives to prevent users from modifying keys for system components that may lead to privilege escalation.

## Related Weaknesses (CWE)
- CWE-284
