# CAPEC-89: Pharming

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** Very High  
**Reference:** https://capec.mitre.org/data/definitions/89.html  

## Description
A pharming attack occurs when the victim is fooled into entering sensitive data into supposedly trusted locations, such as an online bank site or a trading platform. An attacker can impersonate these supposedly trusted sites and have the victim be directed to their site rather than the originally intended one. Pharming does not require script injection or clicking on malicious links for the attack to succeed.

## Related Attack Patterns
- ChildOf: CAPEC-151

## Prerequisites
- Vulnerable DNS software or improperly protected hosts file or router that can be poisoned
- A website that handles sensitive information but does not use a secure connection and a certificate that is valid is also prone to pharming

## Skills Required
- [Medium] The attacker needs to be able to poison the resolver - DNS entries or local hosts file or router entry pointing to a trusted DNS server - in order to successfully carry out a pharming attack. Setting up a fake website, identical to the targeted one, does not require special skills.

## Resources Required
- None: No specialized resources are required to execute this type of attack. Having knowledge of the way the target site has been structured, in order to create a fake version, is required. Poisoning the resolver requires knowledge of a vulnerability that can be exploited.

## Consequences
- Scope: Confidentiality; Impact: Read Data

## Mitigations
- All sensitive information must be handled over a secure connection.
- Known vulnerabilities in DNS or router software or in operating systems must be patched as soon as a fix has been released and tested.
- End users must ensure that they provide sensitive information only to websites that they trust, over a secure connection with a valid certificate issued by a well-known certificate authority.

## Related Weaknesses (CWE)
- CWE-346
- CWE-350
