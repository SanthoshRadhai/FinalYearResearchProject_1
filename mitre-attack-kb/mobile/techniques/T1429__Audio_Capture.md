# T1429: Audio Capture


**ATT&CK ID:** T1429  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Collection  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1429  

## Description
Adversaries may capture audio to collect information by leveraging standard operating system APIs of a mobile device. Examples of audio information adversaries may target include user conversations, surroundings, phone calls, or other sensitive information. 

 

Android and iOS, by default, require that applications request device microphone access from the user.  

 

On Android devices, applications must hold the `RECORD_AUDIO` permission to access the microphone or the `CAPTURE_AUDIO_OUTPUT` permission to access audio output. Because Android does not allow third-party applications to hold the `CAPTURE_AUDIO_OUTPUT` permission by default, only privileged applications, such as those distributed by Google or the device vendor, can access audio output.(Citation: Android Permissions) However, adversaries may be able to gain this access after successfully elevating their privileges. With the `CAPTURE_AUDIO_OUTPUT` permission, adversaries may pass the `MediaRecorder.AudioSource.VOICE_CALL` constant to `MediaRecorder.setAudioOutput`, allowing capture of both voice call uplink and downlink.(Citation: Manifest.permission) 

 

On iOS devices, applications must include the `NSMicrophoneUsageDescription` key in their `Info.plist` file to access the microphone.(Citation: Requesting Auth-Media Capture)

## Mitigations
- M1006: Use Recent OS Version
- M1011: User Guidance

## Known Threat Groups Using This Technique
- G0112: Windshift

## Known Software Using This Technique
- S1061: AbstractEmu
- S1095: AhRat
- S0292: AndroRAT
- S0422: Anubis
- S1079: BOULDSPY
- S0655: BusyGasper
- S0529: CarbonSteal
- S0425: Corona Updates
- S1243: DCHSpy
- S0301: Dendroid
- S0505: Desert Scorpion
- S9005: DocSwap
- S0550: DoubleAgent
- S0320: DroidJack
- S1092: Escobar
- S0405: Exodus
- S1080: Fakecalls
- S0182: FinFisher
- S0408: FlexiSpy
- S0577: FrozenCell
- S1231: GodFather
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
- S0289: Pegasus for iOS
- S1126: Phenakite
- S0295: RCSAndroid
- S1241: RatMilad
- S0326: RedDrop
- S0327: Skygofree
- S1195: SpyC23
- S0324: SpyDealer
- S0305: SpyNote RAT
- S0328: Stealth Mango
- S1082: Sunbird
- S0329: Tangelo
- S1069: TangleBot
- S0558: Tiktok Pro
- S9006: VajraSpy
- S0418: ViceLeaker
- S0506: ViperRAT
- S0489: WolfRAT
- S0318: XLoader for Android
- S0507: eSurv
