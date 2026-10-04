# CAPEC-588: DOM-Based XSS

**Abstraction:** Detailed  
**Status:** Stable  
**Likelihood of Attack:** High  
**Typical Severity:** Very High  
**Reference:** https://capec.mitre.org/data/definitions/588.html  

## Description
This type of attack is a form of Cross-Site Scripting (XSS) where a malicious script is inserted into the client-side HTML being parsed by a web browser. Content served by a vulnerable web application includes script code used to manipulate the Document Object Model (DOM). This script code either does not properly validate input, or does not perform proper output encoding, thus creating an opportunity for an adversary to inject a malicious script launch a XSS attack. A key distinction between other XSS attacks and DOM-based attacks is that in other XSS attacks, the malicious script runs when the vulnerable web page is initially loaded, while a DOM-based attack executes sometime after the page loads. Another distinction of DOM-based attacks is that in some cases, the malicious script is never sent to the vulnerable web server at all. An attack like this is guaranteed to bypass any server-side filtering attempts to protect users.

## Related Attack Patterns
- ChildOf: CAPEC-63

## Prerequisites
- An application that leverages a client-side web browser with scripting enabled.
- An application that manipulates the DOM via client-side scripting.
- An application that failS to adequately sanitize or encode untrusted input.

## Skills Required
- [Medium] Requires the ability to write scripts of some complexity and to inject it through user controlled fields in the system.

## Resources Required
- None: No specialized resources are required to execute this type of attack.

## Consequences
- Scope: Confidentiality; Impact: Read Data
- Scope: Confidentiality, Authorization, Access Control; Impact: Gain Privileges
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands
- Scope: Integrity; Impact: Modify Data

## Mitigations
- Use browser technologies that do not allow client-side scripting.
- Utilize proper character encoding for all output produced within client-site scripts manipulating the DOM.
- Ensure that all user-supplied input is validated before use.

## Related Weaknesses (CWE)
- CWE-79
- CWE-20
- CWE-83
