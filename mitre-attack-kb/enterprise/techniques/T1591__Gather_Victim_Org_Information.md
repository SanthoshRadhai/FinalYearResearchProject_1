# T1591: Gather Victim Org Information


**ATT&CK ID:** T1591  
**Domain:** Mitre Attack  
**Tactic(s):** Reconnaissance  
**Platforms:** PRE  
**Reference:** https://attack.mitre.org/techniques/T1591  

## Description
Adversaries may gather information about the victim's organization that can be used during targeting. Information about an organization may include a variety of details, including the names of divisions/departments, specifics of business operations, as well as the roles and responsibilities of key employees.

Adversaries may gather this information in various ways, such as direct elicitation via [Phishing for Information](https://attack.mitre.org/techniques/T1598). Information about an organization may also be exposed to adversaries via online or other accessible data sets (ex: [Social Media](https://attack.mitre.org/techniques/T1593/001) or [Search Victim-Owned Websites](https://attack.mitre.org/techniques/T1594)).(Citation: ThreatPost Broadvoice Leak)(Citation: SEC EDGAR Search) Gathering this information may reveal opportunities for other forms of reconnaissance (ex: [Phishing for Information](https://attack.mitre.org/techniques/T1598) or [Search Open Websites/Domains](https://attack.mitre.org/techniques/T1593)), establishing operational resources (ex: [Establish Accounts](https://attack.mitre.org/techniques/T1585) or [Compromise Accounts](https://attack.mitre.org/techniques/T1586)), and/or initial access (ex: [Phishing](https://attack.mitre.org/techniques/T1566) or [Trusted Relationship](https://attack.mitre.org/techniques/T1199)).

## Sub-techniques
- T1591.001: Determine Physical Locations
- T1591.002: Business Relationships
- T1591.003: Identify Business Tempo
- T1591.004: Identify Roles

## Mitigations
- M1056: Pre-compromise

## Known Threat Groups Using This Technique
- G0007: APT28
- G0046: FIN7
- G0094: Kimsuky
- G0032: Lazarus Group
- G1054: MirrorFace
- G1036: Moonstone Sleet
- G1017: Volt Typhoon
