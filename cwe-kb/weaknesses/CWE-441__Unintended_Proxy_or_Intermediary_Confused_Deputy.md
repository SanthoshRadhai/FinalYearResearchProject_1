# CWE-441: Unintended Proxy or Intermediary ('Confused Deputy')

**Abstraction:** Class  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/441.html  

## Description
The product receives a request, message, or directive from an upstream component, but the product does not sufficiently preserve the original source of the request before forwarding the request to an external actor that is outside of the product's control sphere. This causes the product to appear to be the source of the request, leading it to act as a proxy or other intermediary between the upstream component and the external actor.

## Extended Description
If an attacker cannot directly contact a target, but the product has access to the target, then the attacker can send a request to the product and have it be forwarded to the target. The request would appear to be coming from the product's system, not the attacker's system. As a result, the attacker can bypass access controls (such as firewalls) or hide the source of malicious requests, since the requests would not be coming directly from the attacker. Since proxy functionality and message-forwarding often serve a legitimate purpose, this issue only becomes a vulnerability when: The product runs with different privileges or on a different system, or otherwise has different levels of access than the upstream component; The attacker is prevented from making the request directly to the target; and The attacker can create a request that the proxy does not explicitly intend to be forwarded on the behalf of the requester. Such a request might point to an unexpected hostname, port number, hardware IP, or service. Or, the request might be sent to an allowed service, but the request could contain disallowed directives, commands, or resources.

## Related Weaknesses
- ChildOf: CWE-610
- CanPrecede: CWE-668

## Common Consequences
- Scope: Non-Repudiation, Access Control; Impact: Gain Privileges or Assume Identity, Hide Activities, Execute Unauthorized Code or Commands

## Potential Mitigations
- [Architecture and Design] Enforce the use of strong mutual authentication mechanism between the two parties.
- [Architecture and Design] Whenever a product is an intermediary or proxy for transactions between two other components, the proxy core should not drop the identity of the initiator of the transaction. The immutability of the identity of the initiator must be maintained and should be forwarded all the way to the target.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- A SoC contains a microcontroller (running ring-3 (least trusted ring) code), a Memory Mapped Input Output (MMIO) mapped IP core (containing design-house secrets), and a Direct Memory Access (DMA) controller, among several other compute elements and peripherals. The SoC implements access control to protect the registers in the IP core (which registers store the design-house secrets) from malicious, ring-3 (least trusted ring) code executing on the microcontroller. The DMA controller, however, is not blocked off from accessing the IP core for functional reasons.
