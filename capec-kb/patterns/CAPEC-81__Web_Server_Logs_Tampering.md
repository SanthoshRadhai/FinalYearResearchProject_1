# CAPEC-81: Web Server Logs Tampering

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/81.html  

## Description
Web Logs Tampering attacks involve an attacker injecting, deleting or otherwise tampering with the contents of web logs typically for the purposes of masking other malicious behavior. Additionally, writing malicious data to log files may target jobs, filters, reports, and other agents that process the logs in an asynchronous attack pattern. This pattern of attack is similar to "Log Injection-Tampering-Forging" except that in this case, the attack is targeting the logs of the web server and not the application.

## Related Attack Patterns
- ChildOf: CAPEC-268

## Prerequisites
- Target server software must be a HTTP server that performs web logging.

## Skills Required
- [Low] To input faked entries into Web logs

## Resources Required
- Ability to send specially formatted HTTP request to web server

## Consequences
- Scope: Integrity; Impact: Modify Data

## Mitigations
- Design: Use input validation before writing to web log
- Design: Validate all log data before it is output

## Related Weaknesses (CWE)
- CWE-117
- CWE-93
- CWE-75
- CWE-221
- CWE-96
- CWE-20
- CWE-150
- CWE-276
- CWE-279
- CWE-116
