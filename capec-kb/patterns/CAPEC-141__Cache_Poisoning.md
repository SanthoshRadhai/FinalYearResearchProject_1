# CAPEC-141: Cache Poisoning

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/141.html  

## Description
An attacker exploits the functionality of cache technologies to cause specific data to be cached that aids the attackers' objectives. This describes any attack whereby an attacker places incorrect or harmful material in cache. The targeted cache can be an application's cache (e.g. a web browser cache) or a public cache (e.g. a DNS or ARP cache). Until the cache is refreshed, most applications or clients will treat the corrupted cache value as valid. This can lead to a wide range of exploits including redirecting web browsers towards sites that install malware and repeatedly incorrect calculations based on the incorrect value.

## Related Attack Patterns
- ChildOf: CAPEC-161

## Prerequisites
- The attacker must be able to modify the value stored in a cache to match a desired value.
- The targeted application must not be able to detect the illicit modification of the cache and must trust the cache value in its calculations.

## Skills Required
- [Medium] To overwrite/modify targeted cache

## Mitigations
- Configuration: Disable client side caching.
- Implementation: Listens for query replies on a network, and sends a notification via email when an entry changes.

## Related Weaknesses (CWE)
- CWE-348
- CWE-345
- CWE-349
- CWE-346
