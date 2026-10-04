# CWE-405: Asymmetric Resource Consumption (Amplification)

**Abstraction:** Class  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/405.html  

## Description
The product does not properly control situations in which an adversary can cause the product to consume or produce excessive resources without requiring the adversary to invest equivalent work or otherwise prove authorization, i.e., the adversary's influence is "asymmetric."

## Extended Description
This can lead to poor performance due to "amplification" of resource consumption, typically in a non-linear fashion. This situation is worsened if the product allows malicious users or attackers to consume more resources than their access level permits.

## Related Weaknesses
- ChildOf: CWE-400

## Common Consequences
- Scope: Availability; Impact: DoS: Amplification, DoS: Resource Consumption (CPU), DoS: Resource Consumption (Memory), DoS: Resource Consumption (Other) — Sometimes this is a factor in "flood" attacks, but other types of amplification exist.

## Potential Mitigations
- [Architecture and Design] An application must make resources available to a client commensurate with the client's access level.
- [Architecture and Design] An application must, at all times, keep track of allocated resources and meter their usage appropriately.
- [System Configuration] Consider disabling resource-intensive algorithms on the server side, such as Diffie-Hellman key exchange.

## Demonstrative Examples (summary)
- This code listens on a port for DNS requests and sends the result to the requesting address.
- This function prints the contents of a specified file requested by a user.
- The DTD and the very brief XML below illustrate what is meant by an XML bomb. The ZERO entity contains one character, the letter A. The choice of entity name ZERO is being used to indicate length equivalent to that exponent on two, that is, the length of ZERO is 2^0. Similarly, ONE refers to ZERO twice, therefore the XML parser will expand ONE to a length of 2, or 2^1. Ultimately, we reach entity THIRTYTWO, which will expand to 2^32 characters in length, or 4 GB, probably consuming far more data than expected.
- This example attempts to check if an input string is a "sentence" [REF-1164].
- An adversary can cause significant resource consumption on a server by filtering the cryptographic algorithms offered by the client to the ones that are the most resource-intensive on the server side. After discovering which cryptographic algorithms are supported by the server, a malicious client can send the initial cryptographic handshake messages that contains only the resource-intensive algorithms. For some cryptographic protocols, these messages can be completely prefabricated, as the resource-intensive part of the handshake happens on the server-side first (such as TLS), rather than on the client side. In the case of cryptographic protocols where the resource-intensive part should happen on the client-side first (such as SSH), a malicious client can send a forged/precalculated computation result, which seems correct to the server, so the resource-intensive part of the handshake is going to happen on the server side. A malicious client is required to send only the initial messages of a cryptographic handshake to initiate the resource-consuming part of the cryptographic handshake. These messages are usually small, and generating them requires minimal computational effort, enabling a denial-of-service attack. An additional risk is the fact that higher key size increases the effectiveness of the attack. Cryptographic protocols where the clients have influence over the size of the used key (such as TLS 1.3 or SSH) are most at risk, as the client can enforce the highest key size supported by the server.
