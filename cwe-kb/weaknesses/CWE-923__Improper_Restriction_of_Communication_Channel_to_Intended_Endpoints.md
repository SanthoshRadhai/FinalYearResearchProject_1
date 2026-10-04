# CWE-923: Improper Restriction of Communication Channel to Intended Endpoints

**Abstraction:** Class  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/923.html  

## Description
The product establishes a communication channel to (or from) an endpoint for privileged or protected operations, but it does not properly ensure that it is communicating with the correct endpoint.

## Extended Description
Attackers might be able to spoof the intended endpoint from a different system or process, thus gaining the same level of access as the intended endpoint. While this issue frequently involves authentication between network-based clients and servers, other types of communication channels and endpoints can have this weakness.

## Related Weaknesses
- ChildOf: CWE-284

## Common Consequences
- Scope: Integrity, Confidentiality; Impact: Gain Privileges or Assume Identity — If an attacker can spoof the endpoint, the attacker gains all the privileges that were intended for the original endpoint.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- These cross-domain policy files mean to allow Flash and Silverlight applications hosted on other domains to access its data:
- This Android application will remove a user account when it receives an intent to do so:
