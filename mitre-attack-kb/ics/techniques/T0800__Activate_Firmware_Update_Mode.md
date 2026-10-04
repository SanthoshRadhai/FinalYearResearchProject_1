# T0800: Activate Firmware Update Mode


**ATT&CK ID:** T0800  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Inhibit Response Function  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0800  

## Description
Adversaries may activate firmware update mode on devices to prevent expected response functions from engaging in reaction to an emergency or process malfunction. For example, devices such as protection relays may have an operation mode designed for firmware installation. This mode may halt process monitoring and related functions to allow new firmware to be loaded. A device left in update mode may be placed in an inactive holding state if no firmware is provided to it. By entering and leaving a device in this mode, the adversary may deny its usual functionalities.

## Mitigations
- M0800: Authorization Enforcement
- M0801: Access Management
- M0802: Communication Authenticity
- M0804: Human User Authentication
- M0807: Network Allowlists
- M0813: Software Process and Device Authentication
- M0930: Network Segmentation
- M0937: Filter Network Traffic

## Known Software Using This Technique
- S0604: Industroyer
