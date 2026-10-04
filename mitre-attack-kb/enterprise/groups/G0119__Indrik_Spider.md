# G0119: Indrik Spider

**Type:** intrusion-set  
**Reference:** https://attack.mitre.org/groups/G0119  
**Aliases:** Indrik Spider, Evil Corp, Manatee Tempest, DEV-0243, UNC2165  

## Description
[Indrik Spider](https://attack.mitre.org/groups/G0119) is a Russia-based cybercriminal group that has been active since at least 2014. [Indrik Spider](https://attack.mitre.org/groups/G0119) initially started with the [Dridex](https://attack.mitre.org/software/S0384) banking Trojan, and then by 2017 they began running ransomware operations using [BitPaymer](https://attack.mitre.org/software/S0570), [WastedLocker](https://attack.mitre.org/software/S0612), and Hades ransomware. Following U.S. sanctions and an indictment in 2019, [Indrik Spider](https://attack.mitre.org/groups/G0119) changed their tactics and diversified their toolset.(Citation: Crowdstrike Indrik November 2018)(Citation: Crowdstrike EvilCorp March 2021)(Citation: Treasury EvilCorp Dec 2019)

## Techniques Used
- T1003.001: LSASS Memory
- T1007: System Service Discovery
- T1012: Query Registry
- T1018: Remote System Discovery
- T1021.001: Remote Desktop Protocol
- T1021.004: SSH
- T1036.005: Match Legitimate Resource Name or Location
- T1047: Windows Management Instrumentation
- T1059.001: PowerShell
- T1059.003: Windows Command Shell
- T1059.007: JavaScript
- T1074.001: Local Data Staging
- T1078: Valid Accounts
- T1078.002: Domain Accounts
- T1105: Ingress Tool Transfer
- T1112: Modify Registry
- T1136: Create Account
- T1136.001: Local Account
- T1204.002: Malicious File
- T1484.001: Group Policy Modification
- T1486: Data Encrypted for Impact
- T1489: Service Stop
- T1552.001: Credentials In Files
- T1555.005: Password Managers
- T1558.003: Kerberoasting
- T1567.002: Exfiltration to Cloud Storage
- T1583: Acquire Infrastructure
- T1584.004: Server
- T1585.002: Email Accounts
- T1587.001: Malware
- T1590: Gather Victim Network Information
- T1685: Disable or Modify Tools
- T1685.005: Clear Windows Event Logs
