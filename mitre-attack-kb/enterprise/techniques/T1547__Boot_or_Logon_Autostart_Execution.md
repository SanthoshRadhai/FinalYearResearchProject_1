# T1547: Boot or Logon Autostart Execution


**ATT&CK ID:** T1547  
**Domain:** Mitre Attack  
**Tactic(s):** Persistence, Privilege Escalation  
**Platforms:** Linux, macOS, Windows, Network Devices  
**Reference:** https://attack.mitre.org/techniques/T1547  

## Description
Adversaries may configure system settings to automatically execute a program during system boot or logon to maintain persistence or gain higher-level privileges on compromised systems. Operating systems may have mechanisms for automatically running a program on system boot or account logon.(Citation: Microsoft Run Key)(Citation: MSDN Authentication Packages)(Citation: Microsoft TimeProvider)(Citation: Cylance Reg Persistence Sept 2013)(Citation: Linux Kernel Programming) These mechanisms may include automatically executing programs that are placed in specially designated directories or are referenced by repositories that store configuration information, such as the Windows Registry. An adversary may achieve the same goal by modifying or extending features of the kernel.

Since some boot or logon autostart programs run with higher privileges, an adversary may leverage these to elevate privileges.

## Sub-techniques
- T1547.001: Registry Run Keys / Startup Folder
- T1547.002: Authentication Package
- T1547.003: Time Providers
- T1547.004: Winlogon Helper DLL
- T1547.005: Security Support Provider
- T1547.006: Kernel Modules and Extensions
- T1547.007: Re-opened Applications
- T1547.008: LSASS Driver
- T1547.009: Shortcut Modification
- T1547.010: Port Monitors
- T1547.012: Print Processors
- T1547.013: XDG Autostart Entries
- T1547.014: Active Setup
- T1547.015: Login Items

## Known Threat Groups Using This Technique
- G1044: APT42

## Known Software Using This Technique
- S0651: BoxCaon
- S0567: Dtrack
- S0084: Mis-Type
- S0083: Misdat
- S0653: xCaon
