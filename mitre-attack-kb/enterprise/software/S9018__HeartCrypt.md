# S9018: HeartCrypt

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S9018  
**Aliases:** HeartCrypt  
**Platforms:** Linux, Windows  

## Description
[HeartCrypt](https://attack.mitre.org/software/S9018) is a packer-as-a-service (PaaS) used to protect malware that has been available since at least 2024. [HeartCrypt](https://attack.mitre.org/software/S9018) has been used to pack a variety of malware including [Lumma Stealer](https://attack.mitre.org/software/S1213), [Remcos](https://attack.mitre.org/software/S0332), and Rhadamanthys. In the [HeartCrypt](https://attack.mitre.org/software/S9018) PaaS model, customers submit malware via private messaging services and it is then packed and returned by the operator as a new binary.(Citation: Palo Alto HeartCrypt DEC 2024)

## Techniques Used
- T1027.001: Binary Padding
- T1027.002: Software Packing
- T1027.013: Encrypted/Encoded File
- T1036.008: Masquerade File Type
- T1055.004: Asynchronous Procedure Call
- T1055.012: Process Hollowing
- T1059.003: Windows Command Shell
- T1106: Native API
- T1140: Deobfuscate/Decode Files or Information
- T1497.001: System Checks
- T1547.001: Registry Run Keys / Startup Folder
