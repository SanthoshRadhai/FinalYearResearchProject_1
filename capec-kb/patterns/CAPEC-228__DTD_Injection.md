# CAPEC-228: DTD Injection

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/228.html  

## Description
An attacker injects malicious content into an application's DTD in an attempt to produce a negative technical impact. DTDs are used to describe how XML documents are processed. Certain malformed DTDs (for example, those with excessive entity expansion as described in CAPEC 197) can cause the XML parsers that process the DTDs to consume excessive resources resulting in resource depletion.

## Related Attack Patterns
- ChildOf: CAPEC-250
- CanPrecede: CAPEC-197
- CanPrecede: CAPEC-491

## Prerequisites
- The target must be running an XML based application that leverages DTDs.

## Mitigations
- Design: Sanitize incoming DTDs to prevent excessive expansion or other actions that could result in impacts like resource depletion.
- Implementation: Disallow the inclusion of DTDs as part of incoming messages.
- Implementation: Use XML parsing tools that protect against DTD attacks.

## Related Weaknesses (CWE)
- CWE-829
