# T1539: Steal Web Session Cookie


**ATT&CK ID:** T1539  
**Domain:** Mitre Attack  
**Tactic(s):** Credential Access  
**Platforms:** Linux, macOS, Office Suite, SaaS, Windows  
**Reference:** https://attack.mitre.org/techniques/T1539  

## Description
An adversary may steal web application or service session cookies and use them to gain access to web applications or Internet services as an authenticated user without needing credentials. Web applications and services often use session cookies as an authentication token after a user has authenticated to a website.

Cookies are often valid for an extended period of time, even if the web application is not actively used. Cookies can be found on disk, in the process memory of the browser, and in network traffic to remote systems. Additionally, other applications on the targets machine might store sensitive authentication cookies in memory (e.g. apps which authenticate to cloud services). Session cookies can be used to bypasses some multi-factor authentication protocols.(Citation: Pass The Cookie)

There are several examples of malware targeting cookies from web browsers on the local system.(Citation: Kaspersky TajMahal April 2019)(Citation: Unit 42 Mac Crypto Cookies January 2019) Adversaries may also steal cookies by injecting malicious JavaScript content into websites or relying on [User Execution](https://attack.mitre.org/techniques/T1204) by tricking victims into running malicious JavaScript in their browser.(Citation: Talos Roblox Scam 2023)(Citation: Krebs Discord Bookmarks 2023)

There are also open source frameworks such as `Evilginx2` and `Muraena` that can gather session cookies through a malicious proxy (e.g., [Adversary-in-the-Middle](https://attack.mitre.org/techniques/T1557)) that can be set up by an adversary and used in phishing campaigns.(Citation: Github evilginx2)(Citation: GitHub Mauraena)

After an adversary acquires a valid cookie, they can then perform a [Web Session Cookie](https://attack.mitre.org/techniques/T1550/004) technique to login to the corresponding web application.

## Mitigations
- M1017: User Training
- M1021: Restrict Web-Based Content
- M1032: Multi-factor Authentication
- M1047: Audit
- M1051: Update Software
- M1054: Software Configuration

## Known Threat Groups Using This Technique
- G1044: APT42
- G0120: Evilnum
- G0094: Kimsuky
- G0030: Lotus Blossom
- G1014: LuminousMoth
- G0034: Sandworm Team
- G1015: Scattered Spider
- G1033: Star Blizzard

## Known Software Using This Technique
- S0657: BLUELIGHT
- S0631: Chaes
- S0492: CookieMiner
- S1111: DarkGate
- S0568: EVILNUM
- S9010: GlassWorm
- S0531: Grandoreiro
- S9044: Kali365
- S9020: LODEINFO
- S1213: Lumma Stealer
- S1146: MgBot
- S0650: QakBot
- S1148: Raccoon Stealer
- S1240: RedLine Stealer
- S1140: Spica
- S1201: TRANSLATEXT
- S0467: TajMahal
- S0658: XCSSET
- S1207: XLoader
- S9003: evilginx2
