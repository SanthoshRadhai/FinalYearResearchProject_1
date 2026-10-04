# D3-WSAA: Web Session Activity Analysis

**Reference:** https://d3fend.mitre.org/technique/D3-WSAA/  

## Definition
Monitoring changes in user web session behavior by comparing current web session activity to a baseline behavior profile or a catalog of predetermined malicious behavior.

## Parent Class(es)
- User Behavior Analysis

## Relationships
- **analyzes:** Web Resource Access
- **kb-reference:** Reference - Host intrusion prevention system using software and user behavior analysis - Sophos Ltd
- **kb-reference:** Reference - System and Method for Detection of a Change in Behavior in the Use of a Website Through Vector Velocity Analysis - Silver Tail Systems
- **kb-reference:** Reference - System and Method for Network Security Including Detection of Attacks Through Partner Websites - EMC IP Holding Co LLC
- **kb-reference:** Reference - System and method thereof for identifying and responding to security incidents based on preemptive forensics - Palo Alto Networks Inc

## Knowledge Base Article
## How it works
User web session data is collected over a period of time to create a user behavior profile. Data collected includes clicks made on a website, average time between clicks, filling out web forms, order in which pages are viewed, and downloading files. Current user web session behavior is then compared against the use behavior profile to identify anomalies and a likelihood that the current user web session is malicious. Current user web session behavior can also be compared to predetermined known malicious behavior profiles that are developed through analysis of malware in run time at a threat research facility.

## Considerations
* Potential for false positives from anomalies that are not associated with malicious activity.
* Attackers may not differentiate their web session activity enough to trigger an alert.
