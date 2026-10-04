# D3-ALLM: Active Logical Link Mapping

**Reference:** https://d3fend.mitre.org/technique/D3-ALLM/  

## Definition
Active logical link mapping sends and receives network traffic as a means to map the whole data link layer, where the links represent logical data flows rather than physical connection

## Parent Class(es)
- Logical Link Mapping

## Relationships
- **kb-reference:** Reference - Identification of traceroute nodes and associated devices
- **kb-reference:** Reference - SNMP - Network Auto-Discovery
- **may-query:** Network Agent

## Knowledge Base Article
## How it works

Active logical link mapping establishes awareness of logical links in the network by sending data over the network to gather information about logical connections in the network.

Typically this will be achieved through network telemetry coordinated for network management and monitoring and will use a link layer discovery protocol such as LLDP and the information gathered and aggregated at higher levels using an application protocol such as SNMP.  The information may be polled by network management software or configured once and then pushed from network sensors (or agents.)

Another means of establishing network connectivity is by means of sending traffic through the use of a tool such as traceroute, to determine the logical paths through the network architecture.

## Considerations

* Best practice is to encrypt network monitoring data and require authentication for queries or admin/management functions.
* Push notifications reduce bandwidth necessary to capture and maintain information if reliable transport is used.
* Special consideration should be made before using of active scanning in OT networks and OT-safe options chosen where available.
