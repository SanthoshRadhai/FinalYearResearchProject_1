# T0863: User Execution


**ATT&CK ID:** T0863  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Execution  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0863  

## Description
Adversaries may rely on a targeted organizations user interaction for the execution of malicious code. User interaction may consist of installing applications, opening email attachments, or granting higher permissions to documents. 

Adversaries may embed malicious code or visual basic code into files such as Microsoft Word and Excel documents or software installers. (Citation: Booz Allen Hamilton) Execution of this code requires that the user enable scripting or write access within the document. Embedded code may not always be noticeable to the user especially in cases of trojanized software. (Citation: Daavid Hentunen, Antti Tikkanen June 2014) 

A Chinese spearphishing campaign running from December 9, 2011 through February 29, 2012 delivered malware through spearphishing attachments which required user action to achieve execution. (Citation: CISA AA21-201A Pipeline Intrusion July 2021)

## Mitigations
- M0917: User Training
- M0921: Restrict Web-Based Content
- M0931: Network Intrusion Prevention
- M0938: Execution Prevention
- M0945: Code Signing
- M0949: Antivirus/Antimalware

## Known Software Using This Technique
- S0093: Backdoor.Oldrea
- S0606: Bad Rabbit
- S0496: REvil
- S0603: Stuxnet
