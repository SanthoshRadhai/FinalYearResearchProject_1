# D3-ITF: Inbound Traffic Filtering

**Reference:** https://d3fend.mitre.org/technique/D3-ITF/  

## Definition
Restricting network traffic originating from untrusted networks destined towards a private host or enclave.

## Parent Class(es)
- Network Traffic Filtering

## Relationships
- **filters:** Inbound Network Traffic
- **kb-reference:** Reference - Active firewall system and methodology - McAfee LLC
- **kb-reference:** Reference - Automatically generating rules for connection security - Microsoft
- **kb-reference:** Reference - FWTK - Firewall Toolkit
- **kb-reference:** Reference - Firewall for interent access - Secure Computing LLC
- **kb-reference:** Reference - Firewall for processing a connectionless network packet - National Security Agency
- **kb-reference:** Reference - Firewall for processing connection-oriented and connectionless datagrams over a connection-oriented network - National Security Agency
- **kb-reference:** Reference - Firewalls that filter based upon protocol commands - Intel Corp
- **kb-reference:** Reference - Method for controlling computer network security - Checkpoint Software Technologies Ltd
- **kb-reference:** Reference - Network firewall with proxy - Secure Computing LLC

## Knowledge Base Article
## How it works
Inbound Traffic, in this context, is network traffic originating from an untrusted network towards a private host or enclave.
For example:

* An untrusted network host connecting to a internal commercial portal, shopping.example.com
* An external mail server connecting to an internal mail server, mail.example.com

Filtering policies are developed by administrators to meet business requirements and limit connectivity. These policies are implemented on edge devices such as firewalls, routers, and intrusion prevention systems. Examples of filters:

* Blocking incoming traffic from spoofed internally facing IP addresses
* Blocking specific ports and services from establishing connections
* Limiting specific IP ranges from connecting to the network
* Dynamic inbound filtering (Hole punching, STUN, NAT-T)

## Considerations
* Business requirements typically drive the development of filtering rulesets
* Protocols using non-standard ports may circumvent filtering technology, which does not detect application protocol based on traffic content

## Implementations
* OpenWRT (Embedded)
* Netfilter (Linux)
* Windows Firewall
* pf(BSD)
