# S1156: Manjusaka

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1156  
**Aliases:** Manjusaka  
**Platforms:** Linux, Windows  

## Description
[Manjusaka](https://attack.mitre.org/software/S1156) is a Chinese-language intrusion framework, similar to [Sliver](https://attack.mitre.org/software/S0633) and [Cobalt Strike](https://attack.mitre.org/software/S0154), with an ELF binary written in GoLang as the controller for Windows and Linux implants written in Rust. First identified in 2022, [Manjusaka](https://attack.mitre.org/software/S1156) consists of multiple components, only one of which (a command and control module) is freely available.(Citation: Talos Manjusaka 2022)

## Techniques Used
- T1016: System Network Configuration Discovery
- T1041: Exfiltration Over C2 Channel
- T1059.003: Windows Command Shell
- T1071.001: Web Protocols
- T1082: System Information Discovery
- T1083: File and Directory Discovery
- T1113: Screen Capture
- T1132.001: Standard Encoding
- T1555: Credentials from Password Stores
- T1555.003: Credentials from Web Browsers
