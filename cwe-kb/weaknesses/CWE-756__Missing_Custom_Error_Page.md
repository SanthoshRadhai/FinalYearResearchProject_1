# CWE-756: Missing Custom Error Page

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/756.html  

## Description
The product does not return custom error pages to the user, possibly exposing sensitive information.

## Related Weaknesses
- ChildOf: CWE-755
- CanPrecede: CWE-209

## Common Consequences
- Scope: Confidentiality; Impact: Read Application Data — Attackers can leverage the additional information provided by a default error page to mount attacks targeted on the framework, database, or other resources used by the application.

## Demonstrative Examples (summary)
- In the snippet below, an unchecked runtime exception thrown from within the try block may cause the container to display its default error page (which may contain a full stack trace, among other things).
- The mode attribute of the <customErrors> tag in the Web.config file defines whether custom or default error pages are used.
