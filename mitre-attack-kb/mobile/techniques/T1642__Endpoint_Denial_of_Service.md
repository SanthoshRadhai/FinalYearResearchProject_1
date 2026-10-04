# T1642: Endpoint Denial of Service


**ATT&CK ID:** T1642  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Impact  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1642  

## Description
Adversaries may perform Endpoint Denial of Service (DoS) attacks to degrade or block the availability of services to users.

On Android versions prior to 7, apps can abuse Device Administrator access to reset the device lock passcode, preventing the user from unlocking the device. After Android 7, only device or profile owners (e.g. MDMs) can reset the device’s passcode.(Citation: Android resetPassword)

On iOS devices, this technique does not work because mobile device management servers can only remove the screen lock passcode; they cannot set a new passcode. However, on jailbroken devices, malware has been discovered that can lock the user out of the device.(Citation: Xiao-KeyRaider)

## Mitigations
- M1006: Use Recent OS Version
- M1011: User Guidance

## Known Software Using This Technique
- S0323: Charger
- S0522: Exobot
- S0536: GPlayed
- S1185: LightSpy
- S0298: Xbot
