# CAPEC-591: Reflected XSS

**Abstraction:** Detailed  
**Status:** Stable  
**Likelihood of Attack:** High  
**Typical Severity:** Very High  
**Reference:** https://capec.mitre.org/data/definitions/591.html  

## Description
This type of attack is a form of Cross-Site Scripting (XSS) where a malicious script is "reflected" off a vulnerable web application and then executed by a victim's browser. The process starts with an adversary delivering a malicious script to a victim and convincing the victim to send the script to the vulnerable web application.

## Related Attack Patterns
- ChildOf: CAPEC-63

## Prerequisites
- An application that leverages a client-side web browser with scripting enabled.
- An application that fail to adequately sanitize or encode untrusted input.

## Skills Required
- [Medium] Requires the ability to write malicious scripts and embed them into HTTP requests.

## Resources Required
- None: No specialized resources are required to execute this type of attack.

## Consequences
- Scope: Confidentiality; Impact: Read Data
- Scope: Confidentiality, Authorization, Access Control; Impact: Gain Privileges
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands
- Scope: Integrity; Impact: Modify Data

## Mitigations
- Use browser technologies that do not allow client-side scripting.
- Utilize strict type, character, and encoding enforcement.
- Ensure that all user-supplied input is validated before use.

## Related Weaknesses (CWE)
- CWE-79
