# T1195: Supply Chain Compromise


**ATT&CK ID:** T1195  
**Domain:** Mitre Attack  
**Tactic(s):** Initial Access  
**Platforms:** Linux, Windows, macOS, SaaS  
**Reference:** https://attack.mitre.org/techniques/T1195  

## Description
Adversaries may manipulate products or product delivery mechanisms prior to receipt by a final consumer for the purpose of data or system compromise.

Supply chain compromise can take place at any stage of the supply chain including:

* Manipulation of development tools
* Manipulation of a development environment
* Manipulation of source code repositories (public or private)
* Manipulation of source code in open-source dependencies
* Manipulation of software update/distribution mechanisms
* Compromised/infected system images (removable media infected at the factory)(Citation: IBM Storwize)(Citation: Schneider Electric USB Malware) 
* Replacement of legitimate software with modified versions
* Sales of modified/counterfeit products to legitimate distributors
* Shipment interdiction

While supply chain compromise can impact any component of hardware or software, adversaries looking to gain execution have often focused on malicious additions to legitimate software in software distribution or update channels.(Citation: Avast CCleaner3 2018)(Citation: Microsoft Dofoil 2018)(Citation: Command Five SK 2011) Adversaries may limit targeting to a desired victim set or distribute malicious software to a broad set of consumers but only follow up with specific victims.(Citation: Symantec Elderwood Sept 2012)(Citation: Avast CCleaner3 2018)(Citation: Command Five SK 2011) Popular open-source projects that are used as dependencies in many applications may also be targeted as a means to add malicious code to users of the dependency.(Citation: Trendmicro NPM Compromise)

In some cases, adversaries may conduct “second-order” supply chain compromises by leveraging the access gained from an initial supply chain compromise to further compromise a software component.(Citation: Krebs 3cx overview 2023) This may allow the threat actor to spread to even more victims.

## Sub-techniques
- T1195.001: Compromise Software Dependencies and Development Tools
- T1195.002: Compromise Software Supply Chain
- T1195.003: Compromise Hardware Supply Chain

## Mitigations
- M1013: Application Developer Guidance
- M1016: Vulnerability Scanning
- M1018: User Account Management
- M1033: Limit Software Installation
- M1046: Boot Integrity
- M1051: Update Software

## Known Threat Groups Using This Technique
- G1003: Ember Bear
- G0049: OilRig
- G0034: Sandworm Team

## Known Software Using This Technique
- S1213: Lumma Stealer
- S1148: Raccoon Stealer
