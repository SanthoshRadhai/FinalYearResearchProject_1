# D3-SWI: Software Inventory

**Synonym(s):** Software Discovery, Software Inventorying  
**Reference:** https://d3fend.mitre.org/technique/D3-SWI/  

## Definition
Software inventorying identifies and records the software items in the organization's architecture.

## Parent Class(es)
- Asset Inventory

## Relationships
- **inventories:** Software
- **kb-reference:** Reference - Web-Based Enterprise Management
- **kb-reference:** Reference - Windows Management Infrastructure (MI)
- **kb-reference:** Reference - Windows Management Instrumentation (WMI)

## Knowledge Base Article
## How it works
Administrators collect information on software items in their architecture using a variety of administrative and management tools that query network nodes for information.  In limited cases, where such queries are not supported or provide specific information of interest, an administrator may also collect this information through network enumeration methods to determine services responding on network nodes.

## Considerations
* Scanning and probing techniques using mapping tools can result in side effects to information technology (IT) and operational technology (OT) systems.
* An adversary conducting network enumeration may engage in activities that parallel normal software inventorying activities, but would require escalating to admin privileges for most of the operations requiting administrative tools.

## Examples

Application-layer discovery:

* Simple Network Management Protocol (SNMP) collects MIB information
* Web-based Enterprise Management (WBEM) collects CIM information
   * Windows Management Instrumentation (WMI)
   * Windows Management Infrastructure (MI)
