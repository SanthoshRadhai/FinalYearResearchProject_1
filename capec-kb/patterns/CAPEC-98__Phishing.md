# CAPEC-98: Phishing

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** Very High  
**Reference:** https://capec.mitre.org/data/definitions/98.html  

## Description
Phishing is a social engineering technique where an attacker masquerades as a legitimate entity with which the victim might do business in order to prompt the user to reveal some confidential information (very frequently authentication credentials) that can later be used by an attacker. Phishing is essentially a form of information gathering or "fishing" for information.

## Related Attack Patterns
- ChildOf: CAPEC-151
- CanPrecede: CAPEC-89
- CanPrecede: CAPEC-543
- CanPrecede: CAPEC-611
- CanPrecede: CAPEC-630
- CanPrecede: CAPEC-631
- CanPrecede: CAPEC-632

## Prerequisites
- An attacker needs to have a way to initiate contact with the victim. Typically that will happen through e-mail.
- An attacker needs to correctly guess the entity with which the victim does business and impersonate it. Most of the time phishers just use the most popular banks/services and send out their "hooks" to many potential victims.
- An attacker needs to have a sufficiently compelling call to action to prompt the user to take action.
- The replicated website needs to look extremely similar to the original website and the URL used to get to that website needs to look like the real URL of the said business entity.

## Skills Required
- [Medium] Basic knowledge about websites: obtaining them, designing and implementing them, etc.

## Resources Required
- Some web development tools to put up a fake website.

## Consequences
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges
- Scope: Confidentiality; Impact: Read Data
- Scope: Integrity; Impact: Modify Data

## Mitigations
- Do not follow any links that you receive within your e-mails and certainly do not input any login credentials on the page that they take you too. Instead, call your Bank, PayPal, eBay, etc., and inquire about the problem. A safe practice would also be to type the URL of your bank in the browser directly and only then log in. Also, never reply to any e-mails that ask you to provide sensitive information of any kind.

## Related Weaknesses (CWE)
- CWE-451
