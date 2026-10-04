# CAPEC-549: Local Execution of Code

**Abstraction:** Meta  
**Status:** Stable  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/549.html  

## Description
An adversary installs and executes malicious code on the target system in an effort to achieve a negative technical impact. Examples include rootkits, ransomware, spyware, adware, and others.

## Prerequisites
- Knowledge of the target system's vulnerabilities that can be capitalized on with malicious code.The adversary must be able to place the malicious code on the target system.

## Resources Required
- The means by which the adversary intends to place the malicious code on the system dictates the tools required. For example, suppose the adversary wishes to leverage social engineering and convince a legitimate user to open a malicious file attached to a seemingly legitimate email. In this case, the adversary might require a tool capable of wrapping malicious code into an innocuous filetype (e.g., PDF, .doc, etc.)

## Consequences
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands
- Scope: Confidentiality, Integrity, Availability; Impact: Other

## Mitigations
- Employ robust cybersecurity training for all employees.
- Implement system antivirus software that scans all attachments before opening them.
- Regularly patch all software.
- Execute all suspicious files in a sandbox environment.

## Related Weaknesses (CWE)
- CWE-829
