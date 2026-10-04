# T1542: Pre-OS Boot


**ATT&CK ID:** T1542  
**Domain:** Mitre Attack  
**Tactic(s):** Stealth, Persistence  
**Platforms:** Linux, macOS, Network Devices, Windows  
**Reference:** https://attack.mitre.org/techniques/T1542  

## Description
Adversaries may abuse Pre-OS Boot mechanisms as a way to establish persistence on a system. During the booting process of a computer, firmware and various startup services are loaded before the operating system. These programs control flow of execution before the operating system takes control.(Citation: Wikipedia Booting)

Adversaries may overwrite data in boot drivers or firmware such as BIOS (Basic Input/Output System) and The Unified Extensible Firmware Interface (UEFI) to persist on systems at a layer below the operating system. This can be particularly difficult to detect as malware at this level will not be detected by host software-based defenses.

## Sub-techniques
- T1542.001: System Firmware
- T1542.002: Component Firmware
- T1542.003: Bootkit
- T1542.004: ROMMONkit
- T1542.005: TFTP Boot

## Mitigations
- M1026: Privileged Account Management
- M1035: Limit Access to Resource Over Network
- M1046: Boot Integrity
- M1047: Audit
- M1051: Update Software
