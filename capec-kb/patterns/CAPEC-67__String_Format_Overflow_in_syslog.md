# CAPEC-67: String Format Overflow in syslog()

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** Very High  
**Reference:** https://capec.mitre.org/data/definitions/67.html  

## Description
This attack targets applications and software that uses the syslog() function insecurely. If an application does not explicitely use a format string parameter in a call to syslog(), user input can be placed in the format string parameter leading to a format string injection attack. Adversaries can then inject malicious format string commands into the function call leading to a buffer overflow. There are many reported software vulnerabilities with the root cause being a misuse of the syslog() function.

## Related Attack Patterns
- ChildOf: CAPEC-100
- ChildOf: CAPEC-135

## Prerequisites
- The Syslog function is used without specifying a format string argument, allowing user input to be placed direct into the function call as a format string.

## Consequences
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands
- Scope: Availability; Impact: Unreliable Execution
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges
- Scope: Integrity; Impact: Modify Data

## Mitigations
- The code should be reviewed for misuse of the Syslog function call. Manual or automated code review can be used. The reviewer needs to ensure that all format string functions are passed a static string which cannot be controlled by the user and that the proper number of arguments are always sent to that function as well. If at all possible, do not use the %n operator in format strings. The following code shows a correct usage of Syslog(): syslog(LOG_ERR, "%s", cmdBuf); The following code shows a vulnerable usage of Syslog(): syslog(LOG_ERR, cmdBuf); // the buffer cmdBuff is taking user supplied data.

## Related Weaknesses (CWE)
- CWE-120
- CWE-134
- CWE-74
- CWE-20
- CWE-680
- CWE-697
