# CAPEC-518: Documentation Alteration to Produce Under-performing Systems

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/518.html  

## Description
An attacker with access to a manufacturer's documentation alters the descriptions of system capabilities with the intent of causing errors in derived system requirements, impacting the overall effectiveness and capability of the system, allowing an attacker to take advantage of the introduced system capability flaw once the system is deployed.

## Related Attack Patterns
- ChildOf: CAPEC-447

## Prerequisites
- Advanced knowledge of software and hardware capabilities of a manufacturer's product.
- Access to the manufacturer's documentation.

## Skills Required
- [High] Ability to read, interpret, and subsequently alter manufacturer's documentation to misrepresent system capabilities.
- [High] Ability to stealthly gain access via remote compromise or physical access to the manufacturer's documentation.

## Mitigations
- Digitize documents and cryptographically sign them to verify authenticity.
- Password protect documents and make them read-only for unauthorized users.
- Avoid emailing important documents and configurations.
- Ensure deleted files are actually deleted.
- Maintain backups of the document for recovery and verification.
- Separate need-to-know information from system configuration information depending on the user.
