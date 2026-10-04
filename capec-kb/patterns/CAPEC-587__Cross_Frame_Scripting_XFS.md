# CAPEC-587: Cross Frame Scripting (XFS)

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/587.html  

## Description
This attack pattern combines malicious Javascript and a legitimate webpage loaded into a concealed iframe. The malicious Javascript is then able to interact with a legitimate webpage in a manner that is unknown to the user. This attack usually leverages some element of social engineering in that an attacker must convinces a user to visit a web page that the attacker controls.

## Related Attack Patterns
- ChildOf: CAPEC-103

## Prerequisites
- The user's browser must have vulnerabilities in its implementation of the same-origin policy. It allows certain data in a loaded page to originate from different servers/domains.

## Consequences
- Scope: Confidentiality; Impact: Read Data

## Mitigations
- Avoid clicking on untrusted links.
- Employ techniques such as frame busting, which is a method by which developers aim to prevent their site being loaded within a frame.

## Related Weaknesses (CWE)
- CWE-1021
