# CWE-579: J2EE Bad Practices: Non-serializable Object Stored in Session

**Abstraction:** Variant  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/579.html  

## Description
The product stores a non-serializable object as an HttpSession attribute, which can hurt reliability.

## Extended Description
A J2EE application can make use of multiple JVMs in order to improve application reliability and performance. In order to make the multiple JVMs appear as a single application to the end user, the J2EE container can replicate an HttpSession object across multiple JVMs so that if one JVM becomes unavailable another can step in and take its place without disrupting the flow of the application. This is only possible if all session data is serializable, allowing the session to be duplicated between the JVMs.

## Related Weaknesses
- ChildOf: CWE-573

## Common Consequences
- Scope: Other; Impact: Quality Degradation

## Potential Mitigations
- [Implementation] In order for session replication to work, the values the product stores as attributes in the session must implement the Serializable interface.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- The following class adds itself to the session, but because it is not serializable, the session can no longer be replicated.
