# T1102: Web Service


**ATT&CK ID:** T1102  
**Domain:** Mitre Attack  
**Tactic(s):** Command And Control  
**Platforms:** ESXi, Linux, macOS, Windows  
**Reference:** https://attack.mitre.org/techniques/T1102  

## Description
Adversaries may use an existing, legitimate external Web service as a means for relaying data to/from a compromised system. Popular websites, cloud services, and social media acting as a mechanism for C2 may give a significant amount of cover due to the likelihood that hosts within a network are already communicating with them prior to a compromise. Using common services, such as those offered by Google, Microsoft, or Twitter, makes it easier for adversaries to hide in expected noise.(Citation: Broadcom BirdyClient Microsoft Graph API 2024) Web service providers commonly use SSL/TLS encryption, giving adversaries an added level of protection.

Use of Web services may also protect back-end C2 infrastructure from discovery through malware binary analysis while also enabling operational resiliency (since this infrastructure may be dynamically changed).

## Sub-techniques
- T1102.001: Dead Drop Resolver
- T1102.002: Bidirectional Communication
- T1102.003: One-Way Communication

## Mitigations
- M1021: Restrict Web-Based Content
- M1031: Network Intrusion Prevention

## Known Threat Groups Using This Technique
- G0050: APT32
- G1044: APT42
- G1011: EXOTIC LILY
- G0037: FIN6
- G0061: FIN8
- G0117: Fox Kitten
- G0047: Gamaredon Group
- G0100: Inception
- G0140: LazyScripter
- G0129: Mustang Panda
- G1039: RedCurl
- G0106: Rocke
- G0139: TeamTNT
- G0010: Turla
- G1055: VOID MANTICORE

## Known Software Using This Technique
- S9031: AshTag
- S1081: BADHATCH
- S9015: BRICKSTORM
- S0534: Bazar
- S0635: BoomBox
- S1063: Brute Ratel C4
- S1039: Bumblebee
- S1149: CHIMNEYSWEEP
- S0335: Carbon
- S0674: CharmPower
- S1066: DarkTortilla
- S0600: Doki
- S0547: DropBook
- S0561: GuLoader
- S0601: Hildegard
- S9044: Kali365
- S1160: Latrodectus
- S1221: MOPSLED
- S0198: NETWIRE
- S1147: Nightdoor
- S9019: PureCrypter
- S1130: Raspberry Robin
- S1240: RedLine Stealer
- S0649: SMOKEDHAM
- S0546: SharpStage
- S1178: ShrinkLocker
- S0589: Sibot
- S1086: Snip3
- S1124: SocGholish
- S0689: WhisperGate
- S0508: ngrok
