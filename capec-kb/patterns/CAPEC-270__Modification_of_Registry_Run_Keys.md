# CAPEC-270: Modification of Registry Run Keys

**Abstraction:** Detailed  
**Status:** Stable  
**Likelihood of Attack:** Medium  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/270.html  

## Description
An adversary adds a new entry to the "run keys" in the Windows registry so that an application of their choosing is executed when a user logs in. In this way, the adversary can get their executable to operate and run on the target system with the authorized user's level of permissions. This attack is a good way for an adversary to run persistent spyware on a user's machine, such as a keylogger.

## Related Attack Patterns
- ChildOf: CAPEC-203
- CanPrecede: CAPEC-568
- CanPrecede: CAPEC-529
- CanPrecede: CAPEC-646
- CanFollow: CAPEC-555

## Prerequisites
- The adversary must have gained access to the target system via physical or logical means in order to carry out this attack.

## Consequences
- Scope: Integrity; Impact: Modify Data, Gain Privileges

## Mitigations
- Identify programs that may be used to acquire process information and block them by using a software restriction policy or tools that restrict program execution by using a process allowlist.

## Related Weaknesses (CWE)
- CWE-15
