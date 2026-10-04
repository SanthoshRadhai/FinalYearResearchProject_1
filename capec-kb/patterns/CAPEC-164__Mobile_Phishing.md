# CAPEC-164: Mobile Phishing

**Abstraction:** Detailed  
**Status:** Stable  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/164.html  

## Description
An adversary targets mobile phone users with a phishing attack for the purpose of soliciting account passwords or sensitive information from the user. Mobile Phishing is a variation of the Phishing social engineering technique where the attack is initiated via a text or SMS message, rather than email. The user is enticed to provide information or visit a compromised web site via this message. Apart from the manner in which the attack is initiated, the attack proceeds as a standard Phishing attack.

## Related Attack Patterns
- ChildOf: CAPEC-98

## Prerequisites
- An adversary needs mobile phone numbers to initiate contact with the victim.
- An adversary needs to correctly guess the entity with which the victim does business and impersonate it. Most of the time phishers just use the most popular banks/services and send out their "hooks" to many potential victims.
- An adversary needs to have a sufficiently compelling call to action to prompt the user to take action.
- The replicated website needs to look extremely similar to the original website and the URL used to get to that website needs to look like the real URL of the said business entity.

## Skills Required
- [Medium] Basic knowledge about websites: obtaining them, designing and implementing them, etc.

## Resources Required
- Either mobile phone or access to a web resource that allows text messages to be sent to mobile phones. Resources needed for regular Phishing attack.

## Consequences
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges
- Scope: Confidentiality; Impact: Read Data
- Scope: Integrity; Impact: Modify Data

## Mitigations
- Do not follow any links that you receive within text messages and do not input any login credentials on the page that they take you too. Instead, call your Bank, PayPal, eBay, etc., and inquire about the problem. Safe practices also include leveraging the entity's mobile application or directly typing the entity's URL in the browser and only then logging in. Never reply to any text messages that ask you to provide sensitive information of any kind.

## Related Weaknesses (CWE)
- CWE-451
