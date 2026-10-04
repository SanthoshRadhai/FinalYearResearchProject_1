# S0581: IronNetInjector

**Type:** tool  
**Reference:** https://attack.mitre.org/software/S0581  
**Aliases:** IronNetInjector  
**Platforms:** Windows  

## Description
[IronNetInjector](https://attack.mitre.org/software/S0581) is a [Turla](https://attack.mitre.org/groups/G0010) toolchain that utilizes scripts from the open-source IronPython implementation of Python with a .NET injector to drop one or more payloads including [ComRAT](https://attack.mitre.org/software/S0126).(Citation: Unit 42 IronNetInjector February 2021 )

## Techniques Used
- T1027.013: Encrypted/Encoded File
- T1036.004: Masquerade Task or Service
- T1053.005: Scheduled Task
- T1055: Process Injection
- T1055.001: Dynamic-link Library Injection
- T1057: Process Discovery
- T1059.006: Python
- T1140: Deobfuscate/Decode Files or Information
