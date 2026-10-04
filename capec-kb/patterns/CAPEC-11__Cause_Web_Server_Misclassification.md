# CAPEC-11: Cause Web Server Misclassification

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/11.html  

## Description
An attack of this type exploits a Web server's decision to take action based on filename or file extension. Because different file types are handled by different server processes, misclassification may force the Web server to take unexpected action, or expected actions in an unexpected sequence. This may cause the server to exhaust resources, supply debug or system data to the attacker, or bind an attacker to a remote process.

## Related Attack Patterns
- ChildOf: CAPEC-635

## Prerequisites
- Web server software must rely on file name or file extension for processing.
- The attacker must be able to make HTTP requests to the web server.

## Skills Required
- [Low] To modify file name or file extension
- [Medium] To use misclassification to force the Web server to disclose configuration information, source, or binary data

## Resources Required
- None: No specialized resources are required to execute this type of attack.

## Consequences
- Scope: Confidentiality; Impact: Read Data
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges

## Mitigations
- Implementation: Server routines should be determined by content not determined by filename or file extension.

## Related Weaknesses (CWE)
- CWE-430
