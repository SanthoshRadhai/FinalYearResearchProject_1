# D3-NNI: Network Node Inventory

**Synonym(s):** System Discovery, System Inventorying  
**Reference:** https://d3fend.mitre.org/technique/D3-NNI/  

## Definition
Network node inventorying identifies and records all the network nodes (hosts, routers, switches, firewalls, etc.) in the organization's architecture.

## Parent Class(es)
- Asset Inventory

## Relationships
- **inventories:** Network Node
- **kb-reference:** Reference - IEEE Standard for Local and Metropolitan Area Networks - Station and Media Access Control Connectivity Discovery
- **kb-reference:** Reference - Qualys Network Passive Sensor Getting Started Guide
- **kb-reference:** Reference - An Architecture for Describing Simple Network Management Protocol (SNMP) Management Frameworks
- **kb-reference:** Reference - Web-Based Enterprise Management
- **kb-reference:** Reference - Windows Management Infrastructure (MI)
- **kb-reference:** Reference - Windows Management Instrumentation (WMI)

## Knowledge Base Article
## How it works
Administrators collect information on network nodes in their architecture using a variety of administrative and management tools that query network devices and nodes for information.  In some cases, where such queries are not supported or provide specific information of interest, an administrator may also collect this information through network enumeration methods to include host discovery and scanning for active ports and services.

## Considerations
* Scanning and probing techniques using mapping tools can result in side effects to information technology (IT) and operational technology (OT) systems.
* An adversary conducting network enumeration may engage in activities that parallel normal network node inventorying activities, but would require escalating to admin privileges for most of the operations requiting administrative tools

## Examples
* Link-layer discovery
   * Link-layer Discovery Protocol (LLDP)
   * Cisco Discovery Protocol (CDP)
* Application-layer discovery
   * Simple Network Management Protocol (SNMP) collects MIB information
   * Web-based Enterprise Management (WBEM) collects CIM information
      * Windows Management Instrumentation (WMI)
      * Windows Management Infrastructure (MI)
