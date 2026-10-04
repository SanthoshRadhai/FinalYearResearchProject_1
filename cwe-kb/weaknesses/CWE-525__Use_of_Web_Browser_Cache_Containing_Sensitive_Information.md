# CWE-525: Use of Web Browser Cache Containing Sensitive Information

**Abstraction:** Variant  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/525.html  

## Description
The web application does not use an appropriate caching policy that specifies the extent to which each web page and associated form fields should be cached.

## Related Weaknesses
- ChildOf: CWE-524

## Common Consequences
- Scope: Confidentiality; Impact: Read Application Data — Browsers often store information in a client-side cache, which can leave behind sensitive information for other users to find and exploit, such as passwords or credit card numbers. The locations at most risk include public terminals, such as those in libraries and Internet cafes.

## Potential Mitigations
- [Architecture and Design] Protect information stored in cache.
- [Implementation] Use a restrictive caching policy for forms and web pages that potentially contain sensitive information, such as "no-cache" in the Cache-Control header.
- [Architecture and Design] Do not store unnecessarily sensitive information in the cache.
- [Architecture and Design] Consider using encryption in the cache.
