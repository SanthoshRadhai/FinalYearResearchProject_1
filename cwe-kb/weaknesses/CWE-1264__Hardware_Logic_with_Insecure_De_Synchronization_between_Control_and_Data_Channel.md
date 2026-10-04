# CWE-1264: Hardware Logic with Insecure De-Synchronization between Control and Data Channels

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/1264.html  

## Description
The hardware logic for error handling and security checks can incorrectly forward data before the security check is complete.

## Extended Description
Many high-performance on-chip bus protocols and processor data-paths employ separate channels for control and data to increase parallelism and maximize throughput. Bugs in the hardware logic that handle errors and security checks can make it possible for data to be forwarded before the completion of the security checks. If the data can propagate to a location in the hardware observable to an attacker, loss of data confidentiality can occur. 'Meltdown' is a concrete example of how de-synchronization between data and permissions checking logic can violate confidentiality requirements. Data loaded from a page marked as privileged was returned to the CPU regardless of current privilege level for performance reasons. The assumption was that the CPU could later remove all traces of this data during the handling of the illegal memory access exception, but this assumption was proven false as traces of the secret data were not removed from the microarchitectural state.

## Related Weaknesses
- ChildOf: CWE-821
- PeerOf: CWE-1037

## Common Consequences
- Scope: Confidentiality; Impact: Read Memory, Read Application Data

## Potential Mitigations
- [Architecture and Design] Thoroughly verify the data routing logic to ensure that any error handling or security checks effectively block illegal dataflows.

## Demonstrative Examples (summary)
- There are several standard on-chip bus protocols used in modern SoCs to allow communication between components. There are a wide variety of commercially available hardware IP implementing the interconnect logic for these protocols. A bus connects components which initiate/request communications such as processors and DMA controllers (bus masters) with peripherals which respond to requests. In a typical system, the privilege level or security designation of the bus master along with the intended functionality of each peripheral determine the security policy specifying which specific bus masters can access specific peripherals. This security policy (commonly referred to as a bus firewall) can be enforced using separate IP/logic from the actual interconnect responsible for the data routing.
