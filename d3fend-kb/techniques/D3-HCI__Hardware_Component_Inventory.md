# D3-HCI: Hardware Component Inventory

**Synonym(s):** Hardware Component Discovery, Hardware Component Inventorying  
**Reference:** https://d3fend.mitre.org/technique/D3-HCI/  

## Definition
Hardware component inventorying identifies and records the hardware items in the organization's architecture.

## Parent Class(es)
- Asset Inventory

## Relationships
- **inventories:** Hardware Device
- **kb-reference:** Reference - Advanced device matching system

## Knowledge Base Article
## How it works
Administrators collect information on hardware devices such as peripherals, NICs, processors, and memory devices that are components of the computers in their architecture using a variety of administrative and management tools that query for this information.  In some cases, where such queries are not supported or provide specific information of interest, an administrator may also collect this information through remote administration tools and system commands, either manually or using scripts.

## Considerations
* Scanning and probing techniques using mapping tools can result in side effects to information technology (IT) and operational technology (OT) systems.
* An adversary conducting network enumeration may engage in activities that parallel normal hardware inventorying activities, but would require escalating to admin privileges for most of the operations requiting administrative tools

## Examples
* Bus discovery
   * Admin-scripted PCI Bus inventory using ssh and pciutils
* Application-layer discovery
   * Simple Network Management Protocol (SNMP) collects MIB information
   * Web-based Enterprise Management (WBEM) collects CIM information
      * Windows Management Instrumentation (WMI)
      * Windows Management Infrastructure (MI)
