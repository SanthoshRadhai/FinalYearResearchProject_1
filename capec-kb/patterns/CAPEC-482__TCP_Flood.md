# CAPEC-482: TCP Flood

**Abstraction:** Standard  
**Status:** Draft  
**Reference:** https://capec.mitre.org/data/definitions/482.html  

## Description
An adversary may execute a flooding attack using the TCP protocol with the intent to deny legitimate users access to a service. These attacks exploit the weakness within the TCP protocol where there is some state information for the connection the server needs to maintain. This often involves the use of TCP SYN messages.

## Related Attack Patterns
- ChildOf: CAPEC-125

## Prerequisites
- This type of an attack requires the ability to generate a large amount of TCP traffic to send to the target port of a functioning server.

## Mitigations
- To mitigate this type of an attack, an organization can monitor incoming packets and look for patterns in the TCP traffic to determine if the network is under an attack. The potential target may implement a rate limit on TCP SYN messages which would provide limited capabilities while under attack.

## Related Weaknesses (CWE)
- CWE-770
