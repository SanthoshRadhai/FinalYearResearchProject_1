# T1663: Remote Access Software


**ATT&CK ID:** T1663  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Command And Control  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1663  

## Description
Adversaries may use legitimate remote access software, such as `VNC`, `TeamViewer`, `AirDroid`, `AirMirror`, etc., to establish an interactive command and control channel to target mobile devices.  

Remote access applications may be installed and used post-compromise as an alternate communication channel for redundant access or as a way to establish an interactive remote session with the target device. They may also be used as a component of malware to establish a reverse connection to an adversary-controlled system or service. Installation of remote access tools may also include persistence.

## Mitigations
- M1011: User Guidance
- M1012: Enterprise Policy

## Known Software Using This Technique
- S1094: BRATA
- S1092: Escobar
