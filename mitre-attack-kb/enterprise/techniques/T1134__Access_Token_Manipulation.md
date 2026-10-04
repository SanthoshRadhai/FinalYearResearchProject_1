# T1134: Access Token Manipulation


**ATT&CK ID:** T1134  
**Domain:** Mitre Attack  
**Tactic(s):** Stealth, Privilege Escalation  
**Platforms:** Windows  
**Reference:** https://attack.mitre.org/techniques/T1134  

## Description
Adversaries may modify access tokens to operate under a different user or system security context to perform actions and bypass access controls. Windows uses access tokens to determine the ownership of a running process. A user can manipulate access tokens to make a running process appear as though it is the child of a different process or belongs to someone other than the user that started the process. When this occurs, the process also takes on the security context associated with the new token.

An adversary can use built-in Windows API functions to copy access tokens from existing processes; this is known as token stealing. These token can then be applied to an existing process (i.e. [Token Impersonation/Theft](https://attack.mitre.org/techniques/T1134/001)) or used to spawn a new process (i.e. [Create Process with Token](https://attack.mitre.org/techniques/T1134/002)). An adversary must already be in a privileged user context (i.e. administrator) to steal a token. However, adversaries commonly use token stealing to elevate their security context from the administrator level to the SYSTEM level. An adversary can then use a token to authenticate to a remote system as the account for that token if the account has appropriate permissions on the remote system.(Citation: Pentestlab Token Manipulation)

Any standard user can use the <code>runas</code> command, and the Windows API functions, to create impersonation tokens; it does not require access to an administrator account. There are also other mechanisms, such as Active Directory fields, that can be used to modify access tokens.

## Sub-techniques
- T1134.001: Token Impersonation/Theft
- T1134.002: Create Process with Token
- T1134.003: Make and Impersonate Token
- T1134.004: Parent PID Spoofing
- T1134.005: SID-History Injection

## Mitigations
- M1018: User Account Management
- M1026: Privileged Account Management

## Known Threat Groups Using This Technique
- G0108: Blue Mockingbird
- G0037: FIN6
- G0030: Lotus Blossom

## Known Software Using This Technique
- S0622: AppleSeed
- S1068: BlackCat
- S0625: Cuba
- S0038: Duqu
- S0363: Empire
- S0666: Gelsemium
- S0697: HermeticWiper
- S0203: Hydraq
- S0607: KillDisk
- S1060: Mafalda
- S0576: MegaCortex
- S0378: PoshC2
- S0194: PowerSploit
- S1242: Qilin
- S0446: Ryuk
- S0562: SUNSPOT
- S1210: Sagerunex
- S0633: Sliver
- S0058: SslMM
