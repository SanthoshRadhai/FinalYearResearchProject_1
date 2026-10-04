# D3-OVAR: OT Variable Access Restriction

**Synonym(s):** OT Variable Access Policy  
**Reference:** https://d3fend.mitre.org/technique/D3-OVAR/  

## Definition
Assign read/write access controls on designated registers or data tags to prevent unauthorized writes.

## Parent Class(es)
- Access Mediation

## Relationships
- **enables:** Isolate
- **kb-reference:** Reference - PLX3x Series Multi-Protocol Gateways
- **kb-reference:** Reference - S7-1200 Programmable controller
- **kb-reference:** Reference - Secure PLC Coding Practices: Top 20 List
- **limits:** OT Logic Variable
- **restricts:** OT Write Command

## Knowledge Base Article
 ## How it works

Many OT Controllers and OT Communication Modules enable Read-Only or Read/Write access on a per-tag basis.

As an example, when configuring OT process tags which can be accessed using the Modbus protocol, configure the tag to a Modbus Input Register to leverage the protocol's registry ranges, restricting the ability of external sources to modify data.

In Siemens, each data block (DB) tag can be configured as "data block write-protected in the device."
