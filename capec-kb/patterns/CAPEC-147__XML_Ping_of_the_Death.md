# CAPEC-147: XML Ping of the Death

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/147.html  

## Description
An attacker initiates a resource depletion attack where a large number of small XML messages are delivered at a sufficiently rapid rate to cause a denial of service or crash of the target. Transactions such as repetitive SOAP transactions can deplete resources faster than a simple flooding attack because of the additional resources used by the SOAP protocol and the resources necessary to process SOAP messages. The transactions used are immaterial as long as they cause resource utilization on the target. In other words, this is a normal flooding attack augmented by using messages that will require extra processing on the target.

## Related Attack Patterns
- ChildOf: CAPEC-528

## Prerequisites
- The target must receive and process XML transactions.

## Skills Required
- [Low] To send small XML messages
- [High] To use distributed network to launch the attack

## Resources Required
- Transaction generator(s)/source(s) and ability to cause arrival of messages at the target with sufficient rapidity to overload target. Larger targets may be able to handle large volumes of requests so the attacker may require significant resources (such as a distributed network) to affect the target. However, the resources required of the attacker would be less than in the case of a simple flooding attack against the same target.

## Consequences
- Scope: Availability; Impact: Resource Consumption

## Mitigations
- Design: Build throttling mechanism into the resource allocation. Provide for a timeout mechanism for allocated resources whose transaction does not complete within a specified interval.
- Implementation: Provide for network flow control and traffic shaping to control access to the resources.

## Related Weaknesses (CWE)
- CWE-400
- CWE-770
