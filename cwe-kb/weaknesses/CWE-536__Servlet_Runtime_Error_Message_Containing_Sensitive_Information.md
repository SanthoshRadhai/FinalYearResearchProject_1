# CWE-536: Servlet Runtime Error Message Containing Sensitive Information

**Abstraction:** Variant  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/536.html  

## Description
A servlet error message indicates that there exists an unhandled exception in the web application code and may provide useful information to an attacker.

## Related Weaknesses
- ChildOf: CWE-211

## Common Consequences
- Scope: Confidentiality; Impact: Read Application Data — The error message may contain the location of the file in which the offending function is located. This may disclose the web root's absolute path as well as give the attacker the location of application files or configuration information. It may even disclose the portion of code that failed. In many cases, an attacker can use the data to launch further attacks against the system.

## Demonstrative Examples (summary)
- The following servlet code does not catch runtime exceptions, meaning that if such an exception were to occur, the container may display potentially dangerous information (such as a full stack trace).
