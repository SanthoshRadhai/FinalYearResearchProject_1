# S1096: Cheerscrypt

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1096  
**Aliases:** Cheerscrypt  
**Platforms:** Windows, ESXi  

## Description
[Cheerscrypt](https://attack.mitre.org/software/S1096) is a ransomware that was developed by [Cinnamon Tempest](https://attack.mitre.org/groups/G1021) and has been used in attacks against ESXi and Windows environments since at least 2022. [Cheerscrypt](https://attack.mitre.org/software/S1096) was derived from the leaked [Babuk](https://attack.mitre.org/software/S0638) source code and has infrastructure overlaps with deployments of Night Sky ransomware, which was also derived from [Babuk](https://attack.mitre.org/software/S0638).(Citation: Sygnia Emperor Dragonfly October 2022)(Citation: Trend Micro Cheerscrypt May 2022)

## Techniques Used
- T1059.012: Hypervisor CLI
- T1083: File and Directory Discovery
- T1486: Data Encrypted for Impact
- T1489: Service Stop
- T1673: Virtual Machine Discovery
