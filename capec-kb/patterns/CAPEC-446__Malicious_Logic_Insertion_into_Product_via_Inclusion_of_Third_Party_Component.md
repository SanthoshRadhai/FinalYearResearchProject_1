# CAPEC-446: Malicious Logic Insertion into Product via Inclusion of Third-Party Component

**Abstraction:** Detailed  
**Status:** Stable  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/446.html  

## Description
An adversary conducts supply chain attacks by the inclusion of insecure third-party components into a technology, product, or code-base, possibly packaging a malicious driver or component along with the product before shipping it to the consumer or acquirer.

## Related Attack Patterns
- ChildOf: CAPEC-444

## Prerequisites
- Access to the product during the initial or continuous development. This access is often obtained via insider access to include the third-party component after deployment.

## Consequences
- Scope: Authorization; Impact: Execute Unauthorized Commands

## Mitigations
- Assess software and hardware during development and prior to deployment to ensure that it functions as intended and without any malicious functionality. This includes both initial development, as well as updates propagated to the product after deployment.
- Don't assume popular third-party components are free from malware or vulnerabilities. For software, assess for malicious functionality via update/commit reviews or automated static/dynamic analysis prior to including the component within the application and deploying in a production environment.
