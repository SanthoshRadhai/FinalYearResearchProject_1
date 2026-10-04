# S0349: LaZagne

**Type:** tool  
**Reference:** https://attack.mitre.org/software/S0349  
**Aliases:** LaZagne  
**Platforms:** Linux, macOS, Windows  

## Description
[LaZagne](https://attack.mitre.org/software/S0349) is a post-exploitation, open-source tool used to recover stored passwords on a system. It has modules for Windows, Linux, and OSX, but is mainly focused on Windows systems. [LaZagne](https://attack.mitre.org/software/S0349) is publicly available on GitHub.(Citation: GitHub LaZagne Dec 2018)

## Techniques Used
- T1003.001: LSASS Memory
- T1003.004: LSA Secrets
- T1003.005: Cached Domain Credentials
- T1003.007: Proc Filesystem
- T1003.008: /etc/passwd and /etc/shadow
- T1552.001: Credentials In Files
- T1555: Credentials from Password Stores
- T1555.001: Keychain
- T1555.003: Credentials from Web Browsers
- T1555.004: Windows Credential Manager
