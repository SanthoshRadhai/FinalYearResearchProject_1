# S1084: QUIETEXIT

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1084  
**Aliases:** QUIETEXIT  
**Platforms:** Network Devices  

## Description
[QUIETEXIT](https://attack.mitre.org/software/S1084) is a novel backdoor, based on the open-source Dropbear SSH client-server software, that has been used by [APT29](https://attack.mitre.org/groups/G0016) since at least 2021. [APT29](https://attack.mitre.org/groups/G0016) has deployed [QUIETEXIT](https://attack.mitre.org/software/S1084) on opaque network appliances that typically don't support antivirus or endpoint detection and response tools within a victim environment.(Citation: Mandiant APT29 Eye Spy Email Nov 22)

## Techniques Used
- T1008: Fallback Channels
- T1036.005: Match Legitimate Resource Name or Location
- T1071: Application Layer Protocol
- T1090.002: External Proxy
- T1095: Non-Application Layer Protocol
