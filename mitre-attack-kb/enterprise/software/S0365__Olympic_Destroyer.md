# S0365: Olympic Destroyer

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0365  
**Aliases:** Olympic Destroyer  
**Platforms:** Windows  

## Description
[Olympic Destroyer](https://attack.mitre.org/software/S0365) is malware that was used by [Sandworm Team](https://attack.mitre.org/groups/G0034) against the 2018 Winter Olympics, held in Pyeongchang, South Korea. The main purpose of the malware was to render infected computer systems inoperable. The malware leverages various native Windows utilities and API calls to carry out its destructive tasks. [Olympic Destroyer](https://attack.mitre.org/software/S0365) has worm-like features to spread itself across a computer network in order to maximize its destructive impact.(Citation: Talos Olympic Destroyer 2018)(Citation: US District Court Indictment GRU Unit 74455 October 2020)

## Techniques Used
- T1003.001: LSASS Memory
- T1016: System Network Configuration Discovery
- T1018: Remote System Discovery
- T1021.002: SMB/Windows Admin Shares
- T1047: Windows Management Instrumentation
- T1135: Network Share Discovery
- T1485: Data Destruction
- T1489: Service Stop
- T1490: Inhibit System Recovery
- T1529: System Shutdown/Reboot
- T1555.003: Credentials from Web Browsers
- T1569.002: Service Execution
- T1570: Lateral Tool Transfer
- T1685.005: Clear Windows Event Logs
