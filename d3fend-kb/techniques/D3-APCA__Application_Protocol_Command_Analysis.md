# D3-APCA: Application Protocol Command Analysis

**Reference:** https://d3fend.mitre.org/technique/D3-APCA/  

## Definition
Analyzing application protocol level remote commands to detect unauthorized activity.

## Parent Class(es)
- Network Traffic Analysis

## Relationships
- **kb-reference:** Reference - Method and apparatus for detecting anomalies of an infrastructure in a network
- **kb-reference:** Reference - Protocol based detection of suspicious network traffic
- **monitors:** Network Traffic

## Knowledge Base Article
## How it works
This technique requires the ability to parse application layer protocols to understand the commands being sent to a remote service. Signature-based or statistical analysis may be employed to identify unauthorized commands being sent. These commands can be observed by monitoring network traffic or application logs.
