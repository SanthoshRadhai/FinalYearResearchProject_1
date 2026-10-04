# CWE-1327: Binding to an Unrestricted IP Address

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/1327.html  

## Description
The product assigns the address 0.0.0.0 for a database server, a cloud service/instance, or any computing resource that communicates remotely.

## Extended Description
When a server binds to the address 0.0.0.0, it allows connections from every IP address on the local machine, effectively exposing the server to every possible network. This might be much broader access than intended by the developer or administrator, who might only be expecting the server to be reachable from a single interface/network.

## Related Weaknesses
- ChildOf: CWE-668

## Common Consequences
- Scope: Availability; Impact: DoS: Amplification

## Potential Mitigations
- [System Configuration] Assign IP addresses that are not 0.0.0.0.
- [System Configuration] Unwanted connections to the configured server may be denied through a firewall or other packet filtering measures.

## Demonstrative Examples (summary)
- The following code snippet uses 0.0.0.0 in a Puppet script.
