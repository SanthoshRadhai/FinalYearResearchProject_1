# CWE-636: Not Failing Securely ('Failing Open')

**Abstraction:** Class  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/636.html  

## Description
When the product encounters an error condition or failure, its design requires it to fall back to a state that is less secure than other options that are available, such as selecting the weakest encryption algorithm or using the most permissive access control restrictions.

## Extended Description
By entering a less secure state, the product inherits the weaknesses associated with that state, making it easier to compromise. At the least, it causes administrators to have a false sense of security. This weakness typically occurs as a result of wanting to "fail functional" to minimize administration and support costs, instead of "failing safe."

## Related Weaknesses
- ChildOf: CWE-657
- ChildOf: CWE-755
- PeerOf: CWE-280

## Common Consequences
- Scope: Access Control; Impact: Bypass Protection Mechanism — Intended access restrictions can be bypassed, which is often contradictory to what the product's administrator expects.

## Potential Mitigations
- [Architecture and Design] Subdivide and allocate resources and components so that a failure in one part does not affect the entire product.

## Demonstrative Examples (summary)
- Switches may revert their functionality to that of hubs when the table used to map ARP information to the switch interface overflows, such as when under a spoofing attack. This results in traffic being broadcast to an eavesdropper, instead of being sent only on the relevant switch interface. To mitigate this type of problem, the developer could limit the number of ARP entries that can be recorded for a given switch interface, while other interfaces may keep functioning normally. Configuration options can be provided on the appropriate actions to be taken in case of a detected failure, but safe defaults should be used.
