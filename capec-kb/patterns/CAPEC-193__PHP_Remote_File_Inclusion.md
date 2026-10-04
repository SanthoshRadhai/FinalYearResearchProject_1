# CAPEC-193: PHP Remote File Inclusion

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/193.html  

## Description
In this pattern the adversary is able to load and execute arbitrary code remotely available from the application. This is usually accomplished through an insecurely configured PHP runtime environment and an improperly sanitized "include" or "require" call, which the user can then control to point to any web-accessible file. This allows adversaries to hijack the targeted application and force it to execute their own instructions.

## Related Attack Patterns
- ChildOf: CAPEC-253

## Prerequisites
- Target application server must allow remote files to be included in the "require", "include", etc. PHP directives
- The adversary must have the ability to make HTTP requests to the target web application.

## Skills Required
- [Low] To inject the malicious payload in a web page
- [Medium] To bypass filters in the application

## Resources Required
- None: No specialized resources are required to execute this type of attack.

## Consequences
- Scope: Integrity; Impact: Modify Data
- Scope: Confidentiality; Impact: Read Data
- Scope: Authorization; Impact: Execute Unauthorized Commands
- Scope: Accountability, Authentication, Authorization, Non-Repudiation; Impact: Gain Privileges
- Scope: Access Control, Authorization; Impact: Bypass Protection Mechanism

## Mitigations
- Implementation: Perform input validation for all remote content, including remote and user-generated content
- Implementation: Only allow known files to be included (allowlist)
- Implementation: Make use of indirect references passed in URL parameters instead of file names
- Configuration: Ensure that remote scripts cannot be include in the "include" or "require" PHP directives

## Related Weaknesses (CWE)
- CWE-98
- CWE-80
