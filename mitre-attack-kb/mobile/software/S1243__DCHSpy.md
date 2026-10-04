# S1243: DCHSpy

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1243  
**Aliases:** DCHSpy  
**Platforms:** Android  

## Description
[DCHSpy](https://attack.mitre.org/software/S1243) is an Android spyware likely used by [MuddyWater](https://attack.mitre.org/groups/G0069). [DCHSpy](https://attack.mitre.org/software/S1243) uses political decoys and masquerades as legitimate applications, such as VPNs and banking applications, to trick victims into downloading the malware. Once downloaded, [DCHSpy](https://attack.mitre.org/software/S1243) collects information from the device and exfiltrates the data to the command and control (C2) server.(Citation: Lookout_DCHSpy_July2025)

## Techniques Used
- T1409: Stored Application Data
- T1429: Audio Capture
- T1430: Location Tracking
- T1437: Application Layer Protocol
- T1512: Video Capture
- T1532: Archive Collected Data
- T1533: Data from Local System
- T1636.002: Call Log
- T1636.003: Contact List
- T1636.004: SMS Messages
- T1636.005: Accounts
- T1655.001: Match Legitimate Name or Location
