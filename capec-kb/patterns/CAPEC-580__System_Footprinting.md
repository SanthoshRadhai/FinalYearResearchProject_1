# CAPEC-580: System Footprinting

**Abstraction:** Standard  
**Status:** Stable  
**Likelihood of Attack:** Low  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/580.html  

## Description
An adversary engages in active probing and exploration activities to determine security information about a remote target system. Often times adversaries will rely on remote applications that can be probed for system configurations.

## Related Attack Patterns
- ChildOf: CAPEC-169

## Prerequisites
- The adversary must have logical access to the target network and system.

## Skills Required
- [Low] The adversary needs to know basic linux commands.

## Consequences
- Scope: Confidentiality; Impact: Read Data

## Mitigations
- Keep patches up to date by installing weekly or daily if possible.
- Identify programs that may be used to acquire peripheral information and block them by using a software restriction policy or tools that restrict program execution by using a process allowlist.

## Related Weaknesses (CWE)
- CWE-204
- CWE-205
- CWE-208
