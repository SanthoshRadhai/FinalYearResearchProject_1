# CWE-420: Unprotected Alternate Channel

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/420.html  

## Description
The product protects a primary channel, but it does not use the same level of protection for an alternate channel.

## Related Weaknesses
- ChildOf: CWE-923

## Common Consequences
- Scope: Access Control; Impact: Gain Privileges or Assume Identity, Bypass Protection Mechanism

## Potential Mitigations
- [Architecture and Design] Identify all alternate channels and use the same protection mechanisms that are used for the primary channels.

## Demonstrative Examples (summary)
- Register SECURE_ME is located at address 0xF00. A mirror of this register called COPY_OF_SECURE_ME is at location 0x800F00. The register SECURE_ME is protected from malicious agents and only allows access to select, while COPY_OF_SECURE_ME is not. Access control is implemented using an allowlist (as indicated by acl_oh_allowlist). The identity of the initiator of the transaction is indicated by the one hot input, incoming_id. This is checked against the acl_oh_allowlist (which contains a list of initiators that are allowed to access the asset). Though this example is shown in Verilog, it will apply to VHDL as well.
