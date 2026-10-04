# T1583: Acquire Infrastructure


**ATT&CK ID:** T1583  
**Domain:** Mitre Attack  
**Tactic(s):** Resource Development  
**Platforms:** PRE  
**Reference:** https://attack.mitre.org/techniques/T1583  

## Description
Adversaries may buy, lease, rent, or obtain infrastructure that can be used during targeting. A wide variety of infrastructure exists for hosting and orchestrating adversary operations. Infrastructure solutions include physical or cloud servers, domains, and third-party web services.(Citation: TrendmicroHideoutsLease) Some infrastructure providers offer free trial periods, enabling infrastructure acquisition at limited to no cost.(Citation: Free Trial PurpleUrchin) Additionally, botnets are available for rent or purchase.

Use of these infrastructure solutions allows adversaries to stage, launch, and execute operations. Solutions may help adversary operations blend in with traffic that is seen as normal, such as contacting third-party web services or acquiring infrastructure to support [Proxy](https://attack.mitre.org/techniques/T1090), including from residential proxy services.(Citation: amnesty_nso_pegasus)(Citation: FBI Proxies Credential Stuffing)(Citation: Mandiant APT29 Microsoft 365 2022) Depending on the implementation, adversaries may use infrastructure that makes it difficult to physically tie back to them as well as utilize infrastructure that can be rapidly provisioned, modified, and shut down.

## Sub-techniques
- T1583.001: Domains
- T1583.002: DNS Server
- T1583.003: Virtual Private Server
- T1583.004: Server
- T1583.005: Botnet
- T1583.006: Web Services
- T1583.007: Serverless
- T1583.008: Malvertising

## Mitigations
- M1056: Pre-compromise

## Known Threat Groups Using This Technique
- G1030: Agrius
- G1052: Contagious Interview
- G1003: Ember Bear
- G0119: Indrik Spider
- G0094: Kimsuky
- G0034: Sandworm Team
- G1041: Sea Turtle
- G1033: Star Blizzard
- G1056: TeamPCP
