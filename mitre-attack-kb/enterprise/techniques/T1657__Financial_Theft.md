# T1657: Financial Theft


**ATT&CK ID:** T1657  
**Domain:** Mitre Attack  
**Tactic(s):** Impact  
**Platforms:** Linux, macOS, Office Suite, SaaS, Windows  
**Reference:** https://attack.mitre.org/techniques/T1657  

## Description
Adversaries may steal monetary resources from targets through extortion, social engineering, technical theft, or other methods aimed at their own financial gain at the expense of the availability of these resources for victims. Financial theft is the ultimate objective of several popular campaign types including extortion by ransomware,(Citation: FBI-ransomware) business email compromise (BEC) and fraud,(Citation: FBI-BEC) "pig butchering,"(Citation: wired-pig butchering) bank hacking,(Citation: DOJ-DPRK Heist) and exploiting cryptocurrency networks.(Citation: BBC-Ronin) 

Adversaries may [Compromise Accounts](https://attack.mitre.org/techniques/T1586) to conduct unauthorized transfers of funds.(Citation: Internet crime report 2022) In the case of business email compromise or email fraud, an adversary may utilize [Impersonation](https://attack.mitre.org/techniques/T1684/001) of a trusted entity. Once the social engineering is successful, victims can be deceived into sending money to financial accounts controlled by an adversary.(Citation: FBI-BEC) This creates the potential for multiple victims (i.e., compromised accounts as well as the ultimate monetary loss) in incidents involving financial theft.(Citation: VEC)

Extortion by ransomware may occur, for example, when an adversary demands payment from a victim after [Data Encrypted for Impact](https://attack.mitre.org/techniques/T1486) (Citation: NYT-Colonial) and [Exfiltration](https://attack.mitre.org/tactics/TA0010) of data, followed by threatening to leak sensitive data to the public unless payment is made to the adversary.(Citation: Mandiant-leaks) Adversaries may use dedicated leak sites to distribute victim data.(Citation: Crowdstrike-leaks)

Due to the potentially immense business impact of financial theft, an adversary may abuse the possibility of financial theft and seeking monetary gain to divert attention from their true goals such as [Data Destruction](https://attack.mitre.org/techniques/T1485) and business disruption.(Citation: AP-NotPetya)

## Mitigations
- M1017: User Training
- M1018: User Account Management

## Known Threat Groups Using This Technique
- G1024: Akira
- G1049: AppleJeus
- G1021: Cinnamon Tempest
- G1052: Contagious Interview
- G1016: FIN13
- G1032: INC Ransom
- G0094: Kimsuky
- G1026: Malteiro
- G1051: Medusa Group
- G1040: Play
- G1015: Scattered Spider
- G1057: ShinyHunters
- G0083: SilverTerrier
- G1053: Storm-0501
- G1056: TeamPCP
- G1055: VOID MANTICORE
- G1050: Water Galura

## Known Software Using This Technique
- S1246: BeaverTail
- S9004: Crocodilus
- S1111: DarkGate
- S1247: Embargo
- S9010: GlassWorm
- S1245: InvisibleFerret
- S1240: RedLine Stealer
- S9041: TeamPCP Cloud Stealer
