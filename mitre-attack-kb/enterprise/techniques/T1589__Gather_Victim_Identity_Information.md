# T1589: Gather Victim Identity Information


**ATT&CK ID:** T1589  
**Domain:** Mitre Attack  
**Tactic(s):** Reconnaissance  
**Platforms:** PRE  
**Reference:** https://attack.mitre.org/techniques/T1589  

## Description
Adversaries may gather information about the victim's identity that can be used during targeting. Information about identities may include a variety of details, including personal data (ex: employee names, email addresses, security question responses, etc.) as well as sensitive details such as credentials or multi-factor authentication (MFA) configurations.

Adversaries may gather this information in various ways, such as direct elicitation via [Phishing for Information](https://attack.mitre.org/techniques/T1598). Information about users could also be enumerated via other active means (i.e. [Active Scanning](https://attack.mitre.org/techniques/T1595)) such as probing and analyzing responses from authentication services that may reveal valid usernames in a system or permitted MFA /methods associated with those usernames.(Citation: GrimBlog UsernameEnum)(Citation: Obsidian SSPR Abuse 2023) Information about victims may also be exposed to adversaries via online or other accessible data sets (ex: [Social Media](https://attack.mitre.org/techniques/T1593/001) or [Search Victim-Owned Websites](https://attack.mitre.org/techniques/T1594)).(Citation: OPM Leak)(Citation: Register Deloitte)(Citation: Register Uber)(Citation: Detectify Slack Tokens)(Citation: Forbes GitHub Creds)(Citation: GitHub truffleHog)(Citation: GitHub Gitrob)(Citation: CNET Leaks)

Gathering this information may reveal opportunities for other forms of reconnaissance (ex: [Search Open Websites/Domains](https://attack.mitre.org/techniques/T1593) or [Phishing for Information](https://attack.mitre.org/techniques/T1598)), establishing operational resources (ex: [Compromise Accounts](https://attack.mitre.org/techniques/T1586)), and/or initial access (ex: [Phishing](https://attack.mitre.org/techniques/T1566) or [Valid Accounts](https://attack.mitre.org/techniques/T1078)).

## Sub-techniques
- T1589.001: Credentials
- T1589.002: Email Addresses
- T1589.003: Employee Names

## Mitigations
- M1056: Pre-compromise

## Known Threat Groups Using This Technique
- G0050: APT32
- G1052: Contagious Interview
- G1016: FIN13
- G1001: HEXANE
- G1004: LAPSUS$
- G0059: Magic Hound
- G1015: Scattered Spider
- G1033: Star Blizzard
- G1055: VOID MANTICORE
- G1017: Volt Typhoon
