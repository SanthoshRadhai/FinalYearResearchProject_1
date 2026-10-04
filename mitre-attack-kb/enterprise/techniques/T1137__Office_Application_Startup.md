# T1137: Office Application Startup


**ATT&CK ID:** T1137  
**Domain:** Mitre Attack  
**Tactic(s):** Persistence  
**Platforms:** Windows, Office Suite  
**Reference:** https://attack.mitre.org/techniques/T1137  

## Description
Adversaries may leverage Microsoft Office-based applications for persistence between startups. Microsoft Office is a fairly common application suite on Windows-based operating systems within an enterprise network. There are multiple mechanisms that can be used with Office for persistence when an Office-based application is started; this can include the use of Office Template Macros and add-ins.

A variety of features have been discovered in Outlook that can be abused to obtain persistence, such as Outlook rules, forms, and Home Page.(Citation: SensePost Ruler GitHub) These persistence mechanisms can work within Outlook or be used through Office 365.(Citation: TechNet O365 Outlook Rules)

## Sub-techniques
- T1137.001: Office Template Macros
- T1137.002: Office Test
- T1137.003: Outlook Forms
- T1137.004: Outlook Home Page
- T1137.005: Outlook Rules
- T1137.006: Add-ins

## Mitigations
- M1040: Behavior Prevention on Endpoint
- M1042: Disable or Remove Feature or Program
- M1051: Update Software
- M1054: Software Configuration

## Known Threat Groups Using This Technique
- G0050: APT32
- G0047: Gamaredon Group
