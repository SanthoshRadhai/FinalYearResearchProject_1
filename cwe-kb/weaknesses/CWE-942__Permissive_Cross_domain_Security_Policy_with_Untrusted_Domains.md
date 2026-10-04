# CWE-942: Permissive Cross-domain Security Policy with Untrusted Domains

**Abstraction:** Variant  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/942.html  

## Description
The product uses a web-client protection mechanism such as a Content Security Policy (CSP) or cross-domain policy file, but the policy includes untrusted domains with which the web client is allowed to communicate.

## Extended Description
If a cross-domain policy file includes domains that should not be trusted, such as when using wildcards under a high-level domain, then the application could be attacked by these untrusted domains. In many cases, the attack can be launched without the victim even being aware of it.

## Related Weaknesses
- ChildOf: CWE-863
- ChildOf: CWE-923
- ChildOf: CWE-183
- CanPrecede: CWE-668

## Common Consequences
- Scope: Confidentiality, Integrity, Availability, Access Control; Impact: Execute Unauthorized Code or Commands, Bypass Protection Mechanism, Read Application Data, Varies by Context — With an overly permissive policy file, an attacker may be able to bypass the web browser's same-origin policy and conduct many of the same attacks seen in Cross-Site Scripting (CWE-79). An attacker can exploit the weakness to transfer private information from the victim's machine to the attacker, manipulate or steal cookies that may include session information, create malicious requests to a web site on behalf of the victim, or execute malicious code on the end user systems. Other damaging attacks include the disclosure of end user files, installation of Trojan horse programs, redirecting the user to some other page or site, running ActiveX controls (under Microsoft Internet Explorer) from sites that a user perceives as trustworthy, and modifying presentation of content.

## Potential Mitigations
- [Architecture and Design, Operation] Define a restrictive Content Security Policy [REF-1486] or cross-domain policy file.
- [Architecture and Design, Operation] Avoid using wildcards in the CSP / cross-domain policy file. Any domain matching the wildcard expression will be implicitly trusted, and can perform two-way interaction with the target server.
- [Architecture and Design, Operation] For Flash, modify crossdomain.xml to use meta-policy options such as 'master-only' or 'none' to reduce the possibility of an attacker planting extraneous cross-domain policy files on a server.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- These cross-domain policy files mean to allow Flash and Silverlight applications hosted on other domains to access its data:
