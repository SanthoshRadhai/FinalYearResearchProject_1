# S1072: Industroyer2

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1072  
**Aliases:** Industroyer2  
**Platforms:** Field Controller/RTU/PLC/IED, Engineering Workstation  

## Description
[Industroyer2](https://attack.mitre.org/software/S1072) is a compiled and static piece of malware that has the ability to communicate over the IEC-104 protocol. It is similar to the IEC-104 module found in [Industroyer](https://attack.mitre.org/software/S0604). Security researchers assess that [Industroyer2](https://attack.mitre.org/software/S1072) was designed to cause impact to high-voltage electrical substations. The initial [Industroyer2](https://attack.mitre.org/software/S1072) sample was compiled on 03/23/2022 and scheduled to execute on 04/08/2022, however it was discovered before deploying, resulting in no impact.(Citation: Industroyer2 Blackhat ESET)

## Techniques Used
- T0801: Monitor Process State
- T0802: Automated Collection
- T0806: Brute Force I/O
- T0836: Modify Parameter
- T0881: Service Stop
- T0888: Remote System Information Discovery
- T1692.001: Command Message
