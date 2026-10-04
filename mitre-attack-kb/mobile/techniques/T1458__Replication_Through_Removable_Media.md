# T1458: Replication Through Removable Media


**ATT&CK ID:** T1458  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Initial Access, Lateral Movement  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1458  

## Description
Adversaries may move onto devices by exploiting or copying malware to devices connected via USB. In the case of Lateral Movement, adversaries may utilize the physical connection of a device to a compromised or malicious charging station or PC to bypass application store requirements and install malicious applications directly.(Citation: Lau-Mactans) In the case of Initial Access, adversaries may attempt to exploit the device via the connection to gain access to data stored on the device.(Citation: Krebs-JuiceJacking) Examples of this include: 
 
* Exploiting insecure bootloaders in a Nexus 6 or 6P device over USB and gaining the ability to perform actions including intercepting phone calls, intercepting network traffic, and obtaining the device physical location.(Citation: IBM-NexusUSB) 
* Exploiting weakly-enforced security boundaries in Android devices such as the Google Pixel 2 over USB.(Citation: GoogleProjectZero-OATmeal) 
* Products from Cellebrite and Grayshift purportedly that can exploit some iOS devices using physical access to the data port to unlock the passcode.(Citation: Computerworld-iPhoneCracking)

## Mitigations
- M1001: Security Updates
- M1003: Lock Bootloader
- M1006: Use Recent OS Version
- M1011: User Guidance
- M1012: Enterprise Policy

## Known Software Using This Technique
- S0315: DualToy
- S0312: WireLurker
