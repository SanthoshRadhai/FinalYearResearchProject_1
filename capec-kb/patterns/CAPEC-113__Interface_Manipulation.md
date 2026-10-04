# CAPEC-113: Interface Manipulation

**Abstraction:** Meta  
**Status:** Draft  
**Likelihood of Attack:** Medium  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/113.html  

## Description
An adversary manipulates the use or processing of an interface (e.g. Application Programming Interface (API) or System-on-Chip (SoC)) resulting in an adverse impact upon the security of the system implementing the interface. This can allow the adversary to bypass access control and/or execute functionality not intended by the interface implementation, possibly compromising the system which integrates the interface. Interface manipulation can take on a number of forms including forcing the unexpected use of an interface or the use of an interface in an unintended way.

## Prerequisites
- The target system must expose interface functionality in a manner that can be discovered and manipulated by an adversary. This may require reverse engineering the interface or decrypting/de-obfuscating client-server exchanges.

## Resources Required
- The requirements vary depending upon the nature of the interface. For example, application-layer APIs related to the processing of the HTTP protocol may require one or more of the following: an Adversary-In-The-Middle (CAPEC-94) proxy, a web browser, or a programming/scripting language.

## Related Weaknesses (CWE)
- CWE-1192
