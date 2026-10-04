# CWE-1275: Sensitive Cookie with Improper SameSite Attribute

**Abstraction:** Variant  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/1275.html  

## Description
The SameSite attribute for sensitive cookies is not set, or an insecure value is used.

## Extended Description
The SameSite attribute controls how cookies are sent for cross-domain requests. This attribute may have three values: 'Lax', 'Strict', or 'None'. If the 'None' value is used, a website may create a cross-domain POST HTTP request to another website, and the browser automatically adds cookies to this request. This may lead to Cross-Site-Request-Forgery (CSRF) attacks if there are no additional protections in place (such as Anti-CSRF tokens).

## Related Weaknesses
- ChildOf: CWE-923
- CanPrecede: CWE-352

## Common Consequences
- Scope: Confidentiality, Integrity, Non-Repudiation, Access Control; Impact: Modify Application Data — If the website does not impose additional defense against CSRF attacks, failing to use the 'Lax' or 'Strict' values could increase the risk of exposure to CSRF attacks. The likelihood of the integrity breach is Low because a successful attack does not only depend on an insecure SameSite attribute. In order to perform a CSRF attack there are many conditions that must be met, such as the lack of CSRF tokens, no confirmations for sensitive actions on the website, a "simple" "Content-Type" header in the HTTP request and many more.

## Potential Mitigations
- [Implementation] Set the SameSite attribute of a sensitive cookie to 'Lax' or 'Strict'. This instructs the browser to apply this cookie only to same-domain requests, which provides a good Defense in Depth against CSRF attacks. When the 'Lax' value is in use, cookies are also sent for top-level cross-domain navigation via HTTP GET, HEAD, OPTIONS, and TRACE methods, but not for other HTTP methods that are more like to cause side-effects of state mutation.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- In this example, a cookie is used to store a session ID for a client's interaction with a website. The snippet of code below establishes a new cookie to hold the sessionID.
