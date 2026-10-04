# T1036: Masquerading


**ATT&CK ID:** T1036  
**Domain:** Mitre Attack  
**Tactic(s):** Stealth  
**Platforms:** Containers, ESXi, Linux, macOS, Windows  
**Reference:** https://attack.mitre.org/techniques/T1036  

## Description
Adversaries may attempt to manipulate features of their artifacts to make them appear legitimate or benign to users and/or security tools. Masquerading occurs when the name or location of an object, legitimate or malicious, is manipulated or abused for the sake of evading defenses and observation. This may include manipulating file metadata, tricking users into misidentifying the file type, and giving legitimate task or service names.

Renaming abusable system utilities to evade security monitoring is also a form of [Masquerading](https://attack.mitre.org/techniques/T1036).(Citation: LOLBAS Main Site)

## Sub-techniques
- T1036.001: Invalid Code Signature
- T1036.002: Right-to-Left Override
- T1036.003: Rename Legitimate Utilities
- T1036.004: Masquerade Task or Service
- T1036.005: Match Legitimate Resource Name or Location
- T1036.006: Space after Filename
- T1036.007: Double File Extension
- T1036.008: Masquerade File Type
- T1036.009: Break Process Trees
- T1036.010: Masquerade Account Name
- T1036.011: Overwrite Process Arguments
- T1036.012: Browser Fingerprint

## Mitigations
- M1017: User Training
- M1018: User Account Management
- M1022: Restrict File and Directory Permissions
- M1038: Execution Prevention
- M1040: Behavior Prevention on Endpoint
- M1045: Code Signing
- M1047: Audit
- M1049: Antivirus/Antimalware

## Known Threat Groups Using This Technique
- G0007: APT28
- G0050: APT32
- G1030: Agrius
- G1007: Aoqin Dragon
- G0060: BRONZE BUTLER
- G1052: Contagious Interview
- G1003: Ember Bear
- G1016: FIN13
- G0140: LazyScripter
- G0133: Nomadic Octopus
- G0049: OilRig
- G0068: PLATINUM
- G0034: Sandworm Team
- G1046: Storm-1811
- G0127: TA551
- G0139: TeamTNT
- G0112: Windshift
- G1035: Winter Vivern
- G0128: ZIRCONIUM
- G0045: menuPass

## Known Software Using This Technique
- S0622: AppleSeed
- S1246: BeaverTail
- S0268: Bisonal
- S0635: BoomBox
- S0497: Dacls
- S1111: DarkGate
- S1066: DarkTortilla
- S0673: DarkWatchman
- S9038: DynoWiper
- S0634: EnvyScout
- S0696: Flagpro
- S0661: FoggyWeb
- S9010: GlassWorm
- S1015: Milan
- S0637: NativeZone
- S0368: NotPetya
- S0453: Pony
- S1046: PowGoop
- S0662: RCSession
- S0148: RTM
- S0565: Raindrop
- S0458: Ramsay
- S1240: RedLine Stealer
- S0446: Ryuk
- S1018: Saint Bot
- S0615: SombRAT
- S1183: StrelaStealer
- S0682: TrailBlazer
- S0266: TrickBot
- S1164: UPSTYLE
- S0689: WhisperGate
- S0466: WindTail
- S0658: XCSSET
