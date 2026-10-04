# CAPEC-4: Using Alternative IP Address Encodings

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/4.html  

## Description
This attack relies on the adversary using unexpected formats for representing IP addresses. Networked applications may expect network location information in a specific format, such as fully qualified domains names (FQDNs), URL, IP address, or IP Address ranges. If the location information is not validated against a variety of different possible encodings and formats, the adversary can use an alternate format to bypass application access control.

## Related Attack Patterns
- ChildOf: CAPEC-267

## Prerequisites
- The target software must fail to anticipate all of the possible valid encodings of an IP/web address.
- The adversary must have the ability to communicate with the server.

## Skills Required
- [Low] The adversary has only to try IP address format combinations.

## Resources Required
- The adversary needs to have knowledge of an alternative IP address encoding that bypasses the access control policy of an application. Alternatively, the adversary can simply try to brute-force various encoding possibilities.

## Consequences
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges

## Mitigations
- Design: Default deny access control policies
- Design: Input validation routines should check and enforce both input data types and content against a positive specification. In regards to IP addresses, this should include the authorized manner for the application to represent IP addresses and not accept user specified IP addresses and IP address formats (such as ranges)
- Implementation: Perform input validation for all remote content.

## Related Weaknesses (CWE)
- CWE-291
- CWE-173
