# T1133: External Remote Services


**ATT&CK ID:** T1133  
**Domain:** Mitre Attack  
**Tactic(s):** Persistence, Initial Access  
**Platforms:** Containers, Linux, macOS, Windows  
**Reference:** https://attack.mitre.org/techniques/T1133  

## Description
Adversaries may leverage external-facing remote services to initially access and/or persist within a network. Remote services such as VPNs, Citrix, and other access mechanisms allow users to connect to internal enterprise network resources from external locations. There are often remote service gateways that manage connections and credential authentication for these services. Services such as [Windows Remote Management](https://attack.mitre.org/techniques/T1021/006) and [VNC](https://attack.mitre.org/techniques/T1021/005) can also be used externally.(Citation: MacOS VNC software for Remote Desktop)

Access to [Valid Accounts](https://attack.mitre.org/techniques/T1078) to use the service is often a requirement, which could be obtained through credential pharming or by obtaining the credentials from users after compromising the enterprise network.(Citation: Volexity Virtual Private Keylogging) Access to remote services may be used as a redundant or persistent access mechanism during an operation.

Access may also be gained through an exposed service that doesn’t require authentication. In containerized environments, this may include an exposed Docker API, Kubernetes API server, kubelet, or web application such as the Kubernetes dashboard.(Citation: Trend Micro Exposed Docker Server)(Citation: Unit 42 Hildegard Malware)

Adversaries may also establish persistence on network by configuring a Tor hidden service on a compromised system. Adversaries may utilize the tool `ShadowLink` to facilitate the installation and configuration of the Tor hidden service. Tor hidden service is then accessible via the Tor network because `ShadowLink` sets up a .onion address on the compromised system. `ShadowLink` may be used to forward any inbound connections to RDP, allowing the adversaries to have remote access.(Citation: The BadPilot campaign) Adversaries may get `ShadowLink` to persist on a system by masquerading it as an MS Defender application.(Citation: Russian threat actors dig in, prepare to seize on war fatigue)

## Mitigations
- M1021: Restrict Web-Based Content
- M1030: Network Segmentation
- M1032: Multi-factor Authentication
- M1035: Limit Access to Resource Over Network
- M1042: Disable or Remove Feature or Program

## Known Threat Groups Using This Technique
- G0099: APT-C-36
- G0026: APT18
- G0007: APT28
- G0016: APT29
- G0096: APT41
- G1024: Akira
- G0114: Chimera
- G0035: Dragonfly
- G1003: Ember Bear
- G1016: FIN13
- G0053: FIN5
- G0093: GALLIUM
- G0115: GOLD SOUTHFIELD
- G0004: Ke3chang
- G0094: Kimsuky
- G1004: LAPSUS$
- G0065: Leviathan
- G0049: OilRig
- G1040: Play
- G0034: Sandworm Team
- G1015: Scattered Spider
- G1041: Sea Turtle
- G0139: TeamTNT
- G0027: Threat Group-3390
- G1055: VOID MANTICORE
- G1047: Velvet Ant
- G1017: Volt Typhoon
- G0102: Wizard Spider

## Known Software Using This Technique
- S0600: Doki
- S0601: Hildegard
- S0599: Kinsing
- S0362: Linux Rabbit
- S1060: Mafalda
