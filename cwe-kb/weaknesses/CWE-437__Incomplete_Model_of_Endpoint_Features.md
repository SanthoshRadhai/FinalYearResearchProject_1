# CWE-437: Incomplete Model of Endpoint Features

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/437.html  

## Description
A product acts as an intermediary or monitor between two or more endpoints, but it does not have a complete model of an endpoint's features, behaviors, or state, potentially causing the product to perform incorrect actions based on this incomplete model.

## Related Weaknesses
- ChildOf: CWE-436

## Common Consequences
- Scope: Integrity, Other; Impact: Unexpected State, Varies by Context

## Demonstrative Examples (summary)
- HTTP request smuggling is an attack against an intermediary such as a proxy. This attack works because the proxy expects the client to parse HTTP headers one way, but the client parses them differently.
- Anti-virus products that reside on mail servers can suffer from this issue if they do not know how a mail client will handle a particular attachment. The product might treat an attachment type as safe, not knowing that the client's configuration treats it as executable.
