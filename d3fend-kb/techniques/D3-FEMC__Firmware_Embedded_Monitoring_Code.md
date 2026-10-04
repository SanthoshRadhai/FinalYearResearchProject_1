# D3-FEMC: Firmware Embedded Monitoring Code

**Reference:** https://d3fend.mitre.org/technique/D3-FEMC/  

## Definition
Monitoring code is injected into firmware for integrity monitoring of firmware and firmware data.

## Parent Class(es)
- Platform Monitoring

## Relationships
- **analyzes:** Firmware
- **kb-reference:** Reference - Firmware Embedded Monitoring Code Red Balloon
- **kb-reference:** Reference - Firmware Embedded Monitoring Code Symbiotes

## Knowledge Base Article
## How it works
Firmware in deployed network devices is typically not monitored for malicious changes. This technique provides a method to embed a software security component into the deployed firmware which provides a near real-time monitoring hook. The exception handling code, in the firmware, is typically used to expose any detected vulnerabilities.

The injected software components provide a feature similar to intrusion detection systems for the firmware by detecting unauthorized modifications of the embedded firmware. The integrity of static code and firmware data are monitored continuously in the hosted devices. Comparisons are made to monitored elements like firmware memory addresses and data segments. Memory pages are scanned and if a modification is detected the software component may lock the page. This will protect subsequent attempted modifications to the firmware. The software component may utilize the exception handling code and thus be able to disclose the exact address of the modified memory.

The injected software components are inserted during the firmware imaging process. The injected software is assumed to have knowledge of both the embedded code and the current execution state of the host program. The injected software will monitor and alert, in near real-time, on potential suspicious activity. The injected code is run alongside of the embedded code in the host. The injected software operates as an independent entity and is not dependent on the host software.

Finally, this technique may implement other countermeasure techniques as part of their analytical processes. These should be identified by referencing other countermeasure techniques directly as necessary.

## Considerations
* The firmware code will need to be modified and re-hosted on the device.
* Exposing monitoring hooks to the injected code may introduce additional risk.
