# T1078: Valid Accounts


**ATT&CK ID:** T1078  
**Domain:** Mitre Attack  
**Tactic(s):** Stealth, Persistence, Privilege Escalation, Initial Access  
**Platforms:** Containers, ESXi, IaaS, Identity Provider, Linux, macOS, Network Devices, Office Suite, SaaS, Windows  
**Reference:** https://attack.mitre.org/techniques/T1078  

## Description
Adversaries may obtain and abuse credentials of existing accounts as a means of gaining Initial Access, Persistence, Privilege Escalation, or Defense Evasion. Compromised credentials may be used to bypass access controls placed on various resources on systems within the network and may even be used for persistent access to remote systems and externally available services, such as VPNs, Outlook Web Access, network devices, and remote desktop.(Citation: volexity_0day_sophos_FW) Compromised credentials may also grant an adversary increased privilege to specific systems or access to restricted areas of the network. Adversaries may choose not to use malware or tools in conjunction with the legitimate access those credentials provide to make it harder to detect their presence.

In some cases, adversaries may abuse inactive accounts: for example, those belonging to individuals who are no longer part of an organization. Using these accounts may allow the adversary to evade detection, as the original account user will not be present to identify any anomalous activity taking place on their account.(Citation: CISA MFA PrintNightmare)

The overlap of permissions for local, domain, and cloud accounts across a network of systems is of concern because the adversary may be able to pivot across accounts and systems to reach a high level of access (i.e., domain or enterprise administrator) to bypass access controls set within the enterprise.(Citation: TechNet Credential Theft)

## Sub-techniques
- T1078.001: Default Accounts
- T1078.002: Domain Accounts
- T1078.003: Local Accounts
- T1078.004: Cloud Accounts

## Mitigations
- M1013: Application Developer Guidance
- M1015: Active Directory Configuration
- M1017: User Training
- M1018: User Account Management
- M1026: Privileged Account Management
- M1027: Password Policies
- M1032: Multi-factor Authentication
- M1036: Account Use Policies

## Known Threat Groups Using This Technique
- G0026: APT18
- G0007: APT28
- G0016: APT29
- G0064: APT33
- G0087: APT39
- G0096: APT41
- G1024: Akira
- G0001: Axiom
- G1043: BlackByte
- G0008: Carbanak
- G0114: Chimera
- G1021: Cinnamon Tempest
- G0035: Dragonfly
- G0051: FIN10
- G0085: FIN4
- G0053: FIN5
- G0037: FIN6
- G0046: FIN7
- G0061: FIN8
- G0117: Fox Kitten
- G0093: GALLIUM
- G1032: INC Ransom
- G0119: Indrik Spider
- G0004: Ke3chang
- G1004: LAPSUS$
- G0032: Lazarus Group
- G0065: Leviathan
- G1051: Medusa Group
- G0049: OilRig
- G1005: POLONIUM
- G0011: PittyTiger
- G1040: Play
- G0034: Sandworm Team
- G1015: Scattered Spider
- G1041: Sea Turtle
- G1057: ShinyHunters
- G0091: Silence
- G0122: Silent Librarian
- G1033: Star Blizzard
- G0039: Suckfly
- G1056: TeamPCP
- G0027: Threat Group-3390
- G1048: UNC3886
- G1055: VOID MANTICORE
- G1017: Volt Typhoon
- G0102: Wizard Spider
- G0045: menuPass

## Known Software Using This Technique
- S0567: Dtrack
- S0038: Duqu
- S0604: Industroyer
- S0599: Kinsing
- S9036: LP-Notes
- S0362: Linux Rabbit
- S0053: SeaDuke
