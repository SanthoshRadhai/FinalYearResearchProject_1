# CAPEC-142: DNS Cache Poisoning

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/142.html  

## Description
A domain name server translates a domain name (such as www.example.com) into an IP address that Internet hosts use to contact Internet resources. An adversary modifies a public DNS cache to cause certain names to resolve to incorrect addresses that the adversary specifies. The result is that client applications that rely upon the targeted cache for domain name resolution will be directed not to the actual address of the specified domain name but to some other address. Adversaries can use this to herd clients to sites that install malware on the victim's computer or to masquerade as part of a Pharming attack.

## Related Attack Patterns
- ChildOf: CAPEC-141
- CanPrecede: CAPEC-89

## Prerequisites
- A DNS cache must be vulnerable to some attack that allows the adversary to replace addresses in its lookup table.Client applications must trust the corrupted cashed values and utilize them for their domain name resolutions.

## Skills Required
- [Medium] To overwrite/modify targeted DNS cache

## Resources Required
- The adversary must have the resources to modify the targeted cache. In addition, in most cases the adversary will wish to host the sites to which users will be redirected, although in some cases redirecting to a third party site will accomplish the adversary's goals.

## Mitigations
- Configuration: Make sure your DNS servers have been updated to the latest versions
- Configuration: UNIX services like rlogin, rsh/rcp, xhost, and nfs are all susceptible to wrong information being held in a cache. Care should be taken with these services so they do not rely upon DNS caches that have been exposed to the Internet.
- Configuration: Disable client side DNS caching.

## Related Weaknesses (CWE)
- CWE-348
- CWE-345
- CWE-349
- CWE-346
- CWE-350
