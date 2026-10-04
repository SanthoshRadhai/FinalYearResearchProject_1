# T0817: Drive-by Compromise


**ATT&CK ID:** T0817  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Initial Access  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0817  

## Description
Adversaries may gain access to a system during a drive-by compromise, when a user visits a website as part of a regular browsing session. With this technique, the user's web browser is targeted and exploited simply by visiting the compromised website. 

The adversary may target a specific community, such as trusted third party suppliers or other industry specific groups, which often visit the target website. This kind of targeted attack relies on a common interest, and is known as a strategic web compromise or watering hole attack. 

The National Cyber Awareness System (NCAS) has issued a Technical Alert (TA) regarding Russian government cyber activity targeting critical infrastructure sectors. (Citation: Cybersecurity & Infrastructure Security Agency March 2018) Analysis by DHS and FBI has noted two distinct categories of victims in the Dragonfly campaign on the Western energy sector: staging and intended targets. The adversary targeted the less secure networks of staging targets, including trusted third-party suppliers and related peripheral organizations. Initial access to the intended targets used watering hole attacks to target process control, ICS, and critical infrastructure related trade publications and informational websites.

## Mitigations
- M0921: Restrict Web-Based Content
- M0948: Application Isolation and Sandboxing
- M0950: Exploit Protection
- M0951: Update Software

## Known Threat Groups Using This Technique
- G1000: ALLANITE
- G0035: Dragonfly
- G0049: OilRig
- G0088: TEMP.Veles

## Known Software Using This Technique
- S0606: Bad Rabbit
