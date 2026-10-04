# T1090: Proxy


**ATT&CK ID:** T1090  
**Domain:** Mitre Attack  
**Tactic(s):** Command And Control  
**Platforms:** ESXi, Linux, macOS, Network Devices, Windows  
**Reference:** https://attack.mitre.org/techniques/T1090  

## Description
Adversaries may use a connection proxy to direct network traffic between systems or act as an intermediary for network communications to a command and control server to avoid direct connections to their infrastructure. Many tools exist that enable traffic redirection through proxies or port redirection, including [HTRAN](https://attack.mitre.org/software/S0040), ZXProxy, and ZXPortMap. (Citation: Trend Micro APT Attack Tools) Adversaries use these types of proxies to manage command and control communications, reduce the number of simultaneous outbound network connections, provide resiliency in the face of connection loss, or to ride over existing trusted communications paths between victims to avoid suspicion. Adversaries may chain together multiple proxies to further disguise the source of malicious traffic.

Adversaries can also take advantage of routing schemes in Content Delivery Networks (CDNs) to proxy command and control traffic.

## Sub-techniques
- T1090.001: Internal Proxy
- T1090.002: External Proxy
- T1090.003: Multi-hop Proxy
- T1090.004: Domain Fronting

## Mitigations
- M1020: SSL/TLS Inspection
- M1031: Network Intrusion Prevention
- M1037: Filter Network Traffic

## Known Threat Groups Using This Technique
- G0096: APT41
- G0108: Blue Mockingbird
- G1021: Cinnamon Tempest
- G1052: Contagious Interview
- G0052: CopyKittens
- G1006: Earth Lusca
- G0117: Fox Kitten
- G0047: Gamaredon Group
- G1004: LAPSUS$
- G0059: Magic Hound
- G1054: MirrorFace
- G1019: MoustachedBouncer
- G0069: MuddyWater
- G1005: POLONIUM
- G0034: Sandworm Team
- G1015: Scattered Spider
- G0010: Turla
- G1017: Volt Typhoon
- G0124: Windigo

## Known Software Using This Technique
- S0456: Aria-body
- S0347: AuditCred
- S0245: BADCALL
- S1081: BADHATCH
- S0268: Bisonal
- S0348: Cardinal RAT
- S0384: Dridex
- S1144: FRP
- S1044: FunnyDream
- S1197: GoBear
- S0690: Green Lambert
- S0246: HARDRAIN
- S0376: HOPLIGHT
- S0040: HTRAN
- S1229: Havoc
- S1051: KEYPLUG
- S0669: KOCTOPUS
- S9044: Kali365
- S1190: Kapeka
- S0487: Kessel
- S1121: LITTLELAMB.WOOLTEA
- S1141: LunarWeb
- S0198: NETWIRE
- S1189: Neo-reGeorg
- S0435: PLEAD
- S0378: PoshC2
- S0262: QuasarRAT
- S0629: RainyDay
- S1212: RansomHub
- S0332: Remcos
- S0461: SDBbot
- S1210: Sagerunex
- S1099: Samurai
- S0273: Socksbot
- S0615: SombRAT
- S0436: TSCookie
- S0263: TYPEFRAME
- S0386: Ursnif
- S0207: Vasport
- S0670: WarzoneRAT
- S0117: XTunnel
- S1114: ZIPLINE
- S0412: ZxShell
- S0283: jRAT
- S0108: netsh
- S0508: ngrok
- S1187: reGeorg
