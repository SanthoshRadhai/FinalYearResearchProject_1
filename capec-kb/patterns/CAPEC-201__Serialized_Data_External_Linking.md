# CAPEC-201: Serialized Data External Linking

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/201.html  

## Description
An adversary creates a serialized data file (e.g. XML, YAML, etc...) that contains an external data reference. Because serialized data parsers may not validate documents with external references, there may be no checks on the nature of the reference in the external data. This can allow an adversary to open arbitrary files or connections, which may further lead to the adversary gaining access to information on the system that they would normally be unable to obtain.

## Related Attack Patterns
- ChildOf: CAPEC-122
- ChildOf: CAPEC-278

## Prerequisites
- The target must follow external data references without validating the validity of the reference target.

## Skills Required
- [Low] To send serialized data messages with maliciously crafted schema.

## Resources Required
- None: No specialized resources are required to execute this type of attack.

## Consequences
- Scope: Confidentiality; Impact: Read Data

## Mitigations
- Configure the serialized data processor to only retrieve external entities from trusted sources.

## Related Weaknesses (CWE)
- CWE-829
