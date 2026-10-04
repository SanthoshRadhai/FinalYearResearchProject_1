# CWE-431: Missing Handler

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/431.html  

## Description
A handler is not available or implemented.

## Extended Description
When an exception is thrown and not caught, the process has given up an opportunity to decide if a given failure or event is worth a change in execution.

## Related Weaknesses
- ChildOf: CWE-691
- CanPrecede: CWE-433

## Common Consequences
- Scope: Other; Impact: Varies by Context

## Potential Mitigations
- [Implementation] Handle all possible situations (e.g. error condition).
- [Implementation] If an operation can throw an Exception, implement a handler for that specific exception.

## Demonstrative Examples (summary)
- If a Servlet does not catch all exceptions, it may reveal debugging information that will help an adversary form a plan of attack. In the following method a DNS lookup failure will cause the Servlet to throw an exception.
