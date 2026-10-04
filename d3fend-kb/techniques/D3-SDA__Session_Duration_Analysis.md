# D3-SDA: Session Duration Analysis

**Reference:** https://d3fend.mitre.org/technique/D3-SDA/  

## Definition
Analyzing the duration of user sessions in order to detect unauthorized  activity.

## Parent Class(es)
- User Behavior Analysis

## Relationships
- **analyzes:** Authentication
- **analyzes:** Authorization
- **kb-reference:** Reference - Method and Apparatus for Network Fraud Detection and Remediation Through Analytics - Idaptive LLC
- **kb-reference:** Reference - System, method, and computer program product for detecting and assessing security risks in a network - Exabeam Inc

## Knowledge Base Article
## How it works
Detecting unauthorized user sessions by comparing the duration of a user logon session with a baseline behavior model. The behavior model comprises historical user session duration times.  Abnormalities between session duration and the behavior model may indicate suspicious activity.

## Considerations
* Potential for false positives from anomalies that are not associated with malicious activity.
* Attackers may not differentiate their session duration enough to trigger an alert.
