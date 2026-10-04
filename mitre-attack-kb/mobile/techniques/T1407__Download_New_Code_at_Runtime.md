# T1407: Download New Code at Runtime


**ATT&CK ID:** T1407  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Defense Evasion  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1407  

## Description
Adversaries may download and execute dynamic code not included in the original application package after installation. This technique is primarily used to evade static analysis checks and pre-publication scans in official app stores. In some cases, more advanced dynamic or behavioral analysis techniques could detect this behavior. However, in conjunction with [Execution Guardrails](https://attack.mitre.org/techniques/T1627) techniques, detecting malicious code downloaded after installation could be difficult.

On Android, dynamic code could include native code, Dalvik code, or JavaScript code that utilizes Android WebView’s `JavascriptInterface` capability. 

On iOS, dynamic code could be downloaded and executed through 3rd party libraries such as JSPatch. (Citation: FireEye-JSPatch)

## Mitigations
- M1006: Use Recent OS Version

## Known Threat Groups Using This Technique
- G0112: Windshift

## Known Software Using This Technique
- S1061: AbstractEmu
- S0422: Anubis
- S1079: BOULDSPY
- S1094: BRATA
- S0293: BrainTest
- S0432: Bread
- S0655: BusyGasper
- S0555: CHEMISTGAMES
- S0529: CarbonSteal
- S0480: Cerberus
- S1083: Chameleon
- S9004: Crocodilus
- S0505: Desert Scorpion
- S0550: DoubleAgent
- S0420: Dvmap
- S0478: EventBot
- S0405: Exodus
- S0577: FrozenCell
- S0536: GPlayed
- S0535: Golden Cup
- S0551: GoldenEagle
- S0544: HenBox
- S0325: Judy
- S0485: Mandrake
- S0295: RCSAndroid
- S1241: RatMilad
- S0539: Red Alert 2.0
- S1055: SharkBot
- S0549: SilkBean
- S0327: Skygofree
- S0324: SpyDealer
- S0545: TERRACOTTA
- S0424: Triada
- S0506: ViperRAT
- S0489: WolfRAT
- S0311: YiSpecter
- S0494: Zen
- S0287: ZergHelper
- S0507: eSurv
