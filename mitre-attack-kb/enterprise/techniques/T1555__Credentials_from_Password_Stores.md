# T1555: Credentials from Password Stores


**ATT&CK ID:** T1555  
**Domain:** Mitre Attack  
**Tactic(s):** Credential Access  
**Platforms:** IaaS, Linux, macOS, Windows  
**Reference:** https://attack.mitre.org/techniques/T1555  

## Description
Adversaries may search for common password storage locations to obtain user credentials.(Citation: F-Secure The Dukes) Passwords are stored in several places on a system, depending on the operating system or application holding the credentials. There are also specific applications and services that store passwords to make them easier for users to manage and maintain, such as password managers and cloud secrets vaults. Once credentials are obtained, they can be used to perform lateral movement and access restricted information.

## Sub-techniques
- T1555.001: Keychain
- T1555.002: Securityd Memory
- T1555.003: Credentials from Web Browsers
- T1555.004: Windows Credential Manager
- T1555.005: Password Managers
- T1555.006: Cloud Secrets Management Stores

## Mitigations
- M1026: Privileged Account Management
- M1027: Password Policies
- M1051: Update Software

## Known Threat Groups Using This Technique
- G0064: APT33
- G0087: APT39
- G0096: APT41
- G0120: Evilnum
- G0037: FIN6
- G1001: HEXANE
- G0077: Leafminer
- G1026: Malteiro
- G0069: MuddyWater
- G0049: OilRig
- G0038: Stealth Falcon
- G1017: Volt Typhoon

## Known Software Using This Technique
- S0331: Agent Tesla
- S0373: Astaroth
- S1246: BeaverTail
- S0484: Carberp
- S0050: CosmicDuke
- S1111: DarkGate
- S0526: KGH_SPY
- S0349: LaZagne
- S0447: Lokibot
- S1156: Manjusaka
- S0167: Matryoshka
- S1146: MgBot
- S0002: Mimikatz
- S9022: MirrorStealer
- S1122: Mispadu
- S0198: NETWIRE
- S0138: OLDBAIT
- S0435: PLEAD
- S0048: PinchDuke
- S0378: PoshC2
- S0113: Prikormka
- S0192: Pupy
- S0262: QuasarRAT
- S1240: RedLine Stealer
- S9041: TeamPCP Cloud Stealer
- S1207: XLoader
