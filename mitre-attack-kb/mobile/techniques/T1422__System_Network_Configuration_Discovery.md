# T1422: System Network Configuration Discovery


**ATT&CK ID:** T1422  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Discovery  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1422  

## Description
Adversaries may look for details about the network configuration and settings, such as IP and/or MAC addresses, of devices they access or through information discovery of remote systems. 

Adversaries may use the information from [System Network Configuration Discovery](https://attack.mitre.org/techniques/T1422) during automated discovery to shape follow-on behaviors, including determining certain access within the target network and what actions to do next. 

On Android, details of onboard network interfaces are accessible to apps through the `java.net.NetworkInterface` class.(Citation: NetworkInterface) Previously, the Android `TelephonyManager` class could be used to gather telephony-related device identifiers, information such as the IMSI, IMEI, and phone number. However, starting with Android 10, only preloaded, carrier, the default SMS, or device and profile owner applications can access the telephony-related device identifiers.(Citation: TelephonyManager) 

 

On iOS, gathering network configuration information is not possible without root access. 

 

Adversaries may use the information from [System Network Configuration Discovery](https://attack.mitre.org/techniques/T1422) during automated discovery to shape follow-on behaviors, including determining certain access within the target network and what actions to do next.

## Sub-techniques
- T1422.001: Internet Connection Discovery
- T1422.002: Wi-Fi Discovery

## Mitigations
- M1006: Use Recent OS Version

## Known Threat Groups Using This Technique
- G1028: APT-C-23

## Known Software Using This Technique
- S0310: ANDROIDOS_ANSERVER.A
- S1061: AbstractEmu
- S0292: AndroRAT
- S1214: Android/SpyAgent
- S0540: Asacub
- S1079: BOULDSPY
- S1215: Binary Validator
- S0432: Bread
- S0529: CarbonSteal
- S0425: Corona Updates
- S9005: DocSwap
- S0315: DualToy
- S0478: EventBot
- S0522: Exobot
- S0405: Exodus
- S0509: FakeSpy
- S1093: FlyTrap
- S0577: FrozenCell
- S0536: GPlayed
- S1231: GodFather
- S0535: Golden Cup
- S0406: Gustuff
- S1077: Hornbill
- S0463: INSOMNIA
- S1185: LightSpy
- S0407: Monokle
- S0291: PJApps
- S0316: Pegasus for Android
- S1241: RatMilad
- S0326: RedDrop
- S0403: Riltok
- S0411: Rotexy
- S0313: RuMMS
- S0324: SpyDealer
- S0328: Stealth Mango
- S1082: Sunbird
- S0545: TERRACOTTA
- S0329: Tangelo
- S1056: TianySpy
- S1216: TriangleDB
- S0427: TrickMo
- S0506: ViperRAT
- S0489: WolfRAT
- S0318: XLoader for Android
- S0490: XLoader for iOS
- S0311: YiSpecter
