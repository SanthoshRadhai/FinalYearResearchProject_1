# CAPEC-268: Audit Log Manipulation

**Abstraction:** Standard  
**Status:** Draft  
**Reference:** https://capec.mitre.org/data/definitions/268.html  

## Description
The attacker injects, manipulates, deletes, or forges malicious log entries into the log file, in an attempt to mislead an audit of the log file or cover tracks of an attack. Due to either insufficient access controls of the log files or the logging mechanism, the attacker is able to perform such actions.

## Related Attack Patterns
- ChildOf: CAPEC-161

## Prerequisites
- The target host is logging the action and data of the user.
- The target host insufficiently protects access to the logs or logging mechanisms.

## Resources Required
- The attacker must understand how the logging mechanism works. Optionally, the attacker must know the location and the format of individual entries of the log files.

## Related Weaknesses (CWE)
- CWE-117
