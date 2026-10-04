# CWE-1004: Sensitive Cookie Without 'HttpOnly' Flag

**Abstraction:** Variant  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/1004.html  

## Description
The product uses a cookie to store sensitive information, but the cookie is not marked with the HttpOnly flag.

## Related Weaknesses
- ChildOf: CWE-732

## Common Consequences
- Scope: Confidentiality; Impact: Read Application Data — If the HttpOnly flag is not set, then sensitive information stored in the cookie may be exposed to unintended parties.
- Scope: Integrity; Impact: Gain Privileges or Assume Identity — If the cookie in question is an authentication cookie, then not setting the HttpOnly flag may allow an adversary to steal authentication data (e.g., a session ID) and assume the identity of the user.

## Potential Mitigations
- [Implementation] Leverage the HttpOnly flag when setting a sensitive cookie in a response.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- In this example, a cookie is used to store a session ID for a client's interaction with a website. The intention is that the cookie will be sent to the website with each request made by the client.
