# T1409: Stored Application Data


**ATT&CK ID:** T1409  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Collection  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1409  

## Description
Adversaries may try to access and collect application data resident on the device. Adversaries often target popular applications, such as Facebook, WeChat, and Gmail.(Citation: SWB Exodus March 2019) 

 

Due to mobile OS sandboxing, this technique is only possible in three scenarios: 

 

* An application stores files in unprotected external storage 
* An application stores files in its internal storage directory with insecure permissions (e.g. 777) 
* The adversary gains root permissions on the device

## Mitigations
- M1006: Use Recent OS Version

## Known Threat Groups Using This Technique
- G0034: Sandworm Team

## Known Software Using This Technique
- S1079: BOULDSPY
- S0655: BusyGasper
- S0529: CarbonSteal
- S1243: DCHSpy
- S0505: Desert Scorpion
- S0550: DoubleAgent
- S1092: Escobar
- S0405: Exodus
- S0509: FakeSpy
- S0408: FlexiSpy
- S1103: FlixOnline
- S1067: FluBot
- S1093: FlyTrap
- S0577: FrozenCell
- S0551: GoldenEagle
- S1128: HilalRAT
- S1077: Hornbill
- S1185: LightSpy
- S0485: Mandrake
- S0399: Pallas
- S0316: Pegasus for Android
- S0289: Pegasus for iOS
- S0295: RCSAndroid
- S1062: S.O.V.A.
- S0327: Skygofree
- S0324: SpyDealer
- S1082: Sunbird
- S0329: Tangelo
- S9006: VajraSpy
- S0311: YiSpecter
