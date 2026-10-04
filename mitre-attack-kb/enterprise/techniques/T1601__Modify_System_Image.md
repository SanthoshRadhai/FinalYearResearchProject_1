# T1601: Modify System Image


**ATT&CK ID:** T1601  
**Domain:** Mitre Attack  
**Tactic(s):** Defense Impairment  
**Platforms:** Network Devices  
**Reference:** https://attack.mitre.org/techniques/T1601  

## Description
Adversaries may make changes to the operating system of embedded network devices to weaken defenses and provide new capabilities for themselves.  On such devices, the operating systems are typically monolithic and most of the device functionality and capabilities are contained within a single file.

To change the operating system, the adversary typically only needs to affect this one file, replacing or modifying it.  This can either be done live in memory during system runtime for immediate effect, or in storage to implement the change on the next boot of the network device.

## Sub-techniques
- T1601.001: Patch System Image
- T1601.002: Downgrade System Image

## Mitigations
- M1026: Privileged Account Management
- M1027: Password Policies
- M1032: Multi-factor Authentication
- M1043: Credential Access Protection
- M1045: Code Signing
- M1046: Boot Integrity

## Known Software Using This Technique
- S9013: DRYHOOK
