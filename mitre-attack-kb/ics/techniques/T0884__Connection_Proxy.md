# T0884: Connection Proxy


**ATT&CK ID:** T0884  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Command And Control  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0884  

## Description
Adversaries may use a connection proxy to direct network traffic between systems or act as an intermediary for network communications.

The definition of a proxy can also be expanded to encompass trust relationships between networks in peer-to-peer, mesh, or trusted connections between networks consisting of hosts or systems that regularly communicate with each other.

The network may be within a single organization or across multiple organizations with trust relationships. Adversaries could use these types of relationships to manage command and control communications, to reduce the number of simultaneous outbound network connections, to provide resiliency in the face of connection loss, or to ride over existing trusted communications paths between victims to avoid suspicion. (Citation: Enterprise ATT&CK January 2018)

## Mitigations
- M0807: Network Allowlists
- M0920: SSL/TLS Inspection
- M0931: Network Intrusion Prevention
- M0937: Filter Network Traffic

## Known Threat Groups Using This Technique
- G0034: Sandworm Team

## Known Software Using This Technique
- S1045: INCONTROLLER
- S0604: Industroyer
