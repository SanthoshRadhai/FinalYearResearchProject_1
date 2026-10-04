# S1203: J-magic

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1203  
**Aliases:** J-magic  
**Platforms:** Network Devices  

## Description
[J-magic](https://attack.mitre.org/software/S1203) is a custom variant of the [cd00r](https://attack.mitre.org/software/S1204) backdoor tailored to target Juniper routers that was first observed during the [J-magic Campaign](https://attack.mitre.org/campaigns/C0050) in mid-2023. [J-magic](https://attack.mitre.org/software/S1203) monitors TCP traffic for five predefined parameters or "magic packets" to be sent by the attackers before activating on compromised devices.(Citation: Lumen J-Magic JAN 2025)

## Techniques Used
- T1016: System Network Configuration Discovery
- T1036.005: Match Legitimate Resource Name or Location
- T1040: Network Sniffing
- T1059.004: Unix Shell
- T1070.003: Clear Command History
- T1095: Non-Application Layer Protocol
- T1205: Traffic Signaling
- T1573.002: Asymmetric Cryptography
