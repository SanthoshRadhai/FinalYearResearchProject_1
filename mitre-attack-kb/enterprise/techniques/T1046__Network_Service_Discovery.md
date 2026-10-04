# T1046: Network Service Discovery


**ATT&CK ID:** T1046  
**Domain:** Mitre Attack  
**Tactic(s):** Discovery  
**Platforms:** Containers, IaaS, Linux, macOS, Network Devices, Windows  
**Reference:** https://attack.mitre.org/techniques/T1046  

## Description
Adversaries may attempt to get a listing of services running on remote hosts and local network infrastructure devices, including those that may be vulnerable to remote software exploitation. Common methods to acquire this information include port, vulnerability, and/or wordlist scans using tools that are brought onto a system.(Citation: CISA AR21-126A FIVEHANDS May 2021)   

Within cloud environments, adversaries may attempt to discover services running on other cloud hosts. Additionally, if the cloud environment is connected to a on-premises environment, adversaries may be able to identify services running on non-cloud systems as well.

Within macOS environments, adversaries may use the native Bonjour application to discover services running on other macOS hosts within a network. The Bonjour mDNSResponder daemon automatically registers and advertises a host’s registered services on the network. For example, adversaries can use a mDNS query (such as <code>dns-sd -B _ssh._tcp .</code>) to find other systems broadcasting the ssh service.(Citation: apple doco bonjour description)(Citation: macOS APT Activity Bradley)

## Mitigations
- M1030: Network Segmentation
- M1031: Network Intrusion Prevention
- M1042: Disable or Remove Feature or Program

## Known Threat Groups Using This Technique
- G0050: APT32
- G0087: APT39
- G0096: APT41
- G1030: Agrius
- G0135: BackdoorDiplomacy
- G1043: BlackByte
- G0098: BlackTech
- G0114: Chimera
- G0080: Cobalt Group
- G0105: DarkVishnya
- G1003: Ember Bear
- G1016: FIN13
- G0037: FIN6
- G0117: Fox Kitten
- G1032: INC Ransom
- G0032: Lazarus Group
- G0077: Leafminer
- G0030: Lotus Blossom
- G0059: Magic Hound
- G1051: Medusa Group
- G0129: Mustang Panda
- G0019: Naikon
- G0049: OilRig
- G1039: RedCurl
- G0106: Rocke
- G0039: Suckfly
- G0139: TeamTNT
- G0027: Threat Group-3390
- G0081: Tropic Trooper
- G1017: Volt Typhoon
- G0045: menuPass

## Known Software Using This Technique
- S1081: BADHATCH
- S0093: Backdoor.Oldrea
- S1180: BlackByte Ransomware
- S0089: BlackEnergy
- S1063: Brute Ratel C4
- S0572: Caterpillar WebShell
- S0020: China Chopper
- S0154: Cobalt Strike
- S0608: Conficker
- S0363: Empire
- S1144: FRP
- S0061: HDoor
- S0698: HermeticWizard
- S0601: Hildegard
- S0604: Industroyer
- S0260: InvisiMole
- S0250: Koadic
- S1185: LightSpy
- S0532: Lucifer
- S0233: MURKYTOP
- S1146: MgBot
- S0590: NBTscan
- S0598: P.A.S. Webshell
- S0683: Peirates
- S0378: PoshC2
- S0192: Pupy
- S0583: Pysa
- S0458: Ramsay
- S0125: Remsec
- S1073: Royal
- S0692: SILENTTRINITY
- S0374: SpeakUp
- S0117: XTunnel
- S0341: Xbash
- S0412: ZxShell
