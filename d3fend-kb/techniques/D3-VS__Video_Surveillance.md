# D3-VS: Video Surveillance

**Synonym(s):** CCTV Surveillance, Video Monitoring  
**Reference:** https://d3fend.mitre.org/technique/D3-VS/  

## Definition
Monitoring of physical areas via camera video feeds to deter, detect, and investigate unauthorized access and related security events.

## Parent Class(es)
- Physical Access Monitoring

## Relationships
- **kb-reference:** Reference - DHS CCTV Technology Handbook
- **kb-reference:** Reference - NIST Special Publication 800-53 Revision 5 - Security and Privacy Controls for Information Systems and Organizations
- **kb-reference:** Reference - ONVIF Profile S
- **monitors:** Digital Camera

## Knowledge Base Article
## How it works

Video surveillance uses digital cameras that stream to a video management system (VMS) or network video recorder (NVR) for live monitoring, recording, and retrieval. Recording can be continuous or event-driven using analytics (motion in regions of interest, line crossing) or external triggers (access denials, sensor alarms). Time synchronization aligns video with other logs, while health monitoring detects camera outages and tamper. Secure export workflows preserve integrity for investigations.

## Considerations

* Plan camera placement and coverage to avoid occlusions and handle challenging lighting; select lenses and mounting to capture entry points and critical areas.
* Size storage and bandwidth for the intended retention period by choosing appropriate resolution, frame rate, and compression, and monitor capacity over time.
* Secure cameras and management systems with unique credentials, timely firmware updates, encrypted transport, and network segmentation to limit exposure.
* Address privacy and legal obligations with visible notice, role-based access to footage, and retention policies aligned with regulations and organizational policy.
* Monitor system health and build resilience with tamper and heartbeat alerts, recorder failover where needed, and accurate time synchronization for correlation.
