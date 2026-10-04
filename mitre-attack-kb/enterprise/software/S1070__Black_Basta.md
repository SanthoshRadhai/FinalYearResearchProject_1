# S1070: Black Basta

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1070  
**Aliases:** Black Basta  
**Platforms:** Windows, ESXi  

## Description
[Black Basta](https://attack.mitre.org/software/S1070) is ransomware written in C++ that has been offered within the ransomware-as-a-service (RaaS) model since at least April 2022; there are variants that target Windows and VMWare ESXi servers. [Black Basta](https://attack.mitre.org/software/S1070) operations have included the double extortion technique where in addition to demanding ransom for decrypting the files of targeted organizations the cyber actors also threaten to post sensitive information to a leak site if the ransom is not paid. [Black Basta](https://attack.mitre.org/software/S1070) affiliates have targeted multiple high-value organizations, with the largest number of victims based in the U.S. Based on similarities in TTPs, leak sites, payment sites, and negotiation tactics, security researchers assess the [Black Basta](https://attack.mitre.org/software/S1070) RaaS operators could include current or former members of the [Conti](https://attack.mitre.org/software/S0575) group.(Citation: Palo Alto Networks Black Basta August 2022)(Citation: Deep Instinct Black Basta August 2022)(Citation: Minerva Labs Black Basta May 2022)(Citation: Avertium Black Basta June 2022)(Citation: NCC Group Black Basta June 2022)(Citation: Cyble Black Basta May 2022)

## Techniques Used
- T1007: System Service Discovery
- T1018: Remote System Discovery
- T1027.001: Binary Padding
- T1036.004: Masquerade Task or Service
- T1036.005: Match Legitimate Resource Name or Location
- T1047: Windows Management Instrumentation
- T1059.001: PowerShell
- T1059.003: Windows Command Shell
- T1082: System Information Discovery
- T1083: File and Directory Discovery
- T1106: Native API
- T1112: Modify Registry
- T1204.002: Malicious File
- T1222.002: Linux and Mac Permissions
- T1480.002: Mutual Exclusion
- T1486: Data Encrypted for Impact
- T1490: Inhibit System Recovery
- T1491.001: Internal Defacement
- T1497: Virtualization/Sandbox Evasion
- T1497.001: System Checks
- T1529: System Shutdown/Reboot
- T1543.003: Windows Service
- T1553.002: Code Signing
- T1622: Debugger Evasion
- T1680: Local Storage Discovery
- T1688: Safe Mode Boot
