# D3-SYSDM: System Dependency Mapping

**Reference:** https://d3fend.mitre.org/technique/D3-SYSDM/  

## Definition
System dependency mapping identifies and models the dependencies of system components on each other to carry out their function.

## Parent Class(es)
- System Mapping

## Relationships
- **kb-reference:** Reference - Catia UAF Plugin
- **kb-reference:** Reference - Software vulnerability graph database
- **kb-reference:** Reference - Tivoli Application Dependency Discovery Manager 7.3.0 - Dependencies between resources
- **kb-reference:** Reference - Unified Architecture Framework (UAF)
- **maps:** System Dependency

## Knowledge Base Article
## How it works
The organization collects and models architectural information about the software, hardware, and products and maps the dependencies between systems, including each system's internal components and dependencies.

## Considerations
* Data exchanges identified in the network mapping efforts usually indicate such dependencies, but may not be part of the intended design.
* Architectural design artifacts and SMEs may need to be consulted to determine if dependencies are intended or otherwise essential.
* System dependency mapping can identify internal dependencies of standard and pre-built systems that should be incorporated into a complete system dependency model.
* System dependencies for critical systems--those supporting critical organizational activities--should be prioritized for supply chain risk analysis.
* System dependencies should identify the integral components of a given named system and their structure to form a system.
* System dependencies with a given system may be fixed by a particular product's configuration, and leveraging external knowledge bases about dependencies available (e.g., from package managers) is essential.
