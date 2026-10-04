# T1037: Boot or Logon Initialization Scripts


**ATT&CK ID:** T1037  
**Domain:** Mitre Attack  
**Tactic(s):** Persistence, Privilege Escalation  
**Platforms:** ESXi, Linux, macOS, Network Devices, Windows  
**Reference:** https://attack.mitre.org/techniques/T1037  

## Description
Adversaries may use scripts automatically executed at boot or logon initialization to establish persistence.(Citation: Mandiant APT29 Eye Spy Email Nov 22)(Citation: Anomali Rocke March 2019) Initialization scripts can be used to perform administrative functions, which may often execute other programs or send information to an internal logging server. These scripts can vary based on operating system and whether applied locally or remotely.  

Adversaries may use these scripts to maintain persistence on a single system. Depending on the access configuration of the logon scripts, either local credentials or an administrator account may be necessary. 

An adversary may also be able to escalate their privileges since some boot or logon initialization scripts run with higher privileges.

## Sub-techniques
- T1037.001: Logon Script (Windows)
- T1037.002: Login Hook
- T1037.003: Network Logon Script
- T1037.004: RC Scripts
- T1037.005: Startup Items

## Mitigations
- M1022: Restrict File and Directory Permissions
- M1024: Restrict Registry Permissions

## Known Threat Groups Using This Technique
- G0016: APT29
- G0096: APT41
- G0106: Rocke
- G1048: UNC3886

## Known Software Using This Technique
- S1078: RotaJakiro
- S9024: SPAWNCHIMERA
- S1217: VIRTUALPITA
