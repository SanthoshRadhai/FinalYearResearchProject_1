# CAPEC-179: Calling Micro-Services Directly

**Abstraction:** Standard  
**Status:** Draft  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/179.html  

## Description
An attacker is able to discover and query Micro-services at a web location and thereby expose the Micro-services to further exploitation by gathering information about their implementation and function. Micro-services in web pages allow portions of a page to connect to the server and update content without needing to cause the entire page to update. This allows user activity to change portions of the page more quickly without causing disruptions elsewhere.

## Related Attack Patterns
- ChildOf: CAPEC-554

## Prerequisites
- The target site must use micro-services that interact with the server and one or more of these micro-services must be vulnerable to some other attack pattern.

## Resources Required
- The attacker usually needs to be able to invoke micro-services directly in order to control the parameters that are used in their attack. The attacker may require other resources depending on the nature of the flaw in the targeted micro-service.
