# T1557: Adversary-in-the-Middle


**ATT&CK ID:** T1557  
**Domain:** Mitre Attack  
**Tactic(s):** Credential Access, Collection  
**Platforms:** Linux, macOS, Network Devices, Windows  
**Reference:** https://attack.mitre.org/techniques/T1557  

## Description
Adversaries may attempt to position themselves between two or more networked devices using an adversary-in-the-middle (AiTM) technique to support follow-on behaviors such as [Network Sniffing](https://attack.mitre.org/techniques/T1040), [Transmitted Data Manipulation](https://attack.mitre.org/techniques/T1565/002), or replay attacks ([Exploitation for Credential Access](https://attack.mitre.org/techniques/T1212)). By abusing features of common networking protocols that can determine the flow of network traffic (e.g. ARP, DNS, LLMNR, etc.), adversaries may force a device to communicate through an adversary controlled system so they can collect information or perform additional actions.(Citation: Rapid7 MiTM Basics)

For example, adversaries may manipulate victim DNS settings to enable other malicious activities such as preventing/redirecting users from accessing legitimate sites and/or pushing additional malware.(Citation: ttint_rat)(Citation: dns_changer_trojans)(Citation: ad_blocker_with_miner) Adversaries may also manipulate DNS and leverage their position in order to intercept user credentials, including access tokens ([Steal Application Access Token](https://attack.mitre.org/techniques/T1528)) and session cookies ([Steal Web Session Cookie](https://attack.mitre.org/techniques/T1539)).(Citation: volexity_0day_sophos_FW)(Citation: Token tactics) [Downgrade Attack](https://attack.mitre.org/techniques/T1689)s can also be used to establish an AiTM position, such as by negotiating a less secure, deprecated, or weaker version of communication protocol (SSL/TLS) or encryption algorithm.(Citation: mitm_tls_downgrade_att)(Citation: taxonomy_downgrade_att_tls)(Citation: tlseminar_downgrade_att)

Adversaries may also leverage the AiTM position to attempt to monitor and/or modify traffic, such as in [Transmitted Data Manipulation](https://attack.mitre.org/techniques/T1565/002). Adversaries can setup a position similar to AiTM to prevent traffic from flowing to the appropriate destination, potentially to impair defenses and/or in support of a [Network Denial of Service](https://attack.mitre.org/techniques/T1498).

## Sub-techniques
- T1557.001: Name Resolution Poisoning and SMB Relay
- T1557.002: ARP Cache Poisoning
- T1557.003: DHCP Spoofing
- T1557.004: Evil Twin

## Mitigations
- M1017: User Training
- M1030: Network Segmentation
- M1031: Network Intrusion Prevention
- M1035: Limit Access to Resource Over Network
- M1037: Filter Network Traffic
- M1041: Encrypt Sensitive Information
- M1042: Disable or Remove Feature or Program

## Known Threat Groups Using This Technique
- G0094: Kimsuky
- G0129: Mustang Panda
- G1041: Sea Turtle

## Known Software Using This Technique
- S0281: Dok
- S9044: Kali365
- S1188: Line Runner
- S1131: NPPSPY
- S9003: evilginx2
