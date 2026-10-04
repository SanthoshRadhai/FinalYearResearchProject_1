# S0695: Donut

**Type:** tool  
**Reference:** https://attack.mitre.org/software/S0695  
**Aliases:** Donut  
**Platforms:** Windows  

## Description
[Donut](https://attack.mitre.org/software/S0695) is an open source framework used to generate position-independent shellcode.(Citation: Donut Github)(Citation: Introducing Donut) [Donut](https://attack.mitre.org/software/S0695) generated code has been used by multiple threat actors to inject and load malicious payloads into memory.(Citation: NCC Group WastedLocker June 2020)

## Techniques Used
- T1027.002: Software Packing
- T1027.013: Encrypted/Encoded File
- T1027.015: Compression
- T1055: Process Injection
- T1057: Process Discovery
- T1059: Command and Scripting Interpreter
- T1059.001: PowerShell
- T1059.005: Visual Basic
- T1059.006: Python
- T1059.007: JavaScript
- T1070: Indicator Removal
- T1071.001: Web Protocols
- T1105: Ingress Tool Transfer
- T1106: Native API
- T1620: Reflective Code Loading
- T1685: Disable or Modify Tools
