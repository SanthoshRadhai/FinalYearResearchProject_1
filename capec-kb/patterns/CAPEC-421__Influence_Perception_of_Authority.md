# CAPEC-421: Influence Perception of Authority

**Abstraction:** Detailed  
**Status:** Stable  
**Likelihood of Attack:** High  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/421.html  

## Description
An adversary uses a social engineering technique to convey a sense of authority that motivates the target to reveal specific information or take specific action. There are various techniques for producing a sense of authority during ordinary modes of communication. One common method is impersonation. By impersonating someone with a position of power within an organization, an adversary may motivate the target individual to reveal some piece of sensitive information or perform an action that benefits the adversary.

## Related Attack Patterns
- ChildOf: CAPEC-417

## Prerequisites
- The adversary must have the means and knowledge of how to communicate with the target in some manner.

## Skills Required
- [Low] The adversary requires strong inter-personal and communication skills.

## Resources Required
- None: No specialized resources are required to execute this type of attack.

## Consequences
- Scope: Confidentiality, Integrity, Availability; Impact: Other

## Mitigations
- An organization should provide regular, robust cybersecurity training to its employees to prevent social engineering attacks.
