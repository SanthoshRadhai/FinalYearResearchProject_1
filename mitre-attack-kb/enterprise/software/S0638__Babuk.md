# S0638: Babuk

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0638  
**Aliases:** Babuk, Babyk, Vasa Locker  
**Platforms:** Windows, Linux  

## Description
[Babuk](https://attack.mitre.org/software/S0638) is a Ransomware-as-a-service (RaaS) malware that has been used since at least 2021. The operators of [Babuk](https://attack.mitre.org/software/S0638) employ a "Big Game Hunting" approach to targeting major enterprises and operate a leak site to post stolen data as part of their extortion scheme.(Citation: Sogeti CERT ESEC Babuk March 2021)(Citation: McAfee Babuk February 2021)(Citation: CyberScoop Babuk February 2021)

## Techniques Used
- T1007: System Service Discovery
- T1027.002: Software Packing
- T1049: System Network Connections Discovery
- T1057: Process Discovery
- T1059.003: Windows Command Shell
- T1083: File and Directory Discovery
- T1106: Native API
- T1135: Network Share Discovery
- T1140: Deobfuscate/Decode Files or Information
- T1486: Data Encrypted for Impact
- T1489: Service Stop
- T1490: Inhibit System Recovery
- T1680: Local Storage Discovery
- T1685: Disable or Modify Tools
