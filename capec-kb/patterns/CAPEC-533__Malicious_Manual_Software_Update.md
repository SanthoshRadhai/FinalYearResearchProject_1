# CAPEC-533: Malicious Manual Software Update

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/533.html  

## Description
An attacker introduces malicious code to the victim's system by altering the payload of a software update, allowing for additional compromise or site disruption at the victim location. These manual, or user-assisted attacks, vary from requiring the user to download and run an executable, to as streamlined as tricking the user to click a URL. Attacks which aim at penetrating a specific network infrastructure often rely upon secondary attack methods to achieve the desired impact. Spamming, for example, is a common method employed as an secondary attack vector. Thus the attacker has in their arsenal a choice of initial attack vectors ranging from traditional SMTP/POP/IMAP spamming and its varieties, to web-application mechanisms which commonly implement both chat and rich HTML messaging within the user interface.

## Related Attack Patterns
- ChildOf: CAPEC-186

## Prerequisites
- Advanced knowledge about the download and update installation processes.
- Advanced knowledge about the deployed system and its various software subcomponents and processes.

## Skills Required
- [High] Able to develop malicious code that can be used on the victim's system while maintaining normal functionality.

## Mitigations
- Only accept software updates from an official source.

## Related Weaknesses (CWE)
- CWE-494
