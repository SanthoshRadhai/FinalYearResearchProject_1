# CWE-433: Unparsed Raw Web Content Delivery

**Abstraction:** Variant  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/433.html  

## Description
The product stores raw content or supporting code under the web document root with an extension that is not specifically handled by the server.

## Extended Description
If code is stored in a file with an extension such as ".inc" or ".pl", and the web server does not have a handler for that extension, then the server will likely send the contents of the file directly to the requester without the pre-processing that was expected. When that file contains sensitive information such as database credentials, this may allow the attacker to compromise the application or associated components.

## Related Weaknesses
- ChildOf: CWE-219

## Common Consequences
- Scope: Confidentiality; Impact: Read Application Data

## Potential Mitigations
- [Architecture and Design] Perform a type check before interpreting files.
- [Architecture and Design] Do not store sensitive information in files which may be misinterpreted.

## Demonstrative Examples (summary)
- The following code uses an include file to store database credentials:
