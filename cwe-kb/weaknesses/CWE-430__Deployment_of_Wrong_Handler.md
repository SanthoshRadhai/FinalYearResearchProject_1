# CWE-430: Deployment of Wrong Handler

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/430.html  

## Description
The wrong "handler" is assigned to process an object.

## Extended Description
An example of deploying the wrong handler would be calling a servlet to reveal source code of a .JSP file, or automatically "determining" type of the object even if it is contradictory to an explicitly specified type.

## Related Weaknesses
- ChildOf: CWE-691
- CanPrecede: CWE-433
- PeerOf: CWE-434

## Common Consequences
- Scope: Integrity, Other; Impact: Varies by Context, Unexpected State

## Potential Mitigations
- [Architecture and Design] Perform a type check before interpreting an object.
- [Architecture and Design] Reject any inconsistent types, such as a file with a .GIF extension that appears to consist of PHP code.
