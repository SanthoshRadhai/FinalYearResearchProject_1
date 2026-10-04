# T1512: Video Capture


**ATT&CK ID:** T1512  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Collection  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1512  

## Description
An adversary can leverage a device’s cameras to gather information by capturing video recordings. Images may also be captured, potentially in specified intervals, in lieu of video files.  

 

Malware or scripts may interact with the device cameras through an available API provided by the operating system. Video or image files may be written to disk and exfiltrated later. This technique differs from [Screen Capture](https://attack.mitre.org/techniques/T1513) due to use of the device’s cameras for video recording rather than capturing the victim’s screen. 

 

In Android, an application must hold the `android.permission.CAMERA` permission to access the cameras. In iOS, applications must include the `NSCameraUsageDescription` key in the `Info.plist` file. In both cases, the user must grant permission to the requesting application to use the camera. If the device has been rooted or jailbroken, an adversary may be able to access the camera without knowledge of the user.

## Mitigations
- M1006: Use Recent OS Version

## Known Threat Groups Using This Technique
- G0112: Windshift

## Known Software Using This Technique
- S1061: AbstractEmu
- S0292: AndroRAT
- S1079: BOULDSPY
- S0655: BusyGasper
- S0426: Concipit1248
- S0425: Corona Updates
- S9004: Crocodilus
- S1243: DCHSpy
- S0301: Dendroid
- S0505: Desert Scorpion
- S9005: DocSwap
- S0320: DroidJack
- S1092: Escobar
- S0405: Exodus
- S1080: Fakecalls
- S0408: FlexiSpy
- S0535: Golden Cup
- S0551: GoldenEagle
- S0421: GolfSpy
- S0544: HenBox
- S1128: HilalRAT
- S1077: Hornbill
- S1185: LightSpy
- S0407: Monokle
- S0399: Pallas
- S0316: Pegasus for Android
- S1126: Phenakite
- S0295: RCSAndroid
- S1241: RatMilad
- S0549: SilkBean
- S0327: Skygofree
- S1195: SpyC23
- S0324: SpyDealer
- S0328: Stealth Mango
- S1082: Sunbird
- S1069: TangleBot
- S0558: Tiktok Pro
- S9006: VajraSpy
- S0418: ViceLeaker
- S0506: ViperRAT
- S0489: WolfRAT
