# CWE-322: Key Exchange without Entity Authentication

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/322.html  

## Description
The product performs a key exchange with an actor without verifying the identity of that actor.

## Extended Description
Performing a key exchange will preserve the integrity of the information sent between two entities, but this will not guarantee that the entities are who they claim they are. This may enable an attacker to impersonate an actor by modifying traffic between the two entities. Typically, this involves a victim client that contacts a malicious server that is impersonating a trusted server. If the client skips authentication or ignores an authentication failure, the malicious server may request authentication information from the user. The malicious server can then use this authentication information to log in to the trusted server using the victim's credentials, sniff traffic between the victim and trusted server, etc.

## Related Weaknesses
- ChildOf: CWE-306
- CanPrecede: CWE-923
- PeerOf: CWE-295

## Common Consequences
- Scope: Access Control; Impact: Bypass Protection Mechanism — No authentication takes place in this process, bypassing an assumed protection of encryption.
- Scope: Confidentiality; Impact: Read Application Data — The encrypted communication between a user and a trusted host may be subject to sniffing by any actor in the communication path.

## Potential Mitigations
- [Architecture and Design] Ensure that proper authentication is included in the system design.
- [Implementation] Understand and properly implement all checks necessary to ensure the identity of entities involved in encrypted communications.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- Many systems have used Diffie-Hellman key exchange without authenticating the entities exchanging keys, allowing attackers to influence communications by redirecting or interfering with the communication path. Many people using SSL/TLS skip the authentication (often unknowingly).
