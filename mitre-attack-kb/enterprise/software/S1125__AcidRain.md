# S1125: AcidRain

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1125  
**Aliases:** AcidRain  
**Platforms:** Network Devices, Linux  

## Description
[AcidRain](https://attack.mitre.org/software/S1125) is an ELF binary targeting modems and routers using MIPS architecture.(Citation: AcidRain JAGS 2022) [AcidRain](https://attack.mitre.org/software/S1125) is associated with the ViaSat KA-SAT communication outage that took place during the initial phases of the 2022 full-scale invasion of Ukraine. Analysis indicates overlap with another network device-targeting malware, VPNFilter, associated with [Sandworm Team](https://attack.mitre.org/groups/G0034).(Citation: AcidRain JAGS 2022) US and European government sources linked [AcidRain](https://attack.mitre.org/software/S1125) to Russian government entities, while Ukrainian government sources linked [AcidRain](https://attack.mitre.org/software/S1125) specifically to [Sandworm Team](https://attack.mitre.org/groups/G0034).(Citation: AcidRain State Department 2022)(Citation: Vincens AcidPour 2024)

## Techniques Used
- T1083: File and Directory Discovery
- T1485: Data Destruction
- T1529: System Shutdown/Reboot
- T1561.001: Disk Content Wipe
