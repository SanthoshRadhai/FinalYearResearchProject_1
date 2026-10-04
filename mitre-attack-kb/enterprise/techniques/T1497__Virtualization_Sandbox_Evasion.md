# T1497: Virtualization/Sandbox Evasion


**ATT&CK ID:** T1497  
**Domain:** Mitre Attack  
**Tactic(s):** Stealth, Discovery  
**Platforms:** Linux, macOS, Windows  
**Reference:** https://attack.mitre.org/techniques/T1497  

## Description
Adversaries may employ various means to detect and avoid virtualization and analysis environments. This may include changing behaviors based on the results of checks for the presence of artifacts indicative of a virtual machine environment (VME) or sandbox. If the adversary detects a VME, they may alter their malware to disengage from the victim or conceal the core functions of the implant. They may also search for VME artifacts before dropping secondary or additional payloads. Adversaries may use the information learned from [Virtualization/Sandbox Evasion](https://attack.mitre.org/techniques/T1497) during automated discovery to shape follow-on behaviors.(Citation: Deloitte Environment Awareness)

Adversaries may use several methods to accomplish [Virtualization/Sandbox Evasion](https://attack.mitre.org/techniques/T1497) such as checking for security monitoring tools (e.g., Sysinternals, Wireshark, etc.) or other system artifacts associated with analysis or virtualization. Adversaries may also check for legitimate user activity to help determine if it is in an analysis environment. Additional methods include use of sleep timers or loops within malware code to avoid operating within a temporary sandbox.(Citation: Unit 42 Pirpi July 2015)

## Sub-techniques
- T1497.001: System Checks
- T1497.002: User Activity Based Checks
- T1497.003: Time Based Checks

## Known Threat Groups Using This Technique
- G1052: Contagious Interview
- G0012: Darkhotel
- G1031: Saint Bear

## Known Software Using This Technique
- S0331: Agent Tesla
- S0534: Bazar
- S0268: Bisonal
- S1070: Black Basta
- S1039: Bumblebee
- S0023: CHOPSTICK
- S0484: Carberp
- S0046: CozyCar
- S0554: Egregor
- S0666: Gelsemium
- S0499: Hancitor
- S0483: IcedID
- S1020: Kevin
- S0455: Metamorfo
- S9043: Mini Shai-Hulud
- S0147: Pteranodon
- S0148: RTM
- S1130: Raspberry Robin
- S1240: RedLine Stealer
- S1030: Squirrelwaffle
- S0380: StoneDrill
- S1183: StrelaStealer
- S1207: XLoader
