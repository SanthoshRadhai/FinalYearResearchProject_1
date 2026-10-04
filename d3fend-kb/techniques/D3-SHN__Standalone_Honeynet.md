# D3-SHN: Standalone Honeynet

**Reference:** https://d3fend.mitre.org/technique/D3-SHN/  

## Definition
An environment created for the purpose of attracting attackers and eliciting their behaviors that is not connected to any production enterprise systems.

## Parent Class(es)
- Decoy Environment

## Relationships
- **kb-reference:** Reference - Dynamic selection and generation of a virtual clone for detonation of suspicious content within a honey network - Palo Alto Networks Inc
- **spoofs:** Intranet Network

## Knowledge Base Article
## How it works
A standalone honeynet does not directly interact with the real enterprise environment. It may be located near or in some portion of the enterprise address space, but it does not interact with enterprise resources.

## Considerations
A standalone honeynet is a lower risk to deploy compared to connected or integrated honeynets due to its isolation from the enterprise network. However, this comes at cost in loss of fidelity and realism. Significant extra effort must be made in order to make the environment look realistic.
