# CAPEC-173: Action Spoofing

**Abstraction:** Meta  
**Status:** Stable  
**Likelihood of Attack:** High  
**Typical Severity:** Very High  
**Reference:** https://capec.mitre.org/data/definitions/173.html  

## Description
An adversary is able to disguise one action for another and therefore trick a user into initiating one type of action when they intend to initiate a different action. For example, a user might be led to believe that clicking a button will submit a query, but in fact it downloads software. Adversaries may perform this attack through social means, such as by simply convincing a victim to perform the action or relying on a user's natural inclination to do so, or through technical means, such as a clickjacking attack where a user sees one interface but is actually interacting with a second, invisible, interface.

## Prerequisites
- The adversary must convince the victim into performing the decoy action.
- The adversary must have the means to control a user's interface to present them with a decoy action as well as the actual malicious action. Simple versions of this attack can be performed using web pages requiring only that the adversary be able to host (or control) content that the user visits.

## Consequences
- Scope: Confidentiality, Integrity, Availability; Impact: Other

## Mitigations
- Avoid interacting with suspicious sites or clicking suspicious links.
- An organization should provide regular, robust cybersecurity training to its employees.

## Related Weaknesses (CWE)
- CWE-451
