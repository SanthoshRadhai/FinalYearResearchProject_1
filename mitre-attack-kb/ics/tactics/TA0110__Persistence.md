# TA0110: Persistence

**Type:** Tactic  
**Reference:** https://attack.mitre.org/tactics/TA0110  

## Description
The adversary is trying to maintain their foothold in your ICS environment.

Persistence consists of techniques that adversaries use to maintain access to ICS systems and devices across restarts, changed credentials, and other interruptions that could cut off their access. Techniques used for persistence include any access, action, or configuration changes that allow them to secure their ongoing activity and keep their foothold on systems. This may include replacing or hijacking legitimate code, firmware, and other project files, or adding startup code and downloading programs onto devices.

## Techniques in This Tactic
- T0859: Valid Accounts
- T0873: Project File Infection
- T0873.001: Siemens Project File Format
- T0889: Modify Program
- T1693: Modify Firmware
- T1693.001: System Firmware
- T1693.002: Module Firmware
- T1694: Insecure Credentials
- T1694.001: Default Credentials
- T1694.002: Hardcoded Credentials
