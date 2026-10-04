# T0865: Spearphishing Attachment


**ATT&CK ID:** T0865  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Initial Access  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0865  

## Description
Adversaries may use a spearphishing attachment, a variant of spearphishing, as a form of a social engineering attack against specific targets. Spearphishing attachments are different from other forms of spearphishing in that they employ malware attached to an email. All forms of spearphishing are electronically delivered and target a specific individual, company, or industry. In this scenario, adversaries attach a file to the spearphishing email and usually rely upon [User Execution](https://attack.mitre.org/techniques/T0863) to gain execution and access. (Citation: Enterprise ATT&CK October 2019) 

A Chinese spearphishing campaign running from December 9, 2011 through February 29, 2012, targeted ONG organizations and their employees. The emails were constructed with a high level of sophistication to convince employees to open the malicious file attachments. (Citation: CISA AA21-201A Pipeline Intrusion July 2021)

## Mitigations
- M0917: User Training
- M0921: Restrict Web-Based Content
- M0931: Network Intrusion Prevention
- M0949: Antivirus/Antimalware

## Known Threat Groups Using This Technique
- G1000: ALLANITE
- G0064: APT33
- G0032: Lazarus Group
- G0049: OilRig

## Known Software Using This Technique
- S0093: Backdoor.Oldrea
- S0089: BlackEnergy
