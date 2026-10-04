# D3-MSM: Motion Sensor Monitoring

**Synonym(s):** Motion Alarm Monitoring, Motion Detector Monitoring  
**Reference:** https://d3fend.mitre.org/technique/D3-MSM/  

## Definition
Monitoring events from motion detectors (e.g., passive IR, microwave, dual-technology) to detect presence or movement within protected areas.

## Parent Class(es)
- Physical Access Monitoring

## Relationships
- **kb-reference:** Reference - NIST Special Publication 800-53 Revision 5 - Security and Privacy Controls for Information Systems and Organizations
- **kb-reference:** Reference - Wikipedia: Motion detector
- **kb-reference:** Reference - Wikipedia: Passive infrared sensor
- **monitors:** Motion Detector

## Knowledge Base Article
## How it works

Motion sensors generate events when movement is detected within their coverage pattern. Alarm panels or PACS correlate motion with arming schedules, door openings, and other sensors; video systems can use motion to trigger recording or bookmarks. Cross-zoning and sensitivity/pulse-count settings are commonly adjusted to balance detection and false-alarm rates.

## Considerations

* Place sensors at appropriate height and angle with clear line of sight, avoiding obstructions or reflective surfaces that can cause missed or false detections.
* Reduce false alarms by tuning sensitivity and pulse-count, using cross-zoning when needed, and accounting for HVAC airflow or rapid thermal changes.
* Monitor tamper and supervision signals; for wireless devices, verify periodic check-ins and battery levels; perform regular walk tests to validate coverage.
* Integrate motion events with cameras and with door position switches and other sensors in the protected area to provide context and faster verification; use motion to trigger recording or bookmarks.
