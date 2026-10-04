# CAPEC-519: Documentation Alteration to Cause Errors in System Design

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/519.html  

## Description
An attacker with access to a manufacturer's documentation containing requirements allocation and software design processes maliciously alters the documentation in order to cause errors in system design. This allows the attacker to take advantage of a weakness in a deployed system of the manufacturer for malicious purposes.

## Related Attack Patterns
- ChildOf: CAPEC-447

## Prerequisites
- Advanced knowledge of software capabilities of a manufacturer's product.
- Access to the manufacturer's documentation.

## Skills Required
- [High] Ability to read, interpret, and subsequently alter manufacturer's documentation to cause errors in system design.
- [High] Ability to stealthly gain access via remote compromise or physical access to the manufacturer's documentation.

## Mitigations
- Digitize documents and cryptographically sign them to verify authenticity.
- Password protect documents and make them read-only for unauthorized users.
- Avoid emailing important documents and configurations.
- Ensure deleted files are actually deleted.
- Maintain multiple instances of the document across different privileged users for recovery and verification.
