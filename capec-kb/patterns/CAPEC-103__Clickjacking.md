# CAPEC-103: Clickjacking

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/103.html  

## Description
An adversary tricks a victim into unknowingly initiating some action in one system while interacting with the UI from a seemingly completely different, usually an adversary controlled or intended, system.

## Related Attack Patterns
- ChildOf: CAPEC-173

## Prerequisites
- The victim is communicating with the target application via a web based UI and not a thick client
- The victim's browser security policies allow at least one of the following JavaScript, Flash, iFrames, ActiveX, or CSS.
- The victim uses a modern browser that supports UI elements like clickable buttons (i.e. not using an old text only browser)
- The victim has an active session with the target system.
- The target system's interaction window is open in the victim's browser and supports the ability for initiating sensitive actions on behalf of the user in the target system

## Skills Required
- [High] Crafting the proper malicious site and luring the victim to this site are not trivial tasks.

## Resources Required
- None: No specialized resources are required to execute this type of attack.

## Consequences
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges
- Scope: Integrity; Impact: Modify Data
- Scope: Confidentiality; Impact: Read Data
- Scope: Availability; Impact: Unreliable Execution

## Mitigations
- If using the Firefox browser, use the NoScript plug-in that will help forbid iFrames.
- Turn off JavaScript, Flash and disable CSS.
- When maintaining an authenticated session with a privileged target system, do not use the same browser to navigate to unfamiliar sites to perform other activities. Finish working with the target system and logout first before proceeding to other tasks.

## Related Weaknesses (CWE)
- CWE-1021
