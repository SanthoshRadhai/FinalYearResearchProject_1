# S1053: AvosLocker

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1053  
**Aliases:** AvosLocker  
**Platforms:** Linux, Windows  

## Description
[AvosLocker](https://attack.mitre.org/software/S1053) is ransomware written in C++ that has been offered via the Ransomware-as-a-Service (RaaS) model. It was first observed in June 2021 and has been used against financial services, critical manufacturing, government facilities, and other critical infrastructure sectors in the United States. As of March 2022, [AvosLocker](https://attack.mitre.org/software/S1053) had also been used against organizations in Belgium, Canada, China, Germany, Saudi Arabia, Spain, Syria, Taiwan, Turkey, the United Arab Emirates, and the United Kingdom.(Citation: Malwarebytes AvosLocker Jul 2021)(Citation: Trend Micro AvosLocker Apr 2022)(Citation: Joint CSA AvosLocker Mar 2022)

## Techniques Used
- T1027: Obfuscated Files or Information
- T1027.007: Dynamic API Resolution
- T1036.008: Masquerade File Type
- T1057: Process Discovery
- T1083: File and Directory Discovery
- T1106: Native API
- T1124: System Time Discovery
- T1135: Network Share Discovery
- T1140: Deobfuscate/Decode Files or Information
- T1486: Data Encrypted for Impact
- T1489: Service Stop
- T1529: System Shutdown/Reboot
- T1547.001: Registry Run Keys / Startup Folder
- T1564.003: Hidden Window
- T1688: Safe Mode Boot
