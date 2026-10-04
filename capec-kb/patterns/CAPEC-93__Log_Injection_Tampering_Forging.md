# CAPEC-93: Log Injection-Tampering-Forging

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/93.html  

## Description
This attack targets the log files of the target host. The attacker injects, manipulates or forges malicious log entries in the log file, allowing them to mislead a log audit, cover traces of attack, or perform other malicious actions. The target host is not properly controlling log access. As a result tainted data is resulting in the log files leading to a failure in accountability, non-repudiation and incident forensics capability.

## Related Attack Patterns
- ChildOf: CAPEC-268
- CanPrecede: CAPEC-592

## Prerequisites
- The target host is logging the action and data of the user.
- The target host insufficiently protects access to the logs or logging mechanisms.

## Skills Required
- [Low] This attack can be as simple as adding extra characters to the logged data (e.g. username). Adding entries is typically easier than removing entries.
- [Medium] A more sophisticated attack can try to defeat the input validation mechanism.

## Consequences
- Scope: Integrity; Impact: Modify Data

## Mitigations
- Carefully control access to physical log files.
- Do not allow tainted data to be written in the log file without prior input validation. An allowlist may be used to properly validate the data.
- Use synchronization to control the flow of execution.
- Use static analysis tools to identify log forging vulnerabilities.
- Avoid viewing logs with tools that may interpret control characters in the file, such as command-line shells.

## Related Weaknesses (CWE)
- CWE-117
- CWE-75
- CWE-150
