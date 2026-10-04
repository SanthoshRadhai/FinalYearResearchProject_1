# T1123: Audio Capture


**ATT&CK ID:** T1123  
**Domain:** Mitre Attack  
**Tactic(s):** Collection  
**Platforms:** Linux, macOS, Windows  
**Reference:** https://attack.mitre.org/techniques/T1123  

## Description
An adversary can leverage a computer's peripheral devices (e.g., microphones and webcams) or applications (e.g., voice and video call services) to capture audio recordings for the purpose of listening into sensitive conversations to gather information.(Citation: ESET Attor Oct 2019)

Malware or scripts may be used to interact with the devices through an available API provided by the operating system or an application to capture audio. Audio files may be written to disk and exfiltrated later.

## Known Threat Groups Using This Technique
- G0067: APT37
- G1055: VOID MANTICORE

## Known Software Using This Technique
- S0438: Attor
- S0234: Bandook
- S0454: Cadelspy
- S0338: Cobian RAT
- S0115: Crimson
- S0213: DOGCALL
- S0334: DarkComet
- S0021: Derusbi
- S0152: EvilGrab
- S0143: Flame
- S0434: Imminent Monitor
- S0260: InvisiMole
- S0163: Janicab
- S1185: LightSpy
- S1016: MacMa
- S0282: MacSpy
- S0409: Machete
- S1146: MgBot
- S0339: Micropsia
- S0336: NanoCore
- S1090: NightClub
- S0194: PowerSploit
- S0192: Pupy
- S0240: ROKRAT
- S0332: Remcos
- S0379: Revenge RAT
- S0098: T9000
- S0467: TajMahal
- S0257: VERMIN
- S0283: jRAT
