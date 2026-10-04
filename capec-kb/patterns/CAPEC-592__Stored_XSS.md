# CAPEC-592: Stored XSS

**Abstraction:** Detailed  
**Status:** Stable  
**Likelihood of Attack:** High  
**Typical Severity:** Very High  
**Reference:** https://capec.mitre.org/data/definitions/592.html  

## Description
An adversary utilizes a form of Cross-site Scripting (XSS) where a malicious script is persistently "stored" within the data storage of a vulnerable web application as valid input.

## Related Attack Patterns
- ChildOf: CAPEC-63

## Prerequisites
- An application that leverages a client-side web browser with scripting enabled.
- An application that fails to adequately sanitize or encode untrusted input.
- An application that stores information provided by the user in data storage of some kind.

## Skills Required
- [Medium] Requires the ability to write scripts of varying complexity and to inject them through user controlled fields within the application.

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
- Ensure that all user-supplied input is validated before being stored.

## Related Weaknesses (CWE)
- CWE-79
