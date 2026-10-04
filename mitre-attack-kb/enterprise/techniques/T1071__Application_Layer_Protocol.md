# T1071: Application Layer Protocol


**ATT&CK ID:** T1071  
**Domain:** Mitre Attack  
**Tactic(s):** Command And Control  
**Platforms:** Linux, macOS, Windows, Network Devices, ESXi  
**Reference:** https://attack.mitre.org/techniques/T1071  

## Description
Adversaries may communicate using OSI application layer protocols to avoid detection/network filtering by blending in with existing traffic. Commands to the remote system, and often the results of those commands, will be embedded within the protocol traffic between the client and server. 

Adversaries may utilize many different protocols, including those used for web browsing, transferring files, electronic mail, DNS, or publishing/subscribing. For connections that occur internally within an enclave (such as those between a proxy or pivot node and other nodes), commonly used protocols are SMB, SSH, or RDP.(Citation: Mandiant APT29 Eye Spy Email Nov 22)

## Sub-techniques
- T1071.001: Web Protocols
- T1071.002: File Transfer Protocols
- T1071.003: Mail Protocols
- T1071.004: DNS
- T1071.005: Publish/Subscribe Protocols

## Mitigations
- M1031: Network Intrusion Prevention
- M1037: Filter Network Traffic

## Known Threat Groups Using This Technique
- G1032: INC Ransom
- G0059: Magic Hound
- G0106: Rocke
- G0139: TeamTNT
- G1047: Velvet Ant

## Known Software Using This Technique
- S0660: Clambling
- S0038: Duqu
- S0601: Hildegard
- S0532: Lucifer
- S0034: NETEAGLE
- S1147: Nightdoor
- S1084: QUIETEXIT
- S1130: Raspberry Robin
- S0623: Siloscape
- S0633: Sliver
