# CAPEC-407: Pretexting

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** Medium  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/407.html  

## Description
An adversary engages in pretexting behavior to solicit information from target persons, or manipulate the target into performing some action that serves the adversary's interests. During a pretexting attack, the adversary creates an invented scenario, assuming an identity or role to persuade a targeted victim to release information or perform some action. It is more than just creating a lie; in some cases it can be creating a whole new identity and then using that identity to manipulate the receipt of information.

## Related Attack Patterns
- ChildOf: CAPEC-416
- ChildOf: CAPEC-410
- CanPrecede: CAPEC-163

## Prerequisites
- The adversary must have the means and knowledge of how to communicate with the target in some manner.The adversary must have knowledge of the pretext that would influence the actions of the specific target.

## Skills Required
- [Low] The adversary requires strong inter-personal and communication skills.

## Consequences
- Scope: Confidentiality; Impact: Other

## Mitigations
- An organization should provide regular, robust cybersecurity training to its employees to prevent successful social engineering attacks.
