# D3-RTSD: Remote Terminal Session Detection

**Reference:** https://d3fend.mitre.org/technique/D3-RTSD/  

## Definition
Detection of an unauthorized remote live terminal console session by examining network traffic to a network host.

## Parent Class(es)
- Network Traffic Analysis

## Relationships
- **analyzes:** Network Traffic
- **kb-reference:** Reference - Method and system for detecting external control of compromised hosts - VECTRA NETWORKS Inc
- **kb-reference:** Reference - CAR-2013-07-002: RDP Connection Detection - MITRE
- **kb-reference:** Reference - CAR-2016-04-005: Remote Desktop Logon - MITRE

## Knowledge Base Article
## How it works
An external attacker takes remote control of a host inside a company or organization's network and manually directs offensive techniques. Nonstandard terminal sessions and abnormal behaviors are analyzed in this technique. Abnormal behavior detection includes analysis of user input patterns in the real-time session, keyboard output and packet inspection.

### Network Traffic Inspection
Network traffic from internal hosts is the main concern and focus for the traffic inspection. The network traffic is collected into inspection groups. The groups of traffic are assembled into distinct pair flows (outbound/inbound) and the pair flows are further divided into sessions. Only sessions originated inside of the network are considered for the inspection. Traffic inspection includes analysis to determine if a human is involved in the session exchanges. Time-based statistics are captured for each session being analyzed by the detection engine.

### Algorithm Analysis Description
Analysis algorithms look for patterns in the network traffic captured from the session data.  A detection engine groups the session traffic data, between the hosts, into rapid exchange instances. Analysis of rapid exchange traffic patterns can lead to the discovery of abnormal behavior which is indicative of a compromised internal host. The analysis algorithms look for patterns in the traffic which correlate to known activity (e.g., relay attacks, bot activity, bitcoin mining). Some metrics used during inspection include the following.

* Number of rapid-exchange instances
* Time interval between packets
* Fixed cadence of traffic
* Rhythm and direction of the initiation of instances
* Volume of data flowing from internal to external controlling host
* Data transfer characteristics
* Variability in length of silent periods

## Considerations
* Full packet capture is required which can be process intensive to analyze
* Attackers that move low and slow may blend in with existing traffic resulting in false negatives
