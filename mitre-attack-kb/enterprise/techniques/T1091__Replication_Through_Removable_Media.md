# T1091: Replication Through Removable Media


**ATT&CK ID:** T1091  
**Domain:** Mitre Attack  
**Tactic(s):** Lateral Movement, Initial Access  
**Platforms:** Windows  
**Reference:** https://attack.mitre.org/techniques/T1091  

## Description
Adversaries may move onto systems, possibly those on disconnected or air-gapped networks, by copying malware to removable media and taking advantage of Autorun features when the media is inserted into a system and executes. In the case of Lateral Movement, this may occur through modification of executable files stored on removable media or by copying malware and renaming it to look like a legitimate file to trick users into executing it on a separate system. In the case of Initial Access, this may occur through manual manipulation of the media, modification of systems used to initially format the media, or modification to the media's firmware itself.

Mobile devices may also be used to infect PCs with malware if connected via USB.(Citation: Exploiting Smartphone USB ) This infection may be achieved using devices (Android, iOS, etc.) and, in some instances, USB charging cables.(Citation: Windows Malware Infecting Android)(Citation: iPhone Charging Cable Hack) For example, when a smartphone is connected to a system, it may appear to be mounted similar to a USB-connected disk drive. If malware that is compatible with the connected system is on the mobile device, the malware could infect the machine (especially if Autorun features are enabled).

## Mitigations
- M1034: Limit Hardware Installation
- M1040: Behavior Prevention on Endpoint
- M1042: Disable or Remove Feature or Program

## Known Threat Groups Using This Technique
- G0007: APT28
- G1007: Aoqin Dragon
- G0012: Darkhotel
- G0046: FIN7
- G0047: Gamaredon Group
- G1014: LuminousMoth
- G0129: Mustang Panda
- G0081: Tropic Trooper

## Known Software Using This Technique
- S1074: ANDROMEDA
- S0092: Agent.btz
- S0023: CHOPSTICK
- S0608: Conficker
- S0115: Crimson
- S0062: DustySky
- S0143: Flame
- S0132: H1N1
- S1230: HIUPAN
- S0013: PlugX
- S0650: QakBot
- S0458: Ramsay
- S1130: Raspberry Robin
- S0028: SHIPSHAPE
- S0603: Stuxnet
- S0136: USBStealer
- S0452: USBferry
- S0130: Unknown Logger
- S0386: Ursnif
- S0385: njRAT
