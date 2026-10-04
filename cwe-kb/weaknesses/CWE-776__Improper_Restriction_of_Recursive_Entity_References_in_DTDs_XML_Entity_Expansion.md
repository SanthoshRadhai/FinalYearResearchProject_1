# CWE-776: Improper Restriction of Recursive Entity References in DTDs ('XML Entity Expansion')

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/776.html  

## Description
The product uses XML documents and allows their structure to be defined with a Document Type Definition (DTD), but it does not properly control the number of recursive definitions of entities.

## Extended Description
If the DTD contains a large number of nested or recursive entities, this can lead to explosive growth of data when parsed, causing a denial of service.

## Related Weaknesses
- ChildOf: CWE-674
- ChildOf: CWE-674
- ChildOf: CWE-405

## Common Consequences
- Scope: Availability; Impact: DoS: Resource Consumption (Other) — If parsed, recursive entity references allow the attacker to expand data exponentially, quickly consuming all system resources.

## Potential Mitigations
- [Operation] If possible, prohibit the use of DTDs or use an XML parser that limits the expansion of recursive DTD entities.
- [Implementation] Before parsing XML files with associated DTDs, scan for recursive entity declarations and do not continue parsing potentially explosive content.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- The DTD and the very brief XML below illustrate what is meant by an XML bomb. The ZERO entity contains one character, the letter A. The choice of entity name ZERO is being used to indicate length equivalent to that exponent on two, that is, the length of ZERO is 2^0. Similarly, ONE refers to ZERO twice, therefore the XML parser will expand ONE to a length of 2, or 2^1. Ultimately, we reach entity THIRTYTWO, which will expand to 2^32 characters in length, or 4 GB, probably consuming far more data than expected.
