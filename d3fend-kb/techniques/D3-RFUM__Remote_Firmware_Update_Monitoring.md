# D3-RFUM: Remote Firmware Update Monitoring

**Reference:** https://d3fend.mitre.org/technique/D3-RFUM/  

## Definition
Monitoring of remote firmware update commands to identify unauthorized software installations.

## Parent Class(es)
- Application Protocol Command Analysis

## Relationships
- **detects:** OT Device Firmware Command
- **kb-reference:** Reference - Method for detecting anomalies in time series data produced by devices of an infrastructure in a network
- **monitors:** OT Network Traffic

## Knowledge Base Article
## How it works
By deploying sensors within the OT environment to passively monitor network traffic, tools can leverage deep packet inspection to identify protocol-specific commands and generate logs of relevant firmware activity. Additionally, these tools may incorporate behavioral and signature-based analysis to enhance detection and alerting capabilities.
