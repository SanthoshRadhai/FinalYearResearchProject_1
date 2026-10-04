# CWE-488: Exposure of Data Element to Wrong Session

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/488.html  

## Description
The product does not sufficiently enforce boundaries between the states of different sessions, causing data to be provided to, or used by, the wrong session.

## Extended Description
Data can "bleed" from one session to another through member variables of singleton objects, such as Servlets, and objects from a shared pool. In the case of Servlets, developers sometimes do not understand that, unless a Servlet implements the SingleThreadModel interface, the Servlet is a singleton; there is only one instance of the Servlet, and that single instance is used and re-used to handle multiple requests that are processed simultaneously by different threads. A common result is that developers use Servlet member fields in such a way that one user may inadvertently see another user's data. In other words, storing user data in Servlet member fields introduces a data access race condition.

## Related Weaknesses
- ChildOf: CWE-668

## Common Consequences
- Scope: Confidentiality; Impact: Read Application Data

## Potential Mitigations
- [Architecture and Design] Protect the application's sessions from information leakage. Make sure that a session's data is not used or visible by other sessions.
- [Testing] Use a static analysis tool to scan the code for information leakage vulnerabilities (e.g. Singleton Member Field).
- [Architecture and Design] In a multithreading environment, storing user data in Servlet member fields introduces a data access race condition. Do not use member fields to store information in the Servlet.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- The following Servlet stores the value of a request parameter in a member field and then later echoes the parameter value to the response output stream.
