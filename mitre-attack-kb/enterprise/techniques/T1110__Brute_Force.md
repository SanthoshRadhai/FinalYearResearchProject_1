# T1110: Brute Force


**ATT&CK ID:** T1110  
**Domain:** Mitre Attack  
**Tactic(s):** Credential Access  
**Platforms:** Containers, ESXi, IaaS, Identity Provider, Linux, macOS, Network Devices, Office Suite, SaaS, Windows  
**Reference:** https://attack.mitre.org/techniques/T1110  

## Description
Adversaries may use brute force techniques to gain access to accounts when passwords are unknown or when password hashes are obtained.(Citation: TrendMicro Pawn Storm Dec 2020) Without knowledge of the password for an account or set of accounts, an adversary may systematically guess the password using a repetitive or iterative mechanism.(Citation: Dragos Crashoverride 2018) Brute forcing passwords can take place via interaction with a service that will check the validity of those credentials or offline against previously acquired credential data, such as password hashes.

Brute forcing credentials may take place at various points during a breach. For example, adversaries may attempt to brute force access to [Valid Accounts](https://attack.mitre.org/techniques/T1078) within a victim environment leveraging knowledge gathered from other post-compromise behaviors such as [OS Credential Dumping](https://attack.mitre.org/techniques/T1003), [Account Discovery](https://attack.mitre.org/techniques/T1087), or [Password Policy Discovery](https://attack.mitre.org/techniques/T1201). Adversaries may also combine brute forcing activity with behaviors such as [External Remote Services](https://attack.mitre.org/techniques/T1133) as part of Initial Access. 

If an adversary guesses the correct password but fails to login to a compromised account due to location-based conditional access policies, they may change their infrastructure until they match the victim’s location and therefore bypass those policies.(Citation: ReliaQuest Health Care Social Engineering Campaign 2024)

## Sub-techniques
- T1110.001: Password Guessing
- T1110.002: Password Cracking
- T1110.003: Password Spraying
- T1110.004: Credential Stuffing

## Mitigations
- M1018: User Account Management
- M1027: Password Policies
- M1032: Multi-factor Authentication
- M1036: Account Use Policies

## Known Threat Groups Using This Technique
- G0007: APT28
- G0082: APT38
- G0087: APT39
- G0096: APT41
- G1030: Agrius
- G0105: DarkVishnya
- G0035: Dragonfly
- G1003: Ember Bear
- G0053: FIN5
- G0117: Fox Kitten
- G1001: HEXANE
- G0049: OilRig
- G1057: ShinyHunters
- G1053: Storm-0501
- G0010: Turla
- G1055: VOID MANTICORE

## Known Software Using This Technique
- S0572: Caterpillar WebShell
- S0220: Chaos
- S0488: CrackMapExec
- S0599: Kinsing
- S0378: PoshC2
- S0583: Pysa
- S0650: QakBot
