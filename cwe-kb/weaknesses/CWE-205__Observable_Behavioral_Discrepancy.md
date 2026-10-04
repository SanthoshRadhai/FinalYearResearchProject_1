# CWE-205: Observable Behavioral Discrepancy

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/205.html  

## Description
The product's behaviors indicate important differences that may be observed by unauthorized actors in a way that reveals (1) its internal state or decision process, or (2) differences from other products with equivalent functionality.

## Extended Description
Ideally, a product should provide as little information about its internal operations as possible. Otherwise, attackers could use knowledge of these internal operations to simplify or optimize their attack. In some cases, behavioral discrepancies can be used by attackers to form a side channel.

## Related Weaknesses
- ChildOf: CWE-203
- CanPrecede: CWE-514

## Common Consequences
- Scope: Confidentiality, Access Control; Impact: Read Application Data, Bypass Protection Mechanism
