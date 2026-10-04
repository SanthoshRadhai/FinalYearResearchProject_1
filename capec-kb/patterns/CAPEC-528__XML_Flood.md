# CAPEC-528: XML Flood

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/528.html  

## Description
An adversary may execute a flooding attack using XML messages with the intent to deny legitimate users access to a web service. These attacks are accomplished by sending a large number of XML based requests and letting the service attempt to parse each one. In many cases this type of an attack will result in a XML Denial of Service (XDoS) due to an application becoming unstable, freezing, or crashing.

## Related Attack Patterns
- ChildOf: CAPEC-125

## Prerequisites
- The target must receive and process XML transactions.
- An adverssary must possess the ability to generate a large amount of XML based messages to send to the target service.

## Skills Required
- [Low] Denial of service

## Consequences
- Scope: Availability; Impact: Resource Consumption

## Mitigations
- Design: Build throttling mechanism into the resource allocation. Provide for a timeout mechanism for allocated resources whose transaction does not complete within a specified interval.
- Implementation: Provide for network flow control and traffic shaping to control access to the resources.

## Related Weaknesses (CWE)
- CWE-770
