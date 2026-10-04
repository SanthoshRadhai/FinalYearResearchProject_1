# T1482: Domain Trust Discovery


**ATT&CK ID:** T1482  
**Domain:** Mitre Attack  
**Tactic(s):** Discovery  
**Platforms:** Windows  
**Reference:** https://attack.mitre.org/techniques/T1482  

## Description
Adversaries may attempt to gather information on domain trust relationships that may be used to identify lateral movement opportunities in Windows multi-domain/forest environments. Domain trusts provide a mechanism for a domain to allow access to resources based on the authentication procedures of another domain.(Citation: Microsoft Trusts) Domain trusts allow the users of the trusted domain to access resources in the trusting domain. The information discovered may help the adversary conduct [SID-History Injection](https://attack.mitre.org/techniques/T1134/005), [Pass the Ticket](https://attack.mitre.org/techniques/T1550/003), and [Kerberoasting](https://attack.mitre.org/techniques/T1558/003).(Citation: AdSecurity Forging Trust Tickets)(Citation: Harmj0y Domain Trusts) Domain trusts can be enumerated using the `DSEnumerateDomainTrusts()` Win32 API call, .NET methods, and LDAP.(Citation: Harmj0y Domain Trusts) The Windows utility [Nltest](https://attack.mitre.org/software/S0359) is known to be used by adversaries to enumerate domain trusts.(Citation: Microsoft Operation Wilysupply)

## Mitigations
- M1030: Network Segmentation
- M1047: Audit

## Known Threat Groups Using This Technique
- G1024: Akira
- G1043: BlackByte
- G0114: Chimera
- G1006: Earth Lusca
- G0061: FIN8
- G0030: Lotus Blossom
- G0059: Magic Hound
- G1054: MirrorFace
- G1053: Storm-0501
- G1046: Storm-1811

## Known Software Using This Technique
- S0552: AdFind
- S1081: BADHATCH
- S0534: Bazar
- S0521: BloodHound
- S1063: Brute Ratel C4
- S1159: DUSTTRAP
- S0363: Empire
- S0483: IcedID
- S9035: LAMEHUG
- S1160: Latrodectus
- S1146: MgBot
- S0359: Nltest
- S1145: Pikabot
- S0378: PoshC2
- S0194: PowerSploit
- S0650: QakBot
- S1071: Rubeus
- S1124: SocGholish
- S0266: TrickBot
- S0105: dsquery
