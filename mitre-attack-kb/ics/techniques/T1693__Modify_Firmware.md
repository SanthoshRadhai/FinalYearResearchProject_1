# T1693: Modify Firmware


**ATT&CK ID:** T1693  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Persistence, Inhibit Response Function, Impair Process Control  
**Reference:** https://attack.mitre.org/techniques/T1693  

## Description
Firmware is low-level software embedded in hardware that enables systems and devices to function properly and is commonly found in ICS environments. Adversaries may modify firmware on a system or device by installing malicious or vulnerable versions that enable them to achieve objectives such as [Persistence](https://attack.mitre.org/tactics/TA0110), [Impair Process Control](https://attack.mitre.org/tactics/TA0106), and [Inhibit Response Function](https://attack.mitre.org/tactics/TA0107). 

Adversaries may modify system and device firmware by using the built-in firmware update functionality which may support local or remote installation. The malicious or vulnerable firmware may be delivered via [Replication Through Removable Media](https://attack.mitre.org/techniques/T0847), [Supply Chain Compromise](https://attack.mitre.org/techniques/T0862), or [Remote Services](https://attack.mitre.org/techniques/T0886). Once installed, the malicious or vulnerable firmware could be used to provide [Rootkit](https://attack.mitre.org/techniques/T0851) and [Hooking](https://attack.mitre.org/techniques/T0874) functionality, [Exploitation for Privilege Escalation](https://attack.mitre.org/techniques/T0890), or [Denial of Service](https://attack.mitre.org/techniques/T0814).(Citation: Basnight, Zachry, et al.)

## Sub-techniques
- T1693.001: System Firmware
- T1693.002: Module Firmware

## Mitigations
- M0801: Access Management
- M0802: Communication Authenticity
- M0804: Human User Authentication
- M0807: Network Allowlists
- M0808: Encrypt Network Traffic
- M0813: Software Process and Device Authentication
- M0930: Network Segmentation
- M0937: Filter Network Traffic
- M0941: Encrypt Sensitive Information
- M0945: Code Signing
- M0946: Boot Integrity
- M0947: Audit
