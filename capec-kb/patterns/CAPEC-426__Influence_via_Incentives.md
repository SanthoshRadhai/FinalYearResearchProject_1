# CAPEC-426: Influence via Incentives

**Abstraction:** Standard  
**Status:** Stable  
**Likelihood of Attack:** Low  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/426.html  

## Description
The adversary incites a behavior from the target by manipulating something of influence. This is commonly associated with financial, social, or ideological incentivization. Examples include monetary fraud, peer pressure, and preying on the target's morals or ethics. The most effective incentive against one target might not be as effective against another, therefore the adversary must gather information about the target's vulnerability to particular incentives.

## Related Attack Patterns
- ChildOf: CAPEC-416

## Prerequisites
- The adversary must have the means and knowledge of how to communicate with the target in some manner.The adversary must have knowledge of the incentives that would influence the actions of the specific target.

## Skills Required
- [Low] The adversary requires strong inter-personal and communication skills.

## Consequences
- Scope: Confidentiality, Integrity, Availability; Impact: Other

## Mitigations
- An organization should provide regular, robust cybersecurity training to its employees to prevent social engineering attacks.
