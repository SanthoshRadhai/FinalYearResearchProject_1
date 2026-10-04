# D3-PSM: Proximity Sensor Monitoring

**Synonym(s):** Proximity Reader Monitoring, RFID Reader Monitoring  
**Reference:** https://d3fend.mitre.org/technique/D3-PSM/  

## Definition
Monitoring events from proximity sensors that indicate a credential or tagged asset is within the sensor’s read range or a defined zone. Common enabling technologies include RFID, Bluetooth Low Energy (BLE), and Ultra-Wideband (UWB).

## Parent Class(es)
- Physical Access Monitoring

## Relationships
- **kb-reference:** Reference - FIPS 201-3
- **kb-reference:** Reference - NIST SP 800-116 Rev. 1
- **kb-reference:** Reference - Wikipedia: Proximity card
- **kb-reference:** Reference - Wikipedia: RFID
- **monitors:** Proximity Sensor

## Knowledge Base Article
## How it works

Proximity readers and sensors detect credentials or tagged assets within their read field, then report presence and, when applicable, authenticate to a controller for access decisions. Systems may use RSSI, dwell time, or time-of-flight to enforce zones and policies such as anti-passback. Secure, authenticated communication between readers and controllers helps prevent cloning and replay attacks.

## Considerations

 * Place readers and align antennas to achieve consistent read ranges; account for materials like metal and liquids that can detune signals.
* Use cryptographic credentials with mutual authentication and encrypted, supervised reader links to mitigate cloning and relay attacks.
* Protect privacy by minimizing collected data, limiting retention, and restricting access to proximity logs.
* Calibrate detection thresholds and zone boundaries; re-test after layout changes or equipment moves.
* Monitor reader and tag health, including battery status for BLE and UWB tags and supervision signals for wired and wireless devices.
