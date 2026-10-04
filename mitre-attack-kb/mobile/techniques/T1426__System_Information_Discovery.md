# T1426: System Information Discovery


**ATT&CK ID:** T1426  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Discovery  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1426  

## Description
Adversaries may attempt to get detailed information about a device’s operating system and hardware, including versions, patches, and architecture. Adversaries may use the information from [System Information Discovery](https://attack.mitre.org/techniques/T1426) during automated discovery to shape follow-on behaviors, including whether or not to fully infects the target and/or attempts specific actions. 

 

On Android, much of this information is programmatically accessible to applications through the `android.os.Build` class. (Citation: Android-Build) iOS is much more restrictive with what information is visible to applications. Typically, applications will only be able to query the device model and which version of iOS it is running.

## Known Threat Groups Using This Technique
- G0112: Windshift

## Known Software Using This Technique
- S0310: ANDROIDOS_ANSERVER.A
- S1061: AbstractEmu
- S1095: AhRat
- S0525: Android/AdDisplay.Ashas
- S0304: Android/Chuli.A
- S0422: Anubis
- S0540: Asacub
- S1079: BOULDSPY
- S1094: BRATA
- S0555: CHEMISTGAMES
- S0529: CarbonSteal
- S0480: Cerberus
- S1083: Chameleon
- S0425: Corona Updates
- S0505: Desert Scorpion
- S9005: DocSwap
- S0550: DoubleAgent
- S0420: Dvmap
- S0478: EventBot
- S0522: Exobot
- S0509: FakeSpy
- S0577: FrozenCell
- S0536: GPlayed
- S1231: GodFather
- S0535: Golden Cup
- S0551: GoldenEagle
- S0421: GolfSpy
- S0406: Gustuff
- S0544: HenBox
- S1077: Hornbill
- S0463: INSOMNIA
- S0288: KeyRaider
- S1185: LightSpy
- S0485: Mandrake
- S0407: Monokle
- S0399: Pallas
- S0289: Pegasus for iOS
- S1126: Phenakite
- S1241: RatMilad
- S0326: RedDrop
- S0403: Riltok
- S0411: Rotexy
- S0313: RuMMS
- S1062: S.O.V.A.
- S1082: Sunbird
- S1056: TianySpy
- S0558: Tiktok Pro
- S0427: TrickMo
- S9006: VajraSpy
- S0418: ViceLeaker
- S0506: ViperRAT
- S0318: XLoader for Android
- S0490: XLoader for iOS
- S0311: YiSpecter
- S0507: eSurv
