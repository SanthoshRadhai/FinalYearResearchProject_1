# S0604: Industroyer

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0604  
**Aliases:** Industroyer, CRASHOVERRIDE, Win32/Industroyer  
**Platforms:** Windows  

## Description
[Industroyer](https://attack.mitre.org/software/S0604) is a sophisticated malware framework designed to cause an impact to the working processes of Industrial Control Systems (ICS), specifically components used in electrical substations.(Citation: ESET Industroyer) [Industroyer](https://attack.mitre.org/software/S0604) was used in the attacks on the Ukrainian power grid in December 2016.(Citation: Dragos Crashoverride 2017) This is the first publicly known malware specifically designed to target and impact operations in the electric grid.(Citation: Dragos Crashoverride 2018)

## Techniques Used
- T0800: Activate Firmware Update Mode
- T0801: Monitor Process State
- T0802: Automated Collection
- T0806: Brute Force I/O
- T0807: Command-Line Interface
- T0809: Data Destruction
- T0813: Denial of Control
- T0814: Denial of Service
- T0815: Denial of View
- T0816: Device Restart/Shutdown
- T0827: Loss of Control
- T0829: Loss of View
- T0831: Manipulation of Control
- T0832: Manipulation of View
- T0837: Loss of Protection
- T0840: Network Connection Enumeration
- T0846: Remote System Discovery
- T0846.001: Port Scan
- T0881: Service Stop
- T0884: Connection Proxy
- T0888: Remote System Information Discovery
- T1691.001: Command Message
- T1691.002: Reporting Message
- T1692.001: Command Message
- T1695.001: Serial COM
