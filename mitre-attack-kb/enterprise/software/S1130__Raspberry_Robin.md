# S1130: Raspberry Robin

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1130  
**Aliases:** Raspberry Robin  
**Platforms:** Windows  

## Description
[Raspberry Robin](https://attack.mitre.org/software/S1130) is initial access malware first identified in September 2021, and active through early 2024. The malware is notable for spreading via infected USB devices containing a malicious LNK object that, on execution, retrieves remote hosted payloads for installation. [Raspberry Robin](https://attack.mitre.org/software/S1130) has been widely used against various industries and geographies, and as a precursor to information stealer, ransomware, and other payloads such as [SocGholish](https://attack.mitre.org/software/S1124), [Cobalt Strike](https://attack.mitre.org/software/S0154), [IcedID](https://attack.mitre.org/software/S0483), and [Bumblebee](https://attack.mitre.org/software/S1039).(Citation: TrendMicro RaspberryRobin 2022)(Citation: RedCanary RaspberryRobin 2022)(Citation: HP RaspberryRobin 2024) The DLL componenet in the [Raspberry Robin](https://attack.mitre.org/software/S1130) infection chain is also referred to as "Roshtyak."(Citation: Avast RaspberryRobin 2022) The name "Raspberry Robin" is used to refer to both the malware as well as the threat actor associated with its use, although the Raspberry Robin operators are also tracked as <code>Storm-0856</code> by some vendors.(Citation: Microsoft RaspberryRobin 2022)

## Techniques Used
- T1027: Obfuscated Files or Information
- T1027.002: Software Packing
- T1033: System Owner/User Discovery
- T1036.004: Masquerade Task or Service
- T1036.008: Masquerade File Type
- T1047: Windows Management Instrumentation
- T1055.012: Process Hollowing
- T1057: Process Discovery
- T1059: Command and Scripting Interpreter
- T1059.003: Windows Command Shell
- T1070.004: File Deletion
- T1070.009: Clear Persistence
- T1071: Application Layer Protocol
- T1071.001: Web Protocols
- T1082: System Information Discovery
- T1083: File and Directory Discovery
- T1091: Replication Through Removable Media
- T1102: Web Service
- T1105: Ingress Tool Transfer
- T1140: Deobfuscate/Decode Files or Information
- T1204: User Execution
- T1218.007: Msiexec
- T1218.008: Odbcconf
- T1218.010: Regsvr32
- T1218.011: Rundll32
- T1480: Execution Guardrails
- T1497: Virtualization/Sandbox Evasion
- T1497.001: System Checks
- T1518.001: Security Software Discovery
- T1547.001: Registry Run Keys / Startup Folder
- T1548: Abuse Elevation Control Mechanism
- T1548.002: Bypass User Account Control
- T1559: Inter-Process Communication
- T1559.001: Component Object Model
- T1571: Non-Standard Port
- T1574: Hijack Execution Flow
- T1574.001: DLL
- T1583.001: Domains
- T1583.008: Malvertising
- T1622: Debugger Evasion
- T1685: Disable or Modify Tools
