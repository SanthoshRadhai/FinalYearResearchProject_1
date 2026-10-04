# CAPEC-472: Browser Fingerprinting

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/472.html  

## Description
An attacker carefully crafts small snippets of Java Script to efficiently detect the type of browser the potential victim is using. Many web-based attacks need prior knowledge of the web browser including the version of browser to ensure successful exploitation of a vulnerability. Having this knowledge allows an attacker to target the victim with attacks that specifically exploit known or zero day weaknesses in the type and version of the browser used by the victim. Automating this process via Java Script as a part of the same delivery system used to exploit the browser is considered more efficient as the attacker can supply a browser fingerprinting method and integrate it with exploit code, all contained in Java Script and in response to the same web page request by the browser.

## Related Attack Patterns
- ChildOf: CAPEC-541

## Prerequisites
- Victim's browser visits a website that contains attacker's Java ScriptJava Script is not disabled in the victim's browser

## Mitigations
- Configuration: Disable Java Script in the browser

## Related Weaknesses (CWE)
- CWE-200
