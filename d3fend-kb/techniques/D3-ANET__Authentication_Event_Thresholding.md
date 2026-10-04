# D3-ANET: Authentication Event Thresholding

**Reference:** https://d3fend.mitre.org/technique/D3-ANET/  

## Definition
Collecting authentication events, creating a baseline user profile, and determining whether authentication events are consistent with the baseline profile.

## Parent Class(es)
- User Behavior Analysis

## Relationships
- **analyzes:** Authentication
- **created:** 2020-08-05T00:00:00
- **kb-reference:** Reference - Method and Apparatus for Network Fraud Detection and Remediation Through Analytics - Idaptive LLC
- **kb-reference:** Reference - CAR-2013-02-008: Simultaneous Logins on a Host - MITRE
- **kb-reference:** Reference - System, method, and computer program product for detecting and assessing security risks in a network - Exabeam Inc
- **kb-reference:** Reference - CAR-2013-02-012: User Logged in to Multiple Hosts - MITRE
- **kb-reference:** Reference - CAR-2013-10-001: User Login Activity Monitoring - MITRE

## Knowledge Base Article
## How it works
Authentication event data is collected (logon information such as device id, time of day, day of week, geo-location, etc.) to create an activity baseline. Then, a threshold is determined either through a manually specified configuration, or a statistical analysis of deviations in historical data. New authentication events are evaluated to determine if a threshold is exceeded. Thresholds can be static or dynamic.

### Actions
As a result of the analysis, actions taken could include:

* [Account Locking](/technique/d3f:AccountLocking)
* Raising an alert

### Example data sources
 * Directory server logs
 * VPN Server logs
 * IDAM Capability logs
 * NAC logs
 * Authentication client logs
 * Kerberos network traffic
 * LDAP network traffic

## Considerations

This technique covers statistical outliers. Though depending on the complexity or dimensionality of the data considered, outliers may not be obvious to a human analyst reviewing events in simplistic analytic views. If the malicious activity is not statistically different from benign activity, an alert threshold will not be met.
