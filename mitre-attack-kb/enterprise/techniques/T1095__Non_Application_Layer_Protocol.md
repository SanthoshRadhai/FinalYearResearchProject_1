# T1095: Non-Application Layer Protocol


**ATT&CK ID:** T1095  
**Domain:** Mitre Attack  
**Tactic(s):** Command And Control  
**Platforms:** ESXi, Linux, macOS, Network Devices, Windows  
**Reference:** https://attack.mitre.org/techniques/T1095  

## Description
Adversaries may use an OSI non-application layer protocol for communication between host and C2 server or among infected hosts within a network. The list of possible protocols is extensive.(Citation: Wikipedia OSI) Specific examples include use of network layer protocols, such as the Internet Control Message Protocol (ICMP), transport layer protocols, such as the User Datagram Protocol (UDP), session layer protocols, such as Socket Secure (SOCKS), as well as redirected/tunneled protocols, such as Serial over LAN (SOL).

ICMP communication between hosts is one example.(Citation: Cisco Synful Knock Evolution) Because ICMP is part of the Internet Protocol Suite, it is required to be implemented by all IP-compatible hosts.(Citation: Microsoft ICMP) However, it is not as commonly monitored as other Internet Protocols such as TCP or UDP and may be used by adversaries to hide communications.

In ESXi environments, adversaries may leverage the Virtual Machine Communication Interface (VMCI) for communication between guest virtual machines and the ESXi host. This traffic is similar to client-server communications on traditional network sockets but is localized to the physical machine running the ESXi host, meaning it does not traverse external networks (routers, switches). This results in communications that are invisible to external monitoring and standard networking tools like tcpdump, netstat, nmap, and Wireshark. By adding a VMCI backdoor to a compromised ESXi host, adversaries may persistently regain access from any guest VM to the compromised ESXi host’s backdoor, regardless of network segmentation or firewall rules in place.(Citation: Google Cloud Threat Intelligence VMWare ESXi Zero-Day 2023)

## Mitigations
- M1030: Network Segmentation
- M1031: Network Intrusion Prevention
- M1037: Filter Network Traffic
- M1047: Audit

## Known Threat Groups Using This Technique
- G0022: APT3
- G1002: BITTER
- G0135: BackdoorDiplomacy
- G1003: Ember Bear
- G0037: FIN6
- G0047: Gamaredon Group
- G0125: HAFNIUM
- G1013: Metador
- G0129: Mustang Panda
- G0068: PLATINUM
- G1022: ToddyCat
- G1048: UNC3886

## Known Software Using This Technique
- S0504: Anchor
- S0456: Aria-body
- S1029: AuTo Stealer
- S0043: BUBBLEWRAP
- S0234: Bandook
- S0268: Bisonal
- S1063: Brute Ratel C4
- S1105: COATHANGER
- S0335: Carbon
- S0660: Clambling
- S0154: Cobalt Strike
- S0115: Crimson
- S0498: Cryptoistic
- S1153: Cuckoo Stealer
- S0021: Derusbi
- S0502: Drovorub
- S1144: FRP
- S0076: FakeM
- S1044: FunnyDream
- S0666: Gelsemium
- S9023: HiddenFace
- S0394: HiddenWasp
- S0260: InvisiMole
- S1245: InvisibleFerret
- S1203: J-magic
- S1051: KEYPLUG
- S1121: LITTLELAMB.WOOLTEA
- S0681: Lizar
- S0582: LookBack
- S1142: LunarMail
- S1221: MOPSLED
- S1016: MacMa
- S1060: Mafalda
- S0455: Metamorfo
- S0084: Mis-Type
- S0083: Misdat
- S0149: MoonWind
- S0699: Mythic
- S0034: NETEAGLE
- S0198: NETWIRE
- S0630: Nebulae
- S1189: Neo-reGeorg
- S1100: Ninja
- S0352: OSX_OCEANLOTUS.D
- S0158: PHOREAL
- S0556: Pay2Key
- S0587: Penquin
- S1031: PingPull
- S0501: PipeMon
- S0013: PlugX
- S1084: QUIETEXIT
- S0650: QakBot
- S0262: QuasarRAT
- S0055: RARSTONE
- S0662: RCSession
- S1219: REPTILE
- S0629: RainyDay
- S0172: Reaver
- S0019: Regin
- S0125: Remsec
- S1078: RotaJakiro
- S1073: Royal
- S0461: SDBbot
- S1049: SUGARUSH
- S1099: Samurai
- S1085: Sardonic
- S0596: ShadowPad
- S1163: SnappyTCP
- S0615: SombRAT
- S1140: Spica
- S1227: StarProxy
- S1200: StealBit
- S9001: SystemBC
- S1239: TONESHELL
- S0436: TSCookie
- S0011: Taidoor
- S0221: Umbreon
- S0022: Uroburos
- S0155: WINDSHIELD
- S0670: WarzoneRAT
- S0515: WellMail
- S0430: Winnti for Linux
- S0141: Winnti for Windows
- S1114: ZIPLINE
- S1204: cd00r
- S0032: gh0st RAT
- S1059: metaMain
- S1187: reGeorg
