# D3-BMA: Bus Message Authentication

**Reference:** https://d3fend.mitre.org/technique/D3-BMA/  

## Definition
Applies cryptographic primitives to individual bus frames to verify the sender's identity and ensure the integrity of the data payload.

## Parent Class(es)
- Message Authentication

## Relationships
- **authenticates:** Bus Message
- **kb-reference:** Reference - Controller area network message authentication - Ford Global Technologies LLC

## Knowledge Base Article
## How it works
Bus Message Authentication functions as a continuous validation layer that operates between the physical transmission of a signal and the application layer's processing of data. Every node on a bus network is provisioned with a cryptographic key and a synchronized 'freshness' state (such as a monotonic counter). When a node prepares to transmit, it generates a Message Authentication Code (MAC) which is created by hashing the message content, the sender's unique ID, and the current freshness value using its secret key. This MAC is then appended to the outgoing frame.

As messages circulate on the bus network, receiving nodes do not immediately trust the incoming data. Instead, a hardware controller intercepts the frame and performs a real-time parallel verification. The controller re-calculates the expected MAC based on its own copy of the key and the current network freshness state. If the received MAC matches the calculated one, the message is passed to the system for further action. If the MAC is missing, incorrect, or stale (indicating a replay of an older message), the hardware silently drops the frame or triggers a security alert.

## Considerations
* Bandwidth Overhead: Adding authentication tags (MACs) and freshness values reduces the effective data throughput; this requires a trade-off between the desired security level (tag length) and the available bus capacity.

* Real-Time Latency: Cryptographic processing must occur in hardware (e.g., via AES-NI, FPGA logic, or specialized ASICs) to meet the deterministic timing constraints of safety-critical systems.

* Key Management: A robust mechanism for secure key storage and lifecycle management (e.g., rotation and revocation) is required to ensure that a single compromised node does not jeopardize the entire network.

* Protocol Transparency: In legacy environments, authentication must often be implemented as a shim that remains compatible with existing protocol standards to avoid breaking legacy hardware.
