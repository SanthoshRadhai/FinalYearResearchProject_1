# T1513: Screen Capture


**ATT&CK ID:** T1513  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Collection  
**Platforms:** Android  
**Reference:** https://attack.mitre.org/techniques/T1513  

## Description
Adversaries may use screen capture to collect additional information about a target device, such as applications running in the foreground, user data, credentials, or other sensitive information. Applications running in the background can capture screenshots or videos of another application running in the foreground by using the Android `MediaProjectionManager` (generally requires the device user to grant consent).(Citation: Fortinet screencap July 2019)(Citation: Android ScreenCap1 2019) Background applications can also use Android accessibility services to capture screen contents being displayed by a foreground application.(Citation: Lookout-Monokle) An adversary with root access or Android Debug Bridge (adb) access could call the Android `screencap` or `screenrecord` commands.(Citation: Android ScreenCap2 2019)(Citation: Trend Micro ScreenCap July 2015)

## Mitigations
- M1011: User Guidance
- M1012: Enterprise Policy
- M1013: Application Developer Guidance

## Known Software Using This Technique
- S1095: AhRat
- S0422: Anubis
- S1079: BOULDSPY
- S1094: BRATA
- S0655: BusyGasper
- S1083: Chameleon
- S9004: Crocodilus
- S0479: DEFENSOR ID
- S1054: Drinik
- S0478: EventBot
- S0405: Exodus
- S0408: FlexiSpy
- S0423: Ginp
- S0551: GoldenEagle
- S0421: GolfSpy
- S1077: Hornbill
- S1185: LightSpy
- S0485: Mandrake
- S0407: Monokle
- S1062: S.O.V.A.
- S1195: SpyC23
- S0324: SpyDealer
- S1082: Sunbird
- S1069: TangleBot
- S0558: Tiktok Pro
- S0427: TrickMo
- S0489: WolfRAT
