# T1001: Data Obfuscation


**ATT&CK ID:** T1001  
**Domain:** Mitre Attack  
**Tactic(s):** Command And Control  
**Platforms:** ESXi, Linux, macOS, Windows  
**Reference:** https://attack.mitre.org/techniques/T1001  

## Description
Adversaries may obfuscate command and control traffic to make it more difficult to detect.(Citation: Bitdefender FunnyDream Campaign November 2020) Command and control (C2) communications are hidden (but not necessarily encrypted) in an attempt to make the content more difficult to discover or decipher and to make the communication less conspicuous and hide commands from being seen. This encompasses many methods, such as adding junk data to protocol traffic, using steganography, or impersonating legitimate protocols.

## Sub-techniques
- T1001.001: Junk Data
- T1001.002: Steganography
- T1001.003: Protocol or Service Impersonation

## Mitigations
- M1031: Network Intrusion Prevention

## Known Threat Groups Using This Technique
- G0047: Gamaredon Group

## Known Software Using This Technique
- S1111: DarkGate
- S1120: FRAMESTING
- S0381: FlawedAmmyy
- S1044: FunnyDream
- S1100: Ninja
- S0439: Okrum
- S0495: RDAT
- S0533: SLOTHFULMEDIA
- S0610: SideTwist
- S1183: StrelaStealer
- S9001: SystemBC
- S0682: TrailBlazer
- S9003: evilginx2
