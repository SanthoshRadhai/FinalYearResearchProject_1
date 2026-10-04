# S1129: Akira

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1129  
**Aliases:** Akira  
**Platforms:** Windows  

## Description
[Akira](https://attack.mitre.org/software/S1129) ransomware, written in C++, is most prominently (but not exclusively) associated with the ransomware-as-a-service entity [Akira](https://attack.mitre.org/groups/G1024). [Akira](https://attack.mitre.org/software/S1129) ransomware has been used in attacks across North America, Europe, and Australia, with a focus on critical infrastructure sectors including manufacturing, education, and IT services. [Akira](https://attack.mitre.org/software/S1129) ransomware employs hybrid encryption and threading to increase the speed and efficiency of encryption and runtime arguments for tailored attacks. Notable variants include Rust-based [Megazord](https://attack.mitre.org/software/S1191) for targeting Windows and [Akira _v2](https://attack.mitre.org/software/S1194) for targeting VMware ESXi servers.(Citation: Kersten Akira 2023)(Citation: CISA Akira Ransomware APR 2024)(Citation: Cisco Akira Ransomware OCT 2024)

## Techniques Used
- T1047: Windows Management Instrumentation
- T1057: Process Discovery
- T1059.001: PowerShell
- T1059.003: Windows Command Shell
- T1082: System Information Discovery
- T1083: File and Directory Discovery
- T1106: Native API
- T1135: Network Share Discovery
- T1486: Data Encrypted for Impact
- T1490: Inhibit System Recovery
