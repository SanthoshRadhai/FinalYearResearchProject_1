# T1021: Remote Services


**ATT&CK ID:** T1021  
**Domain:** Mitre Attack  
**Tactic(s):** Lateral Movement  
**Platforms:** Linux, macOS, Windows, IaaS, ESXi  
**Reference:** https://attack.mitre.org/techniques/T1021  

## Description
Adversaries may use [Valid Accounts](https://attack.mitre.org/techniques/T1078) to log into a service that accepts remote connections, such as telnet, SSH, and VNC. The adversary may then perform actions as the logged-on user.

In an enterprise environment, servers and workstations can be organized into domains. Domains provide centralized identity management, allowing users to login using one set of credentials across the entire network. If an adversary is able to obtain a set of valid domain credentials, they could login to many different machines using remote access protocols such as secure shell (SSH) or remote desktop protocol (RDP).(Citation: SSH Secure Shell)(Citation: TechNet Remote Desktop Services) They could also login to accessible SaaS or IaaS services, such as those that federate their identities to the domain, or management platforms for internal virtualization environments such as VMware vCenter. 

Legitimate applications (such as [Software Deployment Tools](https://attack.mitre.org/techniques/T1072) and other administrative programs) may utilize [Remote Services](https://attack.mitre.org/techniques/T1021) to access remote hosts. For example, Apple Remote Desktop (ARD) on macOS is native software used for remote management. ARD leverages a blend of protocols, including [VNC](https://attack.mitre.org/techniques/T1021/005) to send the screen and control buffers and [SSH](https://attack.mitre.org/techniques/T1021/004) for secure file transfer.(Citation: Remote Management MDM macOS)(Citation: Kickstart Apple Remote Desktop commands)(Citation: Apple Remote Desktop Admin Guide 3.3) Adversaries can abuse applications such as ARD to gain remote code execution and perform lateral movement. In versions of macOS prior to 10.14, an adversary can escalate an SSH session to an ARD session which enables an adversary to accept TCC (Transparency, Consent, and Control) prompts without user interaction and gain access to data.(Citation: FireEye 2019 Apple Remote Desktop)(Citation: Lockboxx ARD 2019)(Citation: Kickstart Apple Remote Desktop commands)

## Sub-techniques
- T1021.001: Remote Desktop Protocol
- T1021.002: SMB/Windows Admin Shares
- T1021.003: Distributed Component Object Model
- T1021.004: SSH
- T1021.005: VNC
- T1021.006: Windows Remote Management
- T1021.007: Cloud Services
- T1021.008: Direct Cloud VM Connections

## Mitigations
- M1018: User Account Management
- M1027: Password Policies
- M1032: Multi-factor Authentication
- M1035: Limit Access to Resource Over Network
- M1042: Disable or Remove Feature or Program
- M1047: Audit

## Known Threat Groups Using This Technique
- G0143: Aquatic Panda
- G1003: Ember Bear
- G0102: Wizard Spider

## Known Software Using This Technique
- S1063: Brute Ratel C4
- S0437: Kivars
- S1016: MacMa
- S0603: Stuxnet
