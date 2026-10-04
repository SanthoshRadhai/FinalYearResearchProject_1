# CAPEC-15: Command Delimiters

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/15.html  

## Description
An attack of this type exploits a programs' vulnerabilities that allows an attacker's commands to be concatenated onto a legitimate command with the intent of targeting other resources such as the file system or database. The system that uses a filter or denylist input validation, as opposed to allowlist validation is vulnerable to an attacker who predicts delimiters (or combinations of delimiters) not present in the filter or denylist. As with other injection attacks, the attacker uses the command delimiter payload as an entry point to tunnel through the application and activate additional attacks through SQL queries, shell commands, network scanning, and so on.

## Related Attack Patterns
- ChildOf: CAPEC-137

## Prerequisites
- Software's input validation or filtering must not detect and block presence of additional malicious command.

## Skills Required
- [Medium] The attacker has to identify injection vector, identify the specific commands, and optionally collect the output, i.e. from an interactive session.

## Resources Required
- Ability to communicate synchronously or asynchronously with server. Optionally, ability to capture output directly through synchronous communication or other method such as FTP.

## Consequences
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands
- Scope: Confidentiality; Impact: Read Data

## Mitigations
- Design: Perform allowlist validation against a positive specification for command length, type, and parameters.
- Design: Limit program privileges, so if commands circumvent program input validation or filter routines then commands do not running under a privileged account
- Implementation: Perform input validation for all remote content.
- Implementation: Use type conversions such as JDBC prepared statements.

## Related Weaknesses (CWE)
- CWE-146
- CWE-77
- CWE-184
- CWE-78
- CWE-185
- CWE-93
- CWE-140
- CWE-157
- CWE-138
- CWE-154
- CWE-697
