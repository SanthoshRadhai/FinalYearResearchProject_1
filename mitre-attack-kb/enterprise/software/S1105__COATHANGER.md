# S1105: COATHANGER

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1105  
**Aliases:** COATHANGER  
**Platforms:** Linux, Network Devices  

## Description
[COATHANGER](https://attack.mitre.org/software/S1105) is a remote access tool (RAT) targeting FortiGate networking appliances. First used in 2023 in targeted intrusions against military and government entities in the Netherlands along with other victims, [COATHANGER](https://attack.mitre.org/software/S1105) was disclosed in early 2024, with a high confidence assessment linking this malware to a state-sponsored entity in the People's Republic of China. [COATHANGER](https://attack.mitre.org/software/S1105) is delivered after gaining access to a FortiGate device, with in-the-wild observations linked to exploitation of CVE-2022-42475. The name [COATHANGER](https://attack.mitre.org/software/S1105) is based on a unique string in the malware used to encrypt configuration files on disk: <code>“She took his coat and hung it up”</code>.(Citation: NCSC-NL COATHANGER Feb 2024)

## Techniques Used
- T1014: Rootkit
- T1027: Obfuscated Files or Information
- T1027.002: Software Packing
- T1055: Process Injection
- T1057: Process Discovery
- T1059.004: Unix Shell
- T1070.004: File Deletion
- T1071.001: Web Protocols
- T1083: File and Directory Discovery
- T1095: Non-Application Layer Protocol
- T1140: Deobfuscate/Decode Files or Information
- T1190: Exploit Public-Facing Application
- T1222.002: Linux and Mac Permissions
- T1543.004: Launch Daemon
- T1564.001: Hidden Files and Directories
- T1573.002: Asymmetric Cryptography
- T1574: Hijack Execution Flow
- T1574.006: Dynamic Linker Hijacking
