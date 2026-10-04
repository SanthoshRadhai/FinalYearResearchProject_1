# CWE-459: Incomplete Cleanup

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/459.html  

## Description
The product does not properly "clean up" and remove temporary or supporting resources after they have been used.

## Related Weaknesses
- ChildOf: CWE-404
- ChildOf: CWE-404

## Common Consequences
- Scope: Other, Confidentiality, Integrity; Impact: Other, Read Application Data, Modify Application Data, DoS: Resource Consumption (Other) — It is possible to overflow the number of temporary files because directories typically have limits on the number of files allowed. This could create a denial of service problem.

## Potential Mitigations
- [Architecture and Design, Implementation] Temporary files and other supporting resources should be deleted/released immediately after they are no longer needed.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- Stream resources in a Java application should be released in a finally block, otherwise an exception thrown before the call to close() would result in an unreleased I/O resource. In the example below, the close() method is called in the try block (incorrect).
