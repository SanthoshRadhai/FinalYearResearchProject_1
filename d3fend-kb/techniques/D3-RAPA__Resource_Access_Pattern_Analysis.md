# D3-RAPA: Resource Access Pattern Analysis

**Reference:** https://d3fend.mitre.org/technique/D3-RAPA/  

## Definition
Analyzing the resources accessed by a user to identify unauthorized activity.

## Parent Class(es)
- User Behavior Analysis

## Relationships
- **analyzes:** Authentication
- **analyzes:** Authorization
- **kb-reference:** Reference - Host intrusion prevention system using software and user behavior analysis - Sophos Ltd
- **kb-reference:** Reference - Method and Apparatus for Network Fraud Detection and Remediation Through Analytics - Idaptive LLC
- **kb-reference:** Reference - Modeling user access to computer resources - Daedalus Group LLC (formerly IBM)
- **kb-reference:** Reference - System, method, and computer program product for detecting and assessing security risks in a network - Exabeam Inc
- **kb-reference:** Reference - System and method thereof for identifying and responding to security incidents based on preemptive forensics - Palo Alto Networks Inc

## Knowledge Base Article
## How it works
This technique analyzes a user's resource accesses by comparing the user's recent activity against a baseline activity model. Major differences between the current activity and the baseline model might indicate unauthorized activity if they are severe enough.


## Considerations
* Potential for false positives from anomalies that are not associated with malicious activity.
* Attackers that move low and slow may not differentiate their resource access activity behavior enough to trigger an alert.
