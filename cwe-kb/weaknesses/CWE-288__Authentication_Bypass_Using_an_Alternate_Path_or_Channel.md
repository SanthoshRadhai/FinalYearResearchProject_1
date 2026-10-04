# CWE-288: Authentication Bypass Using an Alternate Path or Channel

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/288.html  

## Description
The product requires authentication, but the product has an alternate path or channel that does not require authentication.

## Related Weaknesses
- ChildOf: CWE-306
- ChildOf: CWE-284
- PeerOf: CWE-420

## Common Consequences
- Scope: Access Control; Impact: Bypass Protection Mechanism

## Potential Mitigations
- [Architecture and Design] Funnel all access through a single choke point to simplify how users can access a resource. For every access, perform a check to determine if the user has permissions to access the resource.

## Demonstrative Examples (summary)
- Register SECURE_ME is located at address 0xF00. A mirror of this register called COPY_OF_SECURE_ME is at location 0x800F00. The register SECURE_ME is protected from malicious agents and only allows access to select, while COPY_OF_SECURE_ME is not. Access control is implemented using an allowlist (as indicated by acl_oh_allowlist). The identity of the initiator of the transaction is indicated by the one hot input, incoming_id. This is checked against the acl_oh_allowlist (which contains a list of initiators that are allowed to access the asset). Though this example is shown in Verilog, it will apply to VHDL as well.
