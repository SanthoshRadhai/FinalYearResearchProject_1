# CAPEC-183: IMAP/SMTP Command Injection

**Abstraction:** Standard  
**Status:** Draft  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/183.html  

## Description
An adversary exploits weaknesses in input validation on web-mail servers to execute commands on the IMAP/SMTP server. Web-mail servers often sit between the Internet and the IMAP or SMTP mail server. User requests are received by the web-mail servers which then query the back-end mail server for the requested information and return this response to the user. In an IMAP/SMTP command injection attack, mail-server commands are embedded in parts of the request sent to the web-mail server. If the web-mail server fails to adequately sanitize these requests, these commands are then sent to the back-end mail server when it is queried by the web-mail server, where the commands are then executed. This attack can be especially dangerous since administrators may assume that the back-end server is protected against direct Internet access and therefore may not secure it adequately against the execution of malicious commands.

## Related Attack Patterns
- ChildOf: CAPEC-248

## Prerequisites
- The target environment must consist of a web-mail server that the attacker can query and a back-end mail server. The back-end mail server need not be directly accessible to the attacker.
- The web-mail server must fail to adequately sanitize fields received from users and passed on to the back-end mail server.
- The back-end mail server must not be adequately secured against receiving malicious commands from the web-mail server.

## Resources Required
- None: No specialized resources are required to execute this type of attack. However, in most cases, the attacker will need to be a recognized user of the web-mail server.

## Related Weaknesses (CWE)
- CWE-77
