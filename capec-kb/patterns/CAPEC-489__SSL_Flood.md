# CAPEC-489: SSL Flood

**Abstraction:** Standard  
**Status:** Draft  
**Reference:** https://capec.mitre.org/data/definitions/489.html  

## Description
An adversary may execute a flooding attack using the SSL protocol with the intent to deny legitimate users access to a service by consuming all the available resources on the server side. These attacks take advantage of the asymmetric relationship between the processing power used by the client and the processing power used by the server to create a secure connection. In this manner the attacker can make a large number of HTTPS requests on a low provisioned machine to tie up a disproportionately large number of resources on the server. The clients then continue to keep renegotiating the SSL connection. When multiplied by a large number of attacking machines, this attack can result in a crash or loss of service to legitimate users.

## Related Attack Patterns
- ChildOf: CAPEC-125

## Prerequisites
- This type of an attack requires the ability to generate a large amount of SSL traffic to send a target server.

## Mitigations
- To mitigate this type of an attack, an organization can create rule based filters to silently drop connections if too many are attempted in a certain time period.

## Related Weaknesses (CWE)
- CWE-770
