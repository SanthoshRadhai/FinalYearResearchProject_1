# CAPEC-48: Passing Local Filenames to Functions That Expect a URL

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/48.html  

## Description
This attack relies on client side code to access local files and resources instead of URLs. When the client browser is expecting a URL string, but instead receives a request for a local file, that execution is likely to occur in the browser process space with the browser's authority to local files. The attacker can send the results of this request to the local files out to a site that they control. This attack may be used to steal sensitive authentication data (either local or remote), or to gain system profile information to launch further attacks.

## Related Attack Patterns
- ChildOf: CAPEC-212

## Prerequisites
- The victim's software must not differentiate between the location and type of reference passed the client software, e.g. browser

## Skills Required
- [Medium] Attacker identifies known local files to exploit

## Consequences
- Scope: Confidentiality; Impact: Read Data
- Scope: Integrity; Impact: Modify Data

## Mitigations
- Implementation: Ensure all content that is delivered to client is sanitized against an acceptable content specification.
- Implementation: Ensure all configuration files and resource are either removed or protected when promoting code into production.
- Design: Use browser technologies that do not allow client side scripting.
- Implementation: Perform input validation for all remote content.
- Implementation: Perform output validation for all remote content.
- Implementation: Disable scripting languages such as JavaScript in browser

## Related Weaknesses (CWE)
- CWE-241
- CWE-706
