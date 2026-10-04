# CAPEC-108: Command Line Execution through SQL Injection

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** Very High  
**Reference:** https://capec.mitre.org/data/definitions/108.html  

## Description
An attacker uses standard SQL injection methods to inject data into the command line for execution. This could be done directly through misuse of directives such as MSSQL_xp_cmdshell or indirectly through injection of data into the database that would be interpreted as shell commands. Sometime later, an unscrupulous backend application (or could be part of the functionality of the same application) fetches the injected data stored in the database and uses this data as command line arguments without performing proper validation. The malicious data escapes that data plane by spawning new commands to be executed on the host.

## Related Attack Patterns
- ChildOf: CAPEC-66

## Prerequisites
- The application does not properly validate data before storing in the database
- Backend application implicitly trusts the data stored in the database
- Malicious data is used on the backend as a command line argument

## Skills Required
- [High] The attacker most likely has to be familiar with the internal functionality of the system to launch this attack. Without that knowledge, there are not many feedback mechanisms to give an attacker the indication of how to perform command injection or whether the attack is succeeding.

## Resources Required
- None: No specialized resources are required to execute this type of attack.

## Consequences
- Scope: Integrity; Impact: Modify Data
- Scope: Confidentiality; Impact: Read Data
- Scope: Availability; Impact: Unreliable Execution
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands

## Mitigations
- Disable MSSQL xp_cmdshell directive on the database
- Properly validate the data (syntactically and semantically) before writing it to the database.
- Do not implicitly trust the data stored in the database. Re-validate it prior to usage to make sure that it is safe to use in a given context (e.g. as a command line argument).

## Related Weaknesses (CWE)
- CWE-89
- CWE-74
- CWE-20
- CWE-78
- CWE-114
