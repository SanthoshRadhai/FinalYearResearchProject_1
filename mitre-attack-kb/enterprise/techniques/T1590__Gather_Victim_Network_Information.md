# T1590: Gather Victim Network Information


**ATT&CK ID:** T1590  
**Domain:** Mitre Attack  
**Tactic(s):** Reconnaissance  
**Platforms:** PRE  
**Reference:** https://attack.mitre.org/techniques/T1590  

## Description
Adversaries may gather information about the victim's networks that can be used during targeting. Information about networks may include a variety of details, including administrative data (ex: IP ranges, domain names, etc.) as well as specifics regarding its topology and operations.

Adversaries may gather this information in various ways, such as direct collection actions via [Active Scanning](https://attack.mitre.org/techniques/T1595) or [Phishing for Information](https://attack.mitre.org/techniques/T1598). Information about networks may also be exposed to adversaries via online or other accessible data sets (ex: [Search Open Technical Databases](https://attack.mitre.org/techniques/T1596)).(Citation: WHOIS)(Citation: DNS Dumpster)(Citation: Circl Passive DNS) Gathering this information may reveal opportunities for other forms of reconnaissance (ex: [Active Scanning](https://attack.mitre.org/techniques/T1595) or [Search Open Websites/Domains](https://attack.mitre.org/techniques/T1593)), establishing operational resources (ex: [Acquire Infrastructure](https://attack.mitre.org/techniques/T1583) or [Compromise Infrastructure](https://attack.mitre.org/techniques/T1584)), and/or initial access (ex: [Trusted Relationship](https://attack.mitre.org/techniques/T1199)).

## Sub-techniques
- T1590.001: Domain Properties
- T1590.002: DNS
- T1590.003: Network Trust Dependencies
- T1590.004: Network Topology
- T1590.005: IP Addresses
- T1590.006: Network Security Appliances

## Mitigations
- M1056: Pre-compromise

## Known Threat Groups Using This Technique
- G0125: HAFNIUM
- G0119: Indrik Spider
- G1017: Volt Typhoon
