# S1078: RotaJakiro

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1078  
**Aliases:** RotaJakiro  
**Platforms:** Linux  

## Description
[RotaJakiro](https://attack.mitre.org/software/S1078) is a 64-bit Linux backdoor used by [APT32](https://attack.mitre.org/groups/G0050). First seen in 2018, it uses a plugin architecture to extend capabilities. [RotaJakiro](https://attack.mitre.org/software/S1078) can determine it's permission level and execute according to access type (`root` or `user`).(Citation: RotaJakiro 2021 netlab360 analysis)(Citation: netlab360 rotajakiro vs oceanlotus)

## Techniques Used
- T1036.005: Match Legitimate Resource Name or Location
- T1037: Boot or Logon Initialization Scripts
- T1041: Exfiltration Over C2 Channel
- T1057: Process Discovery
- T1082: System Information Discovery
- T1095: Non-Application Layer Protocol
- T1106: Native API
- T1119: Automated Collection
- T1129: Shared Modules
- T1132.001: Standard Encoding
- T1140: Deobfuscate/Decode Files or Information
- T1543.002: Systemd Service
- T1546.004: Unix Shell Configuration Modification
- T1547.013: XDG Autostart Entries
- T1559: Inter-Process Communication
- T1571: Non-Standard Port
- T1573.001: Symmetric Cryptography
