# T1596: Search Open Technical Databases


**ATT&CK ID:** T1596  
**Domain:** Mitre Attack  
**Tactic(s):** Reconnaissance  
**Platforms:** PRE  
**Reference:** https://attack.mitre.org/techniques/T1596  

## Description
Adversaries may search freely available technical databases for information about victims that can be used during targeting. Information about victims may be available in online databases and repositories, such as registrations of domains/certificates as well as public collections of network data/artifacts gathered from traffic and/or scans.(Citation: WHOIS)(Citation: DNS Dumpster)(Citation: Circl Passive DNS)(Citation: Medium SSL Cert)(Citation: SSLShopper Lookup)(Citation: DigitalShadows CDN)(Citation: Shodan)

Adversaries may search in different open databases depending on what information they seek to gather. Information from these sources may reveal opportunities for other forms of reconnaissance (ex: [Phishing for Information](https://attack.mitre.org/techniques/T1598) or [Search Open Websites/Domains](https://attack.mitre.org/techniques/T1593)), establishing operational resources (ex: [Acquire Infrastructure](https://attack.mitre.org/techniques/T1583) or [Compromise Infrastructure](https://attack.mitre.org/techniques/T1584)), and/or initial access (ex: [External Remote Services](https://attack.mitre.org/techniques/T1133) or [Trusted Relationship](https://attack.mitre.org/techniques/T1199)).

## Sub-techniques
- T1596.001: DNS/Passive DNS
- T1596.002: WHOIS
- T1596.003: Digital Certificates
- T1596.004: CDNs
- T1596.005: Scan Databases

## Mitigations
- M1056: Pre-compromise

## Known Threat Groups Using This Technique
- G0007: APT28
- G0094: Kimsuky
