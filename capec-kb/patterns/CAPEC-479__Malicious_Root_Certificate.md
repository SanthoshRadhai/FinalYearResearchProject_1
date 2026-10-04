# CAPEC-479: Malicious Root Certificate

**Abstraction:** Detailed  
**Status:** Stable  
**Likelihood of Attack:** Low  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/479.html  

## Description
An adversary exploits a weakness in authorization and installs a new root certificate on a compromised system. Certificates are commonly used for establishing secure TLS/SSL communications within a web browser. When a user attempts to browse a website that presents a certificate that is not trusted an error message will be displayed to warn the user of the security risk. Depending on the security settings, the browser may not allow the user to establish a connection to the website. Adversaries have used this technique to avoid security warnings prompting users when compromised systems connect over HTTPS to adversary controlled web servers that spoof legitimate websites in order to collect login credentials.

## Related Attack Patterns
- ChildOf: CAPEC-473

## Prerequisites
- The adversary must have the ability to create a new root certificate.

## Related Weaknesses (CWE)
- CWE-284
