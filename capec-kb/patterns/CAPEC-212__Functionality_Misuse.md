# CAPEC-212: Functionality Misuse

**Abstraction:** Meta  
**Status:** Stable  
**Likelihood of Attack:** Medium  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/212.html  

## Description
An adversary leverages a legitimate capability of an application in such a way as to achieve a negative technical impact. The system functionality is not altered or modified but used in a way that was not intended. This is often accomplished through the overuse of a specific functionality or by leveraging functionality with design flaws that enables the adversary to gain access to unauthorized, sensitive data.

## Prerequisites
- The adversary has the capability to interact with the application directly.The target system does not adequately implement safeguards to prevent misuse of authorized actions/processes.

## Skills Required
- [Low] General computer knowledge about how applications are launched, how they interact with input/output, and how they are configured.

## Consequences
- Scope: Confidentiality; Impact: Gain Privileges
- Scope: Confidentiality, Integrity, Availability; Impact: Other

## Mitigations
- Perform comprehensive threat modeling, a process of identifying, evaluating, and mitigating potential threats to the application. This effort can help reveal potentially obscure application functionality that can be manipulated for malicious purposes.
- When implementing security features, consider how they can be misused and compromised.

## Related Weaknesses (CWE)
- CWE-1242
- CWE-1246
- CWE-1281
