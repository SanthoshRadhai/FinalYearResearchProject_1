# CWE-647: Use of Non-Canonical URL Paths for Authorization Decisions

**Abstraction:** Variant  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/647.html  

## Description
The product defines policy namespaces and makes authorization decisions based on the assumption that a URL is canonical. This can allow a non-canonical URL to bypass the authorization.

## Extended Description
If an application defines policy namespaces and makes authorization decisions based on the URL, but it does not require or convert to a canonical URL before making the authorization decision, then it opens the application to attack. For example, if the application only wants to allow access to http://www.example.com/mypage, then the attacker might be able to bypass this restriction using equivalent URLs such as: http://WWW.EXAMPLE.COM/mypage http://www.example.com/%6Dypage (alternate encoding) http://192.168.1.1/mypage (IP address) http://www.example.com/mypage/ (trailing /) http://www.example.com:80/mypage Therefore it is important to specify access control policy that is based on the path information in some canonical form with all alternate encodings rejected (which can be accomplished by a default deny rule).

## Related Weaknesses
- ChildOf: CWE-863
- ChildOf: CWE-180

## Common Consequences
- Scope: Access Control; Impact: Bypass Protection Mechanism — An attacker may be able to bypass the authorization mechanism to gain access to the otherwise-protected URL.
- Scope: Confidentiality; Impact: Read Files or Directories — If a non-canonical URL is used, the server may choose to return the contents of the file, instead of pre-processing the file (e.g. as a program).

## Potential Mitigations
- [Architecture and Design] Make access control policy based on path information in canonical form. Use very restrictive regular expressions to validate that the path is in the expected form.
- [Architecture and Design] Reject all alternate path encodings that are not in the expected canonical form.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- Example from CAPEC (CAPEC ID: 4, "Using Alternative IP Address Encodings"). An attacker identifies an application server that applies a security policy based on the domain and application name, so the access control policy covers authentication and authorization for anyone accessing http://example.domain:8080/application. However, by putting in the IP address of the host the application authentication and authorization controls may be bypassed http://192.168.0.1:8080/application. The attacker relies on the victim applying policy to the namespace abstraction and not having a default deny policy in place to manage exceptions.
