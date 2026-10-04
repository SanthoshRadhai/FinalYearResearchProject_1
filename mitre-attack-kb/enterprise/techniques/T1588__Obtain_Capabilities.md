# T1588: Obtain Capabilities


**ATT&CK ID:** T1588  
**Domain:** Mitre Attack  
**Tactic(s):** Resource Development  
**Platforms:** PRE  
**Reference:** https://attack.mitre.org/techniques/T1588  

## Description
Adversaries may buy and/or steal capabilities that can be used during targeting. Rather than developing their own capabilities in-house, adversaries may purchase, freely download, or steal them. Activities may include the acquisition of malware, software (including licenses), exploits, certificates, and information relating to vulnerabilities. Adversaries may obtain capabilities to support their operations throughout numerous phases of the adversary lifecycle.

In addition to downloading free malware, software, and exploits from the internet, adversaries may purchase these capabilities from third-party entities. Third-party entities can include technology companies that specialize in malware and exploits, criminal marketplaces, or from individuals.(Citation: NationsBuying)(Citation: PegasusCitizenLab)

In addition to purchasing capabilities, adversaries may steal capabilities from third-party entities (including other adversaries). This can include stealing software licenses, malware, SSL/TLS and code-signing certificates, or raiding closed databases of vulnerabilities or exploits.(Citation: DiginotarCompromise)

## Sub-techniques
- T1588.001: Malware
- T1588.002: Tool
- T1588.003: Code Signing Certificates
- T1588.004: Digital Certificates
- T1588.005: Exploits
- T1588.006: Vulnerabilities
- T1588.007: Artificial Intelligence

## Mitigations
- M1056: Pre-compromise
