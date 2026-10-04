# D3-IHN: Integrated Honeynet

**Reference:** https://d3fend.mitre.org/technique/D3-IHN/  

## Definition
The practice of setting decoys in a production environment to entice interaction from attackers.

## Parent Class(es)
- Decoy Environment

## Relationships
- **kb-reference:** Reference - Synchronizing a honey network configuration to reflect a target network environment - Palo Alto Networks Inc
- **spoofs:** Intranet Network

## Knowledge Base Article
## How it works
Integrated honeynets use full production environments connected to the enterprise network, that utilize computing resources or software that attract attackers, and allow full interaction and access that provides a complete view of an attack.

## Considerations
An attacker with control of a system on an Integrated Honeynet could:
* try to attack other connected hosts on the network, its IP range of internal hosts not properly configured to react to connections from machines on the integrated honeynet, or position behind the firewall.
* exploit its position by eavesdropping on network traffic
If an attacker manages to stop the processes used to log an attack without setting off any alarms. [1]

1. Honeypots for Windows, Roger Grimes, 2005
