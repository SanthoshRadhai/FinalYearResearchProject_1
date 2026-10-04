# T1546: Event Triggered Execution


**ATT&CK ID:** T1546  
**Domain:** Mitre Attack  
**Tactic(s):** Privilege Escalation, Persistence  
**Platforms:** Linux, macOS, Windows, SaaS, IaaS, Office Suite  
**Reference:** https://attack.mitre.org/techniques/T1546  

## Description
Adversaries may establish persistence and/or elevate privileges using system mechanisms that trigger execution based on specific events. Various operating systems have means to monitor and subscribe to events such as logons or other user activity such as running specific applications/binaries. Cloud environments may also support various functions and services that monitor and can be invoked in response to specific cloud events.(Citation: Backdooring an AWS account)(Citation: Varonis Power Automate Data Exfiltration)(Citation: Microsoft DART Case Report 001)

Adversaries may abuse these mechanisms as a means of maintaining persistent access to a victim via repeatedly executing malicious code. After gaining access to a victim system, adversaries may create/modify event triggers to point to malicious content that will be executed whenever the event trigger is invoked.(Citation: FireEye WMI 2015)(Citation: Malware Persistence on OS X)(Citation: amnesia malware)

Since the execution can be proxied by an account with higher permissions, such as SYSTEM or service accounts, an adversary may be able to abuse these triggered execution mechanisms to escalate their privileges.

## Sub-techniques
- T1546.001: Change Default File Association
- T1546.002: Screensaver
- T1546.003: Windows Management Instrumentation Event Subscription
- T1546.004: Unix Shell Configuration Modification
- T1546.005: Trap
- T1546.006: LC_LOAD_DYLIB Addition
- T1546.007: Netsh Helper DLL
- T1546.008: Accessibility Features
- T1546.009: AppCert DLLs
- T1546.010: AppInit DLLs
- T1546.011: Application Shimming
- T1546.012: Image File Execution Options Injection
- T1546.013: PowerShell Profile
- T1546.014: Emond
- T1546.015: Component Object Model Hijacking
- T1546.016: Installer Packages
- T1546.017: Udev Rules
- T1546.018: Python Startup Hooks

## Mitigations
- M1026: Privileged Account Management
- M1051: Update Software

## Known Software Using This Technique
- S9043: Mini Shai-Hulud
- S1091: Pacu
- S1164: UPSTYLE
- S0658: XCSSET
