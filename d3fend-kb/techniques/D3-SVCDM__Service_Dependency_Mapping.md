# D3-SVCDM: Service Dependency Mapping

**Synonym(s):** Distributed Tracing  
**Reference:** https://d3fend.mitre.org/technique/D3-SVCDM/  

## Definition
Service dependency mapping determines the services on which each given service relies.

## Parent Class(es)
- System Mapping

## Relationships
- **kb-reference:** Reference - Catia UAF Plugin
- **kb-reference:** Reference - Tivoli Application Dependency Discovery Manager 7.3.0 - Dependencies between resources
- **kb-reference:** Reference - Unified Architecture Framework (UAF)
- **maps:** Service Dependency

## Knowledge Base Article
## How it works
The organization collects and models architectural information about the services and consumers of services and maps the dependencies between the services.

## Considerations
* Architectural design artifacts and SMEs may need to be consulted to determine if dependencies are intended or otherwise essential.
* Service dependencies for critical systems--those supporting critical organizational activities--should be prioritized for supply chain risk analysis.
* Service dependencies in cloud or microservice architectures may be discovered using distributed tracing capabilities
