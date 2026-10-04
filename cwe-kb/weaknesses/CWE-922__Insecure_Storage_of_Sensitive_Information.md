# CWE-922: Insecure Storage of Sensitive Information

**Abstraction:** Class  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/922.html  

## Description
The product stores sensitive information without properly limiting read or write access by unauthorized actors.

## Extended Description
If read access is not properly restricted, then attackers can steal the sensitive information. If write access is not properly restricted, then attackers can modify and possibly delete the data, causing incorrect results and possibly a denial of service.

## Related Weaknesses
- ChildOf: CWE-664

## Common Consequences
- Scope: Confidentiality; Impact: Read Application Data, Read Files or Directories — Attackers can read sensitive information by accessing the unrestricted storage mechanism.
- Scope: Integrity; Impact: Modify Application Data, Modify Files or Directories — Attackers can overwrite sensitive information by accessing the unrestricted storage mechanism.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- In 2022, the OT:ICEFALL study examined products by 10 different Operational Technology (OT) vendors. The researchers reported 56 vulnerabilities and said that the products were "insecure by design" [REF-1283]. If exploited, these vulnerabilities often allowed adversaries to change how the products operated, ranging from denial of service to changing the code that the products executed. Since these products were often used in industries such as power, electrical, water, and others, there could even be safety implications.
