# CAPEC-650: Upload a Web Shell to a Web Server

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/650.html  

## Description
By exploiting insufficient permissions, it is possible to upload a web shell to a web server in such a way that it can be executed remotely. This shell can have various capabilities, thereby acting as a "gateway" to the underlying web server. The shell might execute at the higher permission level of the web server, providing the ability the execute malicious code at elevated levels.

## Related Attack Patterns
- ChildOf: CAPEC-17

## Prerequisites
- The web server is susceptible to one of the various web application exploits that allows for uploading a shell file.

## Consequences
- Scope: Confidentiality; Impact: Read Data
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands

## Mitigations
- Make sure your web server is up-to-date with all patches to protect against known vulnerabilities.
- Ensure that the file permissions in directories on the web server from which files can be execute is set to the "least privilege" settings, and that those directories contents is controlled by an allowlist.

## Related Weaknesses (CWE)
- CWE-287
- CWE-553
