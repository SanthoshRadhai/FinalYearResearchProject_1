# S1161: BPFDoor

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1161  
**Aliases:** BPFDoor, JustForFun, Backdoor.Linux.BPFDOOR, Backdoor.Solaris.BPFDOOR.ZAJE  
**Platforms:** Linux  

## Description
[BPFDoor](https://attack.mitre.org/software/S1161) is a Linux based passive long-term backdoor used by China-based threat actors. First seen in 2021, [BPFDoor](https://attack.mitre.org/software/S1161) is named after its usage of Berkley Packet Filter (BPF) to execute single task instructions. [BPFDoor](https://attack.mitre.org/software/S1161) supports multiple protocols for communicating with a C2 including TCP, UDP, and ICMP and can start local or reverse shells that bypass firewalls using iptables.(Citation: Sandfly BPFDoor 2022)(Citation: Deep Instinct BPFDoor 2023)

## Techniques Used
- T1027: Obfuscated Files or Information
- T1036.009: Break Process Trees
- T1036.011: Overwrite Process Arguments
- T1059.004: Unix Shell
- T1070: Indicator Removal
- T1070.004: File Deletion
- T1070.006: Timestomp
- T1205.002: Socket Filters
- T1480: Execution Guardrails
- T1480.002: Mutual Exclusion
- T1564.011: Ignore Process Interrupts
- T1686: Disable or Modify System Firewall
- T1690: Prevent Command History Logging
