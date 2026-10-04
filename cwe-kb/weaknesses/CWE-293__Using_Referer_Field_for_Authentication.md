# CWE-293: Using Referer Field for Authentication

**Abstraction:** Variant  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/293.html  

## Description
The referer field in HTTP requests can be easily modified and, as such, is not a valid means of message integrity checking.

## Related Weaknesses
- ChildOf: CWE-290

## Common Consequences
- Scope: Access Control; Impact: Gain Privileges or Assume Identity — Actions, which may not be authorized otherwise, can be carried out as if they were validated by the server referred to.

## Potential Mitigations
- [Architecture and Design] In order to usefully check if a given action is authorized, some means of strong authentication and method protection must be used. Use other means of authorization that cannot be simply spoofed. Possibilities include a username/password or certificate.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- The following code samples check a packet's referer in order to decide whether or not an inbound request is from a trusted host.
