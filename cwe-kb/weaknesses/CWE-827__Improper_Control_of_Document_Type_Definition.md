# CWE-827: Improper Control of Document Type Definition

**Abstraction:** Variant  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/827.html  

## Description
The product does not restrict a reference to a Document Type Definition (DTD) to the intended control sphere. This might allow attackers to reference arbitrary DTDs, possibly causing the product to expose files, consume excessive system resources, or execute arbitrary http requests on behalf of the attacker.

## Extended Description
As DTDs are processed, they might try to read or include files on the machine performing the parsing. If an attacker is able to control the DTD, then the attacker might be able to specify sensitive resources or requests or provide malicious content. For example, the SOAP specification prohibits SOAP messages from containing DTDs.

## Related Weaknesses
- ChildOf: CWE-706
- ChildOf: CWE-829
- CanPrecede: CWE-776

## Common Consequences
- Scope: Confidentiality; Impact: Read Files or Directories — If the attacker is able to include a crafted DTD and a default entity resolver is enabled, the attacker may be able to access arbitrary files on the system.
- Scope: Availability; Impact: DoS: Resource Consumption (CPU), DoS: Resource Consumption (Memory) — The DTD may cause the parser to consume excessive CPU cycles or memory using techniques such as nested or recursive entity references (CWE-776).
- Scope: Integrity, Confidentiality, Availability, Access Control; Impact: Execute Unauthorized Code or Commands, Gain Privileges or Assume Identity — The DTD may include arbitrary HTTP requests that the server may execute. This could lead to other attacks leveraging the server's trust relationship with other entities.
