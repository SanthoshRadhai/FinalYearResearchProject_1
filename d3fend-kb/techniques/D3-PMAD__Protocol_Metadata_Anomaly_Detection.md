# D3-PMAD: Protocol Metadata Anomaly Detection

**Reference:** https://d3fend.mitre.org/technique/D3-PMAD/  

## Definition
Collecting network communication protocol metadata and identifying statistical outliers.

## Parent Class(es)
- Network Traffic Analysis

## Relationships
- **analyzes:** Network Traffic
- **kb-reference:** Reference - Method and system for detecting threats using metadata vectors - VECTRA NETWORKS Inc
- **kb-reference:** Reference - Method and system for detecting threats using passive cluster mapping - Vectra Networks Inc
- **kb-reference:** Reference - System for implementing threat detection using daily network traffic community outliers - VECTRA NETWORKS Inc

## Knowledge Base Article
## How it works
Network protocol metadata is first collected and processed in real-time or post-facto. Metadata may include packet header information or information about a session (ex. time between requests/responses). Metadata is then grouped based on shared characteristics and those groups are compared to each other. If particular metadata differs significantly from other data, an alert is generated, identifying the network event as anomalous. Anomalous activity may indicate unauthorized activity.

## Considerations
Metadata collection on enterprises can yield large data sets. Storage, indexing, querying, and aging should be considered prior to implementation.
