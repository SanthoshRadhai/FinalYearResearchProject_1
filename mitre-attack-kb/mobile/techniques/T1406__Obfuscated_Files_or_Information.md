# T1406: Obfuscated Files or Information


**ATT&CK ID:** T1406  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Defense Evasion  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1406  

## Description
Adversaries may attempt to make a payload or file difficult to discover or analyze by encrypting, encoding, or otherwise obfuscating its contents on the device or in transit. This is common behavior that can be used across different platforms and the network to evade defenses. 
 
Payloads may be compressed, archived, or encrypted in order to avoid detection. These payloads may be used during Initial Access or later to mitigate detection. Portions of files can also be encoded to hide the plaintext strings that would otherwise help defenders with discovery. Payloads may also be split into separate, seemingly benign files that only reveal malicious functionality when reassembled.(Citation: Microsoft MalLockerB)

## Sub-techniques
- T1406.001: Steganography
- T1406.002: Software Packing

## Known Threat Groups Using This Technique
- G0112: Windshift

## Known Software Using This Technique
- S1061: AbstractEmu
- S1095: AhRat
- S0525: Android/AdDisplay.Ashas
- S1214: Android/SpyAgent
- S0524: AndroidOS/MalLocker.B
- S0540: Asacub
- S1094: BRATA
- S0293: BrainTest
- S0432: Bread
- S0555: CHEMISTGAMES
- S0529: CarbonSteal
- S0480: Cerberus
- S0323: Charger
- S9004: Crocodilus
- S9005: DocSwap
- S0550: DoubleAgent
- S1054: Drinik
- S0420: Dvmap
- S0478: EventBot
- S0509: FakeSpy
- S0408: FlexiSpy
- S1067: FluBot
- S0536: GPlayed
- S0423: Ginp
- S1231: GodFather
- S0421: GolfSpy
- S0406: Gustuff
- S0544: HenBox
- S0463: INSOMNIA
- S1185: LightSpy
- S0485: Mandrake
- S0407: Monokle
- S0286: OBAD
- S0399: Pallas
- S0539: Red Alert 2.0
- S0411: Rotexy
- S1055: SharkBot
- S0549: SilkBean
- S1195: SpyC23
- S0545: TERRACOTTA
- S1056: TianySpy
- S0427: TrickMo
- S0312: WireLurker
- S0489: WolfRAT
- S0318: XLoader for Android
- S0494: Zen
