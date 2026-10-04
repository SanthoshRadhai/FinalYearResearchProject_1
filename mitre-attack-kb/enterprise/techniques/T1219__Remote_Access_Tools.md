# T1219: Remote Access Tools


**ATT&CK ID:** T1219  
**Domain:** Mitre Attack  
**Tactic(s):** Command And Control  
**Platforms:** Linux, macOS, Windows  
**Reference:** https://attack.mitre.org/techniques/T1219  

## Description
An adversary may use legitimate remote access tools to establish an interactive command and control channel within a network. Remote access tools create a session between two trusted hosts through a graphical interface, a command line interaction, a protocol tunnel via development or management software, or hardware-level access such as KVM (Keyboard, Video, Mouse) over IP solutions. Desktop support software (usually graphical interface) and remote management software (typically command line interface) allow a user to control a computer remotely as if they are a local user inheriting the user or software permissions. This software is commonly used for troubleshooting, software installation, and system management.(Citation: Symantec Living off the Land)(Citation: CrowdStrike 2015 Global Threat Report)(Citation: CrySyS Blog TeamSpy) Adversaries may similarly abuse response features included in EDR and other defensive tools that enable remote access.

Remote access tools may be installed and used post-compromise as an alternate communications channel for redundant access or to establish an interactive remote desktop session with the target system. It may also be used as a malware component to establish a reverse connection or back-connect to a service or adversary-controlled system.

Installation of many remote access tools may also include persistence (e.g., the software's installation routine creates a [Windows Service](https://attack.mitre.org/techniques/T1543/003)). Remote access modules/features may also exist as part of otherwise existing software (e.g., Google Chrome’s Remote Desktop).(Citation: Google Chrome Remote Desktop)(Citation: Chrome Remote Desktop)

## Sub-techniques
- T1219.001: IDE Tunneling
- T1219.002: Remote Desktop Software
- T1219.003: Remote Access Hardware

## Mitigations
- M1031: Network Intrusion Prevention
- M1034: Limit Hardware Installation
- M1037: Filter Network Traffic
- M1038: Execution Prevention
- M1042: Disable or Remove Feature or Program

## Known Threat Groups Using This Technique
- G1024: Akira
- G1043: BlackByte
- G0008: Carbanak
- G0080: Cobalt Group
- G0105: DarkVishnya
- G0046: FIN7
- G0115: GOLD SOUTHFIELD
- G1032: INC Ransom
- G1051: Medusa Group
- G0049: OilRig
- G0034: Sandworm Team
- G1057: ShinyHunters
- G0139: TeamTNT

## Known Software Using This Technique
- S0030: Carbanak
- S0384: Dridex
- S0554: Egregor
- S0601: Hildegard
- S1245: InvisibleFerret
- S0148: RTM
- S0266: TrickBot
