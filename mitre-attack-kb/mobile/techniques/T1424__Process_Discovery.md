# T1424: Process Discovery


**ATT&CK ID:** T1424  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Discovery  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1424  

## Description
Adversaries may attempt to get information about running processes on a device. Information obtained could be used to gain an understanding of common software/applications running on devices within a network. Adversaries may use the information from [Process Discovery](https://attack.mitre.org/techniques/T1424) during automated discovery to shape follow-on behaviors, including whether or not the adversary fully infects the target and/or attempts specific actions. 

 

Recent Android security enhancements have made it more difficult to obtain a list of running processes. On Android 7 and later, there is no way for an application to obtain the process list without abusing elevated privileges. This is due to the Android kernel utilizing the `hidepid` mount feature. Prior to Android 7, applications could utilize the `ps` command or examine the `/proc` directory on the device.(Citation: Android-SELinuxChanges) 

 

In iOS, applications have previously been able to use the `sysctl` command to obtain a list of running processes. This functionality has been removed in later iOS versions.

## Mitigations
- M1002: Attestation
- M1006: Use Recent OS Version

## Known Software Using This Technique
- S0440: Agent Smith
- S0422: Anubis
- S1215: Binary Validator
- S1225: CherryBlos
- S0421: GolfSpy
- S0544: HenBox
- S1185: LightSpy
- S0411: Rotexy
- S1055: SharkBot
- S1216: TriangleDB
- S0489: WolfRAT
- S0311: YiSpecter
