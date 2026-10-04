# CAPEC-466: Leveraging Active Adversary in the Middle Attacks to Bypass Same Origin Policy

**Abstraction:** Standard  
**Status:** Draft  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/466.html  

## Description
An attacker leverages an adversary in the middle attack (CAPEC-94) in order to bypass the same origin policy protection in the victim's browser. This active adversary in the middle attack could be launched, for instance, when the victim is connected to a public WIFI hot spot. An attacker is able to intercept requests and responses between the victim's browser and some non-sensitive website that does not use TLS.

## Related Attack Patterns
- ChildOf: CAPEC-94

## Prerequisites
- The victim and the attacker are both in an environment where an active adversary in the middle attack is possible (e.g., public WIFI hot spot)The victim visits at least one website that does not use TLS / SSL

## Skills Required
- [Low] Ability to intercept and modify requests / responses
- [Medium] Ability to create iFrame and JavaScript code that would initiate unauthorized requests to sensitive sites from the victim's browser
- [Medium] Solid understanding of the HTTP protocol

## Consequences
- Scope: Confidentiality; Impact: Read Data
- Scope: Authorization; Impact: Execute Unauthorized Commands

## Mitigations
- Design: Tunnel communications through a secure proxy
- Design: Trust level separation for privileged / non privileged interactions (e.g., two different browsers, two different users, two different operating systems, two different virtual machines)

## Related Weaknesses (CWE)
- CWE-300
