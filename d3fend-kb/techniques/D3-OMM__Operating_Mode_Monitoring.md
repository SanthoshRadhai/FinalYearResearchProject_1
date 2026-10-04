# D3-OMM: Operating Mode Monitoring

**Reference:** https://d3fend.mitre.org/technique/D3-OMM/  

## Definition
Detects operating modes such as Program, Run, Remote, or Stop.

## Parent Class(es)
- Platform Monitoring

## Relationships
- **kb-reference:** Reference - Value of PLC Key Switch Monitoring to Keep Critical Systems More Secure
- **kb-reference:** Reference - TRITON Malware Remains Threat to Global Critical Infrastructure Industrial Control Systems (ICS)
- **monitors:** OT Controller Operating Mode

## Knowledge Base Article
## How it works
Many OT Controllers have key switches to change the controller into various modes of operation. These modes of operation can include Program, Run, Remote, or Stop.

The key switch position is often available as a system diagnostic function block of the programming logic.

## Considerations
* It is advised to configure a key switch alarm such that an operator is alerted when the controller is put into a programming mode, as this could indicate unintentional or malicious changes to operational code.
