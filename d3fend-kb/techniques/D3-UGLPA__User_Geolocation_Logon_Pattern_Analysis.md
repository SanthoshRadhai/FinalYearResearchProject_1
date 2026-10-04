# D3-UGLPA: User Geolocation Logon Pattern Analysis

**Reference:** https://d3fend.mitre.org/technique/D3-UGLPA/  

## Definition
Monitoring geolocation data of user logon attempts and comparing it to a baseline user behavior profile to identify anomalies in logon location.

## Parent Class(es)
- User Behavior Analysis

## Relationships
- **analyzes:** Network Traffic
- **kb-reference:** Reference - Method and Apparatus for Network Fraud Detection and Remediation Through Analytics - Idaptive LLC
- **kb-reference:** Reference - System, method, and computer program product for detecting and assessing security risks in a network - Exabeam Inc

## Knowledge Base Article
## How it works
Geolocation data for each user logon attempt is collected and used to create a baseline user behavior profile. Current geolocation logon data is then compared against the user behavior profile. Logon activity that deviates from normal patterns and can help in identifying situations that may be indicative of a remote attacker using stolen credentials. For example:

* logons from locations that are different from where a user usually logs in
* logons from a location in which an enterprise has no users located
* logon that is not physically possible given the elapsed time since a logon from another location.

## Considerations
* Potential for false positives from logon anomalies that are not associated with malicious activity.
* Attackers may not differentiate their logon behavior enough to trigger an alert.
