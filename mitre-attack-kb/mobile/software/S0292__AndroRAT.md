# S0292: AndroRAT

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0292  
**Aliases:** AndroRAT  
**Platforms:** Android  

## Description
[AndroRAT](https://attack.mitre.org/software/S0292) is an open-source remote access tool for Android devices. [AndroRAT](https://attack.mitre.org/software/S0292) is capable of collecting data, such as device location, call logs, etc., and is capable of executing actions, such as sending SMS messages and taking pictures.(Citation: Lookout-EnterpriseApps)(Citation: github_androrat)(Citation: Forcepoint BITTER Pakistan Oct 2016) It is originally available through the `The404Hacking` Github repository.(Citation: github_androrat)

## Techniques Used
- T1422: System Network Configuration Discovery
- T1429: Audio Capture
- T1430: Location Tracking
- T1512: Video Capture
- T1582: SMS Control
- T1616: Call Control
- T1636.002: Call Log
- T1636.003: Contact List
- T1636.004: SMS Messages
- T1655.001: Match Legitimate Name or Location
