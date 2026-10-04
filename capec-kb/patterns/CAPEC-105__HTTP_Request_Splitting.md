# CAPEC-105: HTTP Request Splitting

**Abstraction:** Detailed  
**Status:** Stable  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/105.html  

## Description
An adversary abuses the flexibility and discrepancies in the parsing and interpretation of HTTP Request messages by different intermediary HTTP agents (e.g., load balancer, reverse proxy, web caching proxies, application firewalls, etc.) to split a single HTTP request into multiple unauthorized and malicious HTTP requests to a back-end HTTP agent (e.g., web server). See CanPrecede relationships for possible consequences.

## Related Attack Patterns
- ChildOf: CAPEC-220
- PeerOf: CAPEC-34
- CanPrecede: CAPEC-115
- CanPrecede: CAPEC-141
- CanPrecede: CAPEC-63
- CanPrecede: CAPEC-593
- CanPrecede: CAPEC-148
- CanPrecede: CAPEC-154

## Prerequisites
- An additional intermediary HTTP agent such as an application firewall or a web caching proxy between the adversary and the second agent such as a web server, that sends multiple HTTP messages over same network connection.
- Differences in the way the two HTTP agents parse and interpret HTTP requests and its headers.
- HTTP headers capable of being user-manipulated.
- HTTP agents running on HTTP/1.0 or HTTP/1.1 that allow for Keep Alive mode, Pipelined queries, and Chunked queries and responses.

## Skills Required
- [Medium] Detailed knowledge on HTTP protocol: request and response messages structure and usage of specific headers.
- [Medium] Detailed knowledge on how specific HTTP agents receive, send, process, interpret, and parse a variety of HTTP messages and headers.
- [Medium] Possess knowledge on the exact details in the discrepancies between several targeted HTTP agents in path of an HTTP message in parsing its message structure and individual headers.

## Resources Required
- Tools capable of crafting malicious HTTP messages and monitoring HTTP messages responses.

## Consequences
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges
- Scope: Confidentiality; Impact: Read Data
- Scope: Integrity; Impact: Modify Data

## Mitigations
- Design: evaluate HTTP agents prior to deployment for parsing/interpretation discrepancies.
- Configuration: front-end HTTP agents notice ambiguous requests.
- Configuration: back-end HTTP agents reject ambiguous requests and close the network connection.
- Configuration: Disable reuse of back-end connections.
- Configuration: Use HTTP/2 for back-end connections.
- Configuration: Use the same web server software for front-end and back-end server.
- Implementation: Utilize a Web Application Firewall (WAF) that has built-in mitigation to detect abnormal requests/responses.
- Configuration: Install latest vendor security patches available for both intermediary and back-end HTTP infrastructure (i.e. proxies and web servers)
- Configuration: Ensure that HTTP infrastructure in the chain or network path utilize a strict uniform parsing process.
- Implementation: Utilize intermediary HTTP infrastructure capable of filtering and/or sanitizing user-input.

## Related Weaknesses (CWE)
- CWE-74
- CWE-113
- CWE-138
- CWE-436
