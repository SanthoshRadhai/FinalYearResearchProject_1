# T1593: Search Open Websites/Domains


**ATT&CK ID:** T1593  
**Domain:** Mitre Attack  
**Tactic(s):** Reconnaissance  
**Platforms:** PRE  
**Reference:** https://attack.mitre.org/techniques/T1593  

## Description
Adversaries may search freely available websites and/or domains for information about victims that can be used during targeting. Information about victims may be available in various online sites, such as social media, new sites, or those hosting information about business operations such as hiring or requested/rewarded contracts.(Citation: Cyware Social Media)(Citation: SecurityTrails Google Hacking)(Citation: ExploitDB GoogleHacking)

Adversaries may search in different online sites depending on what information they seek to gather. Information from these sources may reveal opportunities for other forms of reconnaissance (ex: [Phishing for Information](https://attack.mitre.org/techniques/T1598) or [Search Open Technical Databases](https://attack.mitre.org/techniques/T1596)), establishing operational resources (ex: [Establish Accounts](https://attack.mitre.org/techniques/T1585) or [Compromise Accounts](https://attack.mitre.org/techniques/T1586)), and/or initial access (ex: [External Remote Services](https://attack.mitre.org/techniques/T1133) or [Phishing](https://attack.mitre.org/techniques/T1566)).

## Sub-techniques
- T1593.001: Social Media
- T1593.002: Search Engines
- T1593.003: Code Repositories

## Mitigations
- M1013: Application Developer Guidance
- M1047: Audit

## Known Threat Groups Using This Technique
- G0099: APT-C-36
- G1052: Contagious Interview
- G0129: Mustang Panda
- G0034: Sandworm Team
- G1033: Star Blizzard
- G1017: Volt Typhoon
