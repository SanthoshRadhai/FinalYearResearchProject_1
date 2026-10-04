# D3-CSPP: Client-server Payload Profiling

**Reference:** https://d3fend.mitre.org/technique/D3-CSPP/  

## Definition
Comparing client-server request and response payloads to a baseline profile to identify outliers.

## Parent Class(es)
- Network Traffic Analysis

## Relationships
- **analyzes:** Network Traffic
- **kb-reference:** Reference - Method and system for detecting malicious payloads - Vectra Networks Inc

## Knowledge Base Article
## How it works
Profiling request and response payloads across multiple clients to a single server to develop a baseline of their characteristics. May take into account request/response sizes, entropy, frequency, and rhythm. Finally, identify outliers as they may indicate a malicious payload delivery and subsequent server exploitation.


## Considerations
* Collecting metrics to establish a profile can be challenging since user behavior can change easily.
* Employees may work different hours or inconsistent schedules which will cause false positives.
* Collection of network activity to generate metrics is a computationally intensive process.
* Users may log into different workstations which may cause false positives.
