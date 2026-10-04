# T1218: System Binary Proxy Execution


**ATT&CK ID:** T1218  
**Domain:** Mitre Attack  
**Tactic(s):** Stealth  
**Platforms:** Linux, macOS, Windows  
**Reference:** https://attack.mitre.org/techniques/T1218  

## Description
Adversaries may bypass process and/or signature-based defenses by proxying execution of malicious content with signed, or otherwise trusted, binaries. Binaries used in this technique are often Microsoft-signed files, indicating that they have been either downloaded from Microsoft or are already native in the operating system.(Citation: LOLBAS Project) Binaries signed with trusted digital certificates can typically execute on Windows systems protected by digital signature validation. Several Microsoft signed binaries that are default on Windows installations can be used to proxy execution of other files or commands.

Similarly, on Linux systems adversaries may abuse trusted binaries such as <code>split</code> to proxy execution of malicious commands.(Citation: split man page)(Citation: GTFO split)

## Sub-techniques
- T1218.001: Compiled HTML File
- T1218.002: Control Panel
- T1218.003: CMSTP
- T1218.004: InstallUtil
- T1218.005: Mshta
- T1218.007: Msiexec
- T1218.008: Odbcconf
- T1218.009: Regsvcs/Regasm
- T1218.010: Regsvr32
- T1218.011: Rundll32
- T1218.012: Verclsid
- T1218.013: Mavinject
- T1218.014: MMC
- T1218.015: Electron Applications

## Mitigations
- M1021: Restrict Web-Based Content
- M1026: Privileged Account Management
- M1037: Filter Network Traffic
- M1038: Execution Prevention
- M1042: Disable or Remove Feature or Program
- M1050: Exploit Protection

## Known Threat Groups Using This Technique
- G0032: Lazarus Group
- G1017: Volt Typhoon
