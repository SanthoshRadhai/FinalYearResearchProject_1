# CAPEC-273: HTTP Response Smuggling

**Abstraction:** Detailed  
**Status:** Stable  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/273.html  

## Description
An adversary manipulates and injects malicious content in the form of secret unauthorized HTTP responses, into a single HTTP response from a vulnerable or compromised back-end HTTP agent (e.g., server). See CanPrecede relationships for possible consequences.

## Related Attack Patterns
- ChildOf: CAPEC-220
- PeerOf: CAPEC-33
- CanPrecede: CAPEC-115
- CanPrecede: CAPEC-141
- CanPrecede: CAPEC-63
- CanPrecede: CAPEC-593
- CanPrecede: CAPEC-148
- CanPrecede: CAPEC-154

## Prerequisites
- A vulnerable or compromised server or domain/site capable of allowing adversary to insert/inject malicious content that will appear in the server's response to target HTTP agents (e.g., proxies and users' web browsers).
- Differences in the way the two HTTP agents parse and interpret HTTP responses and its headers.
- HTTP agents running on HTTP/1.1 that allow for Keep Alive mode, Pipelined queries, and Chunked queries and responses.

## Skills Required
- [Medium] Detailed knowledge on HTTP protocol: request and response messages structure and usage of specific headers.
- [Medium] Detailed knowledge on how specific HTTP agents receive, send, process, interpret, and parse a variety of HTTP messages and headers.
- [Medium] Possess knowledge on the exact details in the discrepancies between several targeted HTTP agents in path of an HTTP message in parsing its message structure and individual headers.

## Resources Required
- Tools capable of monitoring HTTP messages, and crafting malicious HTTP messages and/or injecting malicious content into HTTP messages.

## Consequences
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges
- Scope: Integrity; Impact: Modify Data

## Mitigations
- Design: evaluate HTTP agents prior to deployment for parsing/interpretation discrepancies.
- Configuration: front-end HTTP agents notice ambiguous requests.
- Configuration: back-end HTTP agents reject ambiguous requests and close the network connection.
- Configuration: Disable reuse of back-end connections.
- Configuration: Use HTTP/2 for back-end connections.
- Configuration: Use the same web server software for front-end and back-end server.
- Implementation: Utilize a Web Application Firewall (WAF) that has built-in mitigation to detect abnormal requests/responses.
- Configuration: Prioritize Transfer-Encoding header over Content-Length, whenever an HTTP message contains both.
- Configuration: Disallow HTTP messages with both Transfer-Encoding and Content-Length or Double Content-Length Headers.
- Configuration: Disallow Malformed/Invalid Transfer-Encoding Headers used in obfuscation, such as: Headers with no space before the value “chunked” Headers with extra spaces Headers beginning with trailing characters Headers providing a value “chunk” instead of “chunked” (the server normalizes this as chunked encoding) Headers with multiple spaces before the value “chunked” Headers with quoted values (whether single or double quotations) Headers with CRLF characters before the value “chunked” Values with invalid characters
- Configuration: Install latest vendor security patches available for both intermediary and back-end HTTP infrastructure (i.e. proxies and web servers)
- Configuration: Ensure that HTTP infrastructure in the chain or network path utilize a strict uniform parsing process.
- Implementation: Utilize intermediary HTTP infrastructure capable of filtering and/or sanitizing user-input.

## Related Weaknesses (CWE)
- CWE-74
- CWE-436
- CWE-444
