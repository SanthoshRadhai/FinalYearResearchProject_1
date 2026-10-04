# CAPEC-19: Embedding Scripts within Scripts

**Abstraction:** Standard  
**Status:** Stable  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/19.html  

## Description
An adversary leverages the capability to execute their own script by embedding it within other scripts that the target software is likely to execute due to programs' vulnerabilities that are brought on by allowing remote hosts to execute scripts.

## Related Attack Patterns
- ChildOf: CAPEC-242

## Prerequisites
- Target software must be able to execute scripts, and also grant the adversary privilege to write/upload scripts.

## Skills Required
- [Low] To load malicious script into open, e.g. world writable directory
- [Medium] Executing remote scripts on host and collecting output

## Consequences
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges

## Mitigations
- Use browser technologies that do not allow client side scripting.
- Utilize strict type, character, and encoding enforcement.
- Server side developers should not proxy content via XHR or other means. If a HTTP proxy for remote content is setup on the server side, the client's browser has no way of discerning where the data is originating from.
- Ensure all content that is delivered to client is sanitized against an acceptable content specification.
- Perform input validation for all remote content.
- Perform output validation for all remote content.
- Disable scripting languages such as JavaScript in browser
- Session tokens for specific host
- Patching software. There are many attack vectors for XSS on the client side and the server side. Many vulnerabilities are fixed in service packs for browser, web servers, and plug in technologies, staying current on patch release that deal with XSS countermeasures mitigates this.
- Privileges are constrained, if a script is loaded, ensure system runs in chroot jail or other limited authority mode

## Related Weaknesses (CWE)
- CWE-284
