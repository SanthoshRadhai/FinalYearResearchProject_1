# T1572: Protocol Tunneling


**ATT&CK ID:** T1572  
**Domain:** Mitre Attack  
**Tactic(s):** Command And Control  
**Platforms:** ESXi, Linux, macOS, Windows  
**Reference:** https://attack.mitre.org/techniques/T1572  

## Description
Adversaries may tunnel network communications to and from a victim system within a separate protocol to avoid detection/network filtering and/or enable access to otherwise unreachable systems. Tunneling involves explicitly encapsulating a protocol within another. This behavior may conceal malicious traffic by blending in with existing traffic and/or provide an outer layer of encryption (similar to a VPN). Tunneling could also enable routing of network packets that would otherwise not reach their intended destination, such as SMB, RDP, or other traffic that would be filtered by network appliances or not routed over the Internet. 

There are various means to encapsulate a protocol within another protocol. For example, adversaries may perform SSH tunneling (also known as SSH port forwarding), which involves forwarding arbitrary data over an encrypted SSH tunnel.(Citation: SSH Tunneling)(Citation: Sygnia Abyss Locker 2025) 

[Protocol Tunneling](https://attack.mitre.org/techniques/T1572) may also be abused by adversaries during [Dynamic Resolution](https://attack.mitre.org/techniques/T1568). Known as DNS over HTTPS (DoH), queries to resolve C2 infrastructure may be encapsulated within encrypted HTTPS packets.(Citation: BleepingComp Godlua JUL19) 

Adversaries may also leverage [Protocol Tunneling](https://attack.mitre.org/techniques/T1572) in conjunction with [Proxy](https://attack.mitre.org/techniques/T1090) and/or [Protocol or Service Impersonation](https://attack.mitre.org/techniques/T1001/003) to further conceal C2 communications and infrastructure.

## Mitigations
- M1031: Network Intrusion Prevention
- M1037: Filter Network Traffic

## Known Threat Groups Using This Technique
- G0114: Chimera
- G1021: Cinnamon Tempest
- G0080: Cobalt Group
- G1003: Ember Bear
- G1016: FIN13
- G0037: FIN6
- G0046: FIN7
- G0117: Fox Kitten
- G0065: Leviathan
- G0059: Magic Hound
- G0129: Mustang Panda
- G0049: OilRig
- G1045: Salt Typhoon
- G1015: Scattered Spider
- G1055: VOID MANTICORE

## Known Software Using This Technique
- S9015: BRICKSTORM
- S1063: Brute Ratel C4
- S0154: Cobalt Strike
- S0687: Cyclops Blink
- S0038: Duqu
- S0173: FLIPSIDE
- S1144: FRP
- S1044: FunnyDream
- S1027: Heyoka Backdoor
- S9023: HiddenFace
- S0604: Industroyer
- S1020: Kevin
- S1141: LunarWeb
- S1015: Milan
- S0699: Mythic
- S1189: Neo-reGeorg
- S0650: QakBot
- S9024: SPAWNCHIMERA
- S0022: Uroburos
- S0508: ngrok
- S1187: reGeorg
