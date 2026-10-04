# D3-OPR: Operating Mode Restriction

**Reference:** https://d3fend.mitre.org/technique/D3-OPR/  

## Definition
Restricting unauthorized changes to the operating mode prevents devices from switching into inappropriate or vulnerable states during normal use.

## Parent Class(es)
- Access Mediation

## Relationships
- **kb-reference:** Reference - MITRE ATT&CK - Authorization Enforcement
- **kb-reference:** Reference - TRITON Malware Remains Threat to Global Critical Infrastructure Industrial Control Systems (ICS)
- **restricts:** OT Controller Operating Mode

## Knowledge Base Article
## How it works
Many OT Controllers use key switches to change the controller into different modes of operation. These modes of operation can include Program, Run, Remote, or Stop.

The key switch should be left in the appropriate key switch position, e.g., run or remote during normal operations.

Implement a key management procedure to include removing the physical key from the key switch when not in use.
