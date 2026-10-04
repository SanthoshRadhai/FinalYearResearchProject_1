# CAPEC-443: Malicious Logic Inserted Into Product by Authorized Developer

**Abstraction:** Detailed  
**Status:** Stable  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/443.html  

## Description
An adversary uses their privileged position within an authorized development organization to inject malicious logic into a codebase or product.

## Related Attack Patterns
- ChildOf: CAPEC-444

## Prerequisites
- Access to the product during the initial or continuous development.

## Consequences
- Scope: Authorization; Impact: Execute Unauthorized Commands

## Mitigations
- Assess software and hardware during development and prior to deployment to ensure that it functions as intended and without any malicious functionality. This includes both initial development, as well as updates propagated to the product after deployment.
