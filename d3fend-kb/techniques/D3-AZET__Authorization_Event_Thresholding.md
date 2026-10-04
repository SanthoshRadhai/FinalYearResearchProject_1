# D3-AZET: Authorization Event Thresholding

**Reference:** https://d3fend.mitre.org/technique/D3-AZET/  

## Definition
Collecting authorization events, creating a baseline user profile, and determining whether authorization events are consistent with the baseline profile.

## Parent Class(es)
- User Behavior Analysis

## Relationships
- **analyzes:** Authorization
- **created:** 2020-08-05T00:00:00
- **kb-reference:** Reference - Method and Apparatus for Network Fraud Detection and Remediation Through Analytics - Idaptive LLC
- **kb-reference:** Reference - CAR-2013-09-003: SMB Session Setups - MITRE
- **kb-reference:** Reference - System, method, and computer program product for detecting and assessing security risks in a network - Exabeam Inc
- **kb-reference:** Reference - CAR-2013-02-012: User Logged in to Multiple Hosts - MITRE

## Knowledge Base Article
## How it works

Authorization event data is collected to create a baseline user profile. Authorization events that deviate from the baseline and exceed a static or dynamic threshold are identified for further action. Authorization events can include successful and failed authorization attempts as well as events related to permissions including viewing, editing, deleting, creating files, databases etc.

## Considerations

Depending on the complexity of the data considered, outliers may not be obvious to a human analyst reviewing events in simplistic analytic views. If malicious activity is not statistically different from benign activity, an alert threshold will not be met.
