# CWE-12: ASP.NET Misconfiguration: Missing Custom Error Page

**Abstraction:** Variant  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/12.html  

## Description
An ASP .NET application must enable custom error pages in order to prevent attackers from mining information from the framework's built-in responses.

## Related Weaknesses
- ChildOf: CWE-756

## Common Consequences
- Scope: Confidentiality; Impact: Read Application Data — Default error pages gives detailed information about the error that occurred, and should not be used in production environments. Attackers can leverage the additional information provided by a default error page to mount attacks targeted on the framework, database, or other resources used by the application.

## Potential Mitigations
- [System Configuration] Handle exceptions appropriately in source code. ASP .NET applications should be configured to use custom error pages instead of the framework default page.
- [Architecture and Design] Do not attempt to process an error or attempt to mask it.
- [Implementation] Verify return values are correct and do not supply sensitive information about the system.

## Demonstrative Examples (summary)
- The mode attribute of the <customErrors> tag in the Web.config file defines whether custom or default error pages are used.
