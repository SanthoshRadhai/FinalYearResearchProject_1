# CWE-600: Uncaught Exception in Servlet

**Abstraction:** Variant  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/600.html  

## Description
The Servlet does not catch all exceptions, which may reveal sensitive debugging information.

## Extended Description
When a Servlet throws an exception, the default error response the Servlet container sends back to the user typically includes debugging information. This information is of great value to an attacker. For example, a stack trace might show the attacker a malformed SQL query string, the type of database being used, and the version of the application container. This information enables the attacker to target known vulnerabilities in these components.

## Related Weaknesses
- ChildOf: CWE-248
- CanPrecede: CWE-209
- PeerOf: CWE-390

## Common Consequences
- Scope: Confidentiality, Availability; Impact: Read Application Data, DoS: Crash, Exit, or Restart

## Potential Mitigations
- [Implementation] Implement Exception blocks to handle all types of Exceptions.

## Demonstrative Examples (summary)
- The following example attempts to resolve a hostname.
