# S0540: Asacub

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0540  
**Aliases:** Asacub, Trojan-SMS.AndroidOS.Smaps  
**Platforms:** Android  

## Description
[Asacub](https://attack.mitre.org/software/S0540) is a banking trojan that attempts to steal money from victims’ bank accounts. It attempts to do this by initiating a wire transfer via SMS message from compromised devices.(Citation: Securelist Asacub)

## Techniques Used
- T1406: Obfuscated Files or Information
- T1422: System Network Configuration Discovery
- T1422.001: Internet Connection Discovery
- T1426: System Information Discovery
- T1437.001: Web Protocols
- T1532: Archive Collected Data
- T1575: Native API
- T1582: SMS Control
- T1626.001: Device Administrator Permissions
- T1636.003: Contact List
- T1636.004: SMS Messages
- T1655.001: Match Legitimate Name or Location
