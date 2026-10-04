# D3-UDTA: User Data Transfer Analysis

**Reference:** https://d3fend.mitre.org/technique/D3-UDTA/  

## Definition
Analyzing the amount of data transferred by a user.

## Parent Class(es)
- User Behavior Analysis

## Relationships
- **analyzes:** Resource Access
- **kb-reference:** Reference - System and method thereof for identifying and responding to security incidents based on preemptive forensics - Palo Alto Networks Inc
- **kb-reference:** Reference - System for implementing threat detection using threat and risk assessment of asset-actor interactions - VECTRA NETWORKS Inc

## Knowledge Base Article
## How it works
Unusual data transfer activity may indicate unauthorized activity. Data transfers can be analyzed by collecting network traffic or application logs.

## Considerations
* There is a potential for false positives from anomalies that are not associated with unauthorized activity.
* Attackers that move low and slow may not differentiate their data transfer behavior enough for an alert to trigger.
