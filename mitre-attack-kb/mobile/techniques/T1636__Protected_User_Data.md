# T1636: Protected User Data


**ATT&CK ID:** T1636  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Collection  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1636  

## Description
Adversaries may utilize standard operating system APIs to collect data from permission-backed data stores on a device, such as the calendar or contact list. These permissions need to be declared ahead of time. On Android, they must be included in the application’s manifest. On iOS, they must be included in the application’s `Info.plist` file.  

 

In almost all cases, the user is required to grant access to the data store that the application is trying to access. In recent OS versions, vendors have introduced additional privacy controls for users, such as the ability to grant permission to an application only while the application is being actively used by the user. 

 

If the device has been jailbroken or rooted, an adversary may be able to access [Protected User Data](https://attack.mitre.org/techniques/T1636) without the user’s knowledge or approval.

## Sub-techniques
- T1636.001: Calendar Entries
- T1636.002: Call Log
- T1636.003: Contact List
- T1636.004: SMS Messages
- T1636.005: Accounts

## Mitigations
- M1006: Use Recent OS Version
- M1011: User Guidance
