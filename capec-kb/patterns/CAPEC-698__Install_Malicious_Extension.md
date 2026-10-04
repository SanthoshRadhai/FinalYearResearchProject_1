# CAPEC-698: Install Malicious Extension

**Abstraction:** Detailed  
**Status:** Stable  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/698.html  

## Description
An adversary directly installs or tricks a user into installing a malicious extension into existing trusted software, with the goal of achieving a variety of negative technical impacts.

## Related Attack Patterns
- ChildOf: CAPEC-542

## Prerequisites
- The adversary must craft malware based on the type of software and system(s) they intend to exploit.
- If the adversary intends to install the malicious extension themself, they must first compromise the target machine via some other means.

## Skills Required
- [Medium] Ability to create malicious extensions that can exploit specific software applications and systems.
- [Medium] Optional: Ability to exploit target system(s) via other means in order to gain entry.

## Consequences
- Scope: Confidentiality, Access Control; Impact: Read Data
- Scope: Integrity, Access Control; Impact: Modify Data
- Scope: Authorization, Access Control; Impact: Execute Unauthorized Commands, Alter Execution Logic, Gain Privileges

## Mitigations
- Only install extensions/plugins from official/verifiable sources.
- Confirm extensions/plugins are legitimate and not malware masquerading as a legitimate extension/plugin.
- Ensure the underlying software leveraging the extension/plugin (including operating systems) is up-to-date.
- Implement an extension/plugin allow list, based on the given security policy.
- If applicable, confirm extensions/plugins are properly signed by the official developers.
- For web browsers, close sessions when finished to prevent malicious extensions/plugins from executing the the background.

## Related Weaknesses (CWE)
- CWE-507
- CWE-829
