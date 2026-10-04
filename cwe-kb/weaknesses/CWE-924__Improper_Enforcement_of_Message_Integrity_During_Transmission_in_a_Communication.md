# CWE-924: Improper Enforcement of Message Integrity During Transmission in a Communication Channel

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/924.html  

## Description
The product establishes a communication channel with an endpoint and receives a message from that endpoint, but it does not sufficiently ensure that the message was not modified during transmission.

## Extended Description
Attackers might be able to modify the message and spoof the endpoint by interfering with the data as it crosses the network or by redirecting the connection to a system under their control.

## Related Weaknesses
- ChildOf: CWE-345
- ChildOf: CWE-345

## Common Consequences
- Scope: Integrity, Confidentiality; Impact: Gain Privileges or Assume Identity — If an attackers can spoof the endpoint, the attacker gains all the privileges that were intended for the original endpoint.
