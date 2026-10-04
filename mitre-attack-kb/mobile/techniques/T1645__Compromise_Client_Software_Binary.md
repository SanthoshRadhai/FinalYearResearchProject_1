# T1645: Compromise Client Software Binary


**ATT&CK ID:** T1645  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Persistence  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1645  

## Description
Adversaries may modify system software binaries to establish persistent access to devices. System software binaries are used by the underlying operating system and users over adb or terminal emulators. 

Adversaries may make modifications to client software binaries to carry out malicious tasks when those binaries are executed. For example, malware may come with a pre-compiled malicious binary intended to overwrite the genuine one on the device. Since these binaries may be routinely executed by the system or user, the adversary can leverage this for persistent access to the device.

## Mitigations
- M1001: Security Updates
- M1002: Attestation
- M1003: Lock Bootloader
- M1004: System Partition Integrity

## Known Software Using This Technique
- S0293: BrainTest
- S0655: BusyGasper
- S0550: DoubleAgent
- S0407: Monokle
- S0316: Pegasus for Android
- S0289: Pegasus for iOS
- S0294: ShiftyBug
- S0324: SpyDealer
