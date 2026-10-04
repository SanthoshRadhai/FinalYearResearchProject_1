# CAPEC-521: Hardware Design Specifications Are Altered

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/521.html  

## Description
An attacker with access to a manufacturer's hardware manufacturing process documentation alters the design specifications, which introduces flaws advantageous to the attacker once the system is deployed.

## Related Attack Patterns
- ChildOf: CAPEC-447

## Prerequisites
- Advanced knowledge of hardware capabilities of a manufacturer's product.
- Access to the manufacturer's documentation.

## Skills Required
- [High] Ability to read, interpret, and subsequently alter manufacturer's documentation to cause errors in design specifications.
- [High] Ability to stealthly gain access via remote compromise or physical access to the manufacturer's documentation.

## Mitigations
- Digitize documents and cryptographically sign them to verify authenticity.
- Password protect documents and make them read-only for unauthorized users.
- Avoid emailing important documents and configurations.
- Ensure deleted files are actually deleted.
- Maintain backups of the document for recovery and verification.
- Separate need-to-know information from system configuration information depending on the user.
