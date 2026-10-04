# D3-OTF: Outbound Traffic Filtering

**Reference:** https://d3fend.mitre.org/technique/D3-OTF/  

## Definition
Restricting network traffic originating from a private host or enclave destined towards untrusted networks.

## Parent Class(es)
- Network Traffic Filtering

## Relationships
- **filters:** Outbound Network Traffic
- **kb-reference:** Reference - Automatically generating rules for connection security - Microsoft

## Knowledge Base Article
## How it works

Outbound traffic, in this context, is network traffic originating from a private host or enclave destined towards untrusted networks.
For example:

* An enterprise desktop intranet user connecting to www.example.com
* An internal mail server connecting to an external mail server, mail.example.com

Filtering is commonly implemented as firewall rulesets to limit outbound traffic permitted to egress a host or network. Firewalls are deployed either directly on hosts through kernel level software implementations or installed in-line directly on network links. There are benefits and disadvantages to each approach.

There are various strategies for developing filtering rulesets:

* Block everything by default
* Limit destination hosts
* Limit destination transport or application protocols
* Restrict content outbound (Ex. strings formatted as social security numbers, or proprietary data)

## Considerations
* Dynamic IP assignment creates challenges for Outbound Traffic Filtering because users are not necessarily associated with the same IP address. This can be addressed by linking IP address management information with the filtering logic.
* Connections using non-standard transport layer ports may circumvent outbound traffic filtering technology which does not detect application protocol based on traffic content.
* Business requirements typically drive the development of filtering rule sets.

## Implementations
- iptables (Linux)
- Windows Firewall
- pf (BSD)
