# CAPEC-546: Incomplete Data Deletion in a Multi-Tenant Environment

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/546.html  

## Description
An adversary obtains unauthorized information due to insecure or incomplete data deletion in a multi-tenant environment. If a cloud provider fails to completely delete storage and data from former cloud tenants' systems/resources, once these resources are allocated to new, potentially malicious tenants, the latter can probe the provided resources for sensitive information still there.

## Related Attack Patterns
- ChildOf: CAPEC-545

## Prerequisites
- The cloud provider must not assuredly delete part or all of the sensitive data for which they are responsible.The adversary must have the ability to interact with the system.

## Skills Required
- [Low] The adversary requires the ability to traverse directory structure.

## Consequences
- Scope: Confidentiality; Impact: Read Data

## Mitigations
- Cloud providers should completely delete data to render it irrecoverable and inaccessible from any layer and component of infrastructure resources.
- Deletion of data should be completed promptly when requested.

## Related Weaknesses (CWE)
- CWE-284
- CWE-1266
- CWE-1272
