# T1216: System Script Proxy Execution


**ATT&CK ID:** T1216  
**Domain:** Mitre Attack  
**Tactic(s):** Stealth  
**Platforms:** Windows  
**Reference:** https://attack.mitre.org/techniques/T1216  

## Description
Adversaries may use trusted scripts, often signed with certificates, to proxy the execution of malicious files. Several Microsoft signed scripts that have been downloaded from Microsoft or are default on Windows installations can be used to proxy execution of other files.(Citation: LOLBAS Project) This behavior may be abused by adversaries to execute malicious files that could bypass application control and signature validation on systems.(Citation: GitHub Ultimate AppLocker Bypass List)

## Sub-techniques
- T1216.001: PubPrn
- T1216.002: SyncAppvPublishingServer

## Mitigations
- M1038: Execution Prevention
