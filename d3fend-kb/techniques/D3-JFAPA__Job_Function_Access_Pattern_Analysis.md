# D3-JFAPA: Job Function Access Pattern Analysis

**Reference:** https://d3fend.mitre.org/technique/D3-JFAPA/  

## Definition
Detecting anomalies in user access patterns by comparing user access activity to behavioral profiles that categorize users by role such as job title, function, department.

## Parent Class(es)
- User Behavior Analysis

## Relationships
- **analyzes:** Authorization
- **kb-reference:** Reference - Anomaly Detection Using Adaptive Behavioral Profiles - Securonix Inc

## Knowledge Base Article
## How it works
Peer group analysis identifies functionally similar groups of actors (users or resources) based on categorizations such as job title, organizational hierarchy, or other attribute that indicates similarity of job function. Current user access activity is then compared to the appropriate peer group behavior profile to identify anomalies.

## Considerations
Potential for false positives from anomalies that are not associated with malicious activity.
