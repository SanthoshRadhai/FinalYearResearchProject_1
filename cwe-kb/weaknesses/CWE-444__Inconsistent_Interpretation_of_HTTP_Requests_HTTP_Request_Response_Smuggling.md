# CWE-444: Inconsistent Interpretation of HTTP Requests ('HTTP Request/Response Smuggling')

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/444.html  

## Description
The product acts as an intermediary HTTP agent (such as a proxy or firewall) in the data flow between two entities such as a client and server, but it does not interpret malformed HTTP requests or responses in ways that are consistent with how the messages will be processed by those entities that are at the ultimate destination.

## Extended Description
HTTP requests or responses ("messages") can be malformed or unexpected in ways that cause web servers or clients to interpret the messages in different ways than intermediary HTTP agents such as load balancers, reverse proxies, web caching proxies, application firewalls, etc. For example, an adversary may be able to add duplicate or different header fields that a client or server might interpret as one set of messages, whereas the intermediary might interpret the same sequence of bytes as a different set of messages. For example, discrepancies can arise in how to handle duplicate headers like two Transfer-encoding (TE) or two Content-length (CL), or the malicious HTTP message will have different headers for TE and CL. The inconsistent parsing and interpretation of messages can allow the adversary to "smuggle" a message to the client/server without the intermediary being aware of it. This weakness is usually the result of the usage of outdated or incompatible HTTP protocol versions in the HTTP agents.

## Related Weaknesses
- ChildOf: CWE-436
- ChildOf: CWE-436

## Common Consequences
- Scope: Integrity, Non-Repudiation, Access Control; Impact: Unexpected State, Hide Activities, Bypass Protection Mechanism — An attacker could create HTTP messages to exploit a number of weaknesses including 1) the message can trick the web server to associate a URL with another URL's webpage and caching the contents of the webpage (web cache poisoning attack), 2) the message can be structured to bypass the firewall protection mechanisms and gain unauthorized access to a web application, and 3) the message can invoke a script or a page that returns client credentials (similar to a Cross Site Scripting attack).

## Potential Mitigations
- [Implementation] Use a web server that employs a strict HTTP parsing procedure, such as Apache [REF-433].
- [Implementation] Use only SSL communication.
- [Implementation] Terminate the client session after each request.
- [System Configuration] Turn all pages to non-cacheable.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- In the following example, a malformed HTTP request is sent to a website that includes a proxy server and a web server with the intent of poisoning the cache to associate one webpage with another malicious webpage.
- In the following example, a malformed HTTP request is sent to a website that includes a web server with a firewall with the intent of bypassing the web server firewall to smuggle malicious code into the system.
- The interpretation of HTTP responses can be manipulated if response headers include a space between the header name and colon, or if HTTP 1.1 headers are sent through a proxy configured for HTTP 1.0, allowing for HTTP response smuggling. This can be exploited in web browsers and other applications when used in combination with various proxy servers. For instance, the HTTP response interpreted by the front-end/client HTTP agent/entity - in this case the web browser - can interpret a single response from an adversary-compromised web server as being two responses from two different web sites. In the Example below, notice the extra space after the Content-Length and Set-Cookie headers.
