# D3-FBA: Firmware Behavior Analysis

**Synonym(s):** Firmware Timing Analysis  
**Reference:** https://d3fend.mitre.org/technique/D3-FBA/  

## Definition
Analyzing the behavior of embedded code in firmware and looking for anomalous behavior and suspicious activity.

## Parent Class(es)
- Platform Monitoring

## Relationships
- **analyzes:** Firmware
- **kb-reference:** Reference - Firmware Behavior Analysis ConFirm
- **kb-reference:** Reference - Firmware Behavior Analysis VIPER

## Knowledge Base Article
## How it works
Firmware behavior analysis provides protections by ensuring that installed firmware has not been tampered with or modified. Firmware analysis applies to mutable firmware and immutable read-only memory (ROMs).

Firmware in deployed network devices is typically not analyzed and monitored for vulnerabilities and thus is subject to potential attacks. This technique makes use of known and measured behavioral attributes, including timing attributes, of analyzed firmware on deployed devices.

A behavioral method that employs known timing measurements may use the timing results from a challenge and response protocol to detect the presence of malware in embedded firmware. Firmware device timing measurements are made, specific to the installed device, and are used in the verifying function.

The original firmware image is modified by injecting a monitoring software component into the embedded firmware code. The injected software components will allow for a software root of trust, the challenge and response protocol, to be implement in the firmware.

A challenge-response is issued and includes a nonce so that replays are not allowed. The firmware will calculate a checksum over all of memory, including the nonce, and return the result. The verification system will compare the computed checksum and the time it took for the computation of the checksum to determine if the firmware has been modified.

## Considerations
* The firmware code will need to be modified to include the behavioral monitoring functionality.
* This technique is sensitive to the device the embedded firmware is hosted on and it is expected that the devices and firmware will need to be profiled and analyzed to determine timing estimation.
* This technique is not expected to be one hundred percent correct as you would expect in a hardware root of trust solution and may require some tuning.
