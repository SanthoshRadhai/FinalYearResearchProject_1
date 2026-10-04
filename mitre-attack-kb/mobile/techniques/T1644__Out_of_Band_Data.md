# T1644: Out of Band Data


**ATT&CK ID:** T1644  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Command And Control  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1644  

## Description
Adversaries may communicate with compromised devices using out of band data streams. This could be done for a variety of reasons, including evading network traffic monitoring, as a backup method of command and control, or for data exfiltration if the device is not connected to any Internet-providing networks (i.e. cellular or Wi-Fi). Several out of band data streams exist, such as SMS messages, NFC, and Bluetooth. 

 

On Android, applications can read push notifications to capture content from SMS messages, or other out of band data streams. This requires that the user manually grant notification access to the application via the settings menu. However, the application could launch an Intent to take the user directly there. 

 

On iOS, there is no way to programmatically read push notifications.

## Mitigations
- M1011: User Guidance

## Known Software Using This Technique
- S0304: Android/Chuli.A
- S1079: BOULDSPY
- S0655: BusyGasper
- S0529: CarbonSteal
- S0505: Desert Scorpion
- S0406: Gustuff
- S0407: Monokle
- S0316: Pegasus for Android
- S0289: Pegasus for iOS
- S0295: RCSAndroid
- S0411: Rotexy
- S1055: SharkBot
- S0327: Skygofree
- S1195: SpyC23
- S0324: SpyDealer
- S0328: Stealth Mango
- S1216: TriangleDB
- S0427: TrickMo
