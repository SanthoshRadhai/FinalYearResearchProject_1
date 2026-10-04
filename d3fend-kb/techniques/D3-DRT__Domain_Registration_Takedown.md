# D3-DRT: Domain Registration Takedown

**Reference:** https://d3fend.mitre.org/technique/D3-DRT/  

## Definition
The process of performing a takedown of the attacker's domain registration infrastructure.

## Parent Class(es)
- Object Eviction

## Relationships
- **deletes:** Domain Registration
- **kb-reference:** Reference - Understanding the Domain Registration Behavior of Spammers

## Knowledge Base Article
## How it works

Most nameserver hosts and domain name registrars comply with internationally recognised standards and supply their services based on terms and conditions that provide users and organisations protection from abuse and trademark infringement. Performing a WHOIS query on the attacker's domain will provide a contact that can be notified in the case of abuse. Formal takedown processes should be initiated to suspend or disable the normal function of the domain name.

## Considerations

- Takedown notifications should clearly demonstrate (with evidence) that the nameserver or registrars Terms and Conditions have been breached.
- Takedown processes are notoriously slow and sometimes unsuccessful.
- Many government organisations will have takedown processes that should also be followed. They may use this for intelligence to assist other organisations suffering an attack.
- Top level domain registrars will have takedown processes that can be followed, as an escalation path, when the nameserver host and/or registrar have not responded or complied timeously or inline with the TLD expectations.

## Examples of Domain Registration Abuse

Attackers will create infrastructure from which to carry out their operations and this may include registering domain names to be used in the various attacks. Known misuse cases include:

- Registering domain names that are similar to the victim's. This is known as typosquatting or URL hijacking. Legitimate looking mails or URLs could be sent using this domain in phishing campaigns.
- Registering domain names that are used in C2 beacons.
