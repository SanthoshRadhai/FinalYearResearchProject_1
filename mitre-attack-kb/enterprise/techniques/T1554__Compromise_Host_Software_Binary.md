# T1554: Compromise Host Software Binary


**ATT&CK ID:** T1554  
**Domain:** Mitre Attack  
**Tactic(s):** Persistence  
**Platforms:** ESXi, Linux, macOS, Windows  
**Reference:** https://attack.mitre.org/techniques/T1554  

## Description
Adversaries may modify host software binaries to establish persistent access to systems. Software binaries/executables provide a wide range of system commands or services, programs, and libraries. Common software binaries are SSH clients, FTP clients, email clients, web browsers, and many other user or server applications.

Adversaries may establish persistence though modifications to host software binaries. For example, an adversary may replace or otherwise infect a legitimate application binary (or support files) with a backdoor. Since these binaries may be routinely executed by applications or the user, the adversary can leverage this for persistent access to the host. An adversary may also modify a software binary such as an SSH client in order to persistently collect credentials during logins (i.e., [Modify Authentication Process](https://attack.mitre.org/techniques/T1556)).(Citation: Google Cloud Mandiant UNC3886 2024)

An adversary may also modify an existing binary by patching in malicious functionality (e.g., IAT Hooking/Entry point patching)(Citation: Unit42 Banking Trojans Hooking 2022) prior to the binary’s legitimate execution. For example, an adversary may modify the entry point of a binary to point to malicious code patched in by the adversary before resuming normal execution flow.(Citation: ESET FontOnLake Analysis 2021)

After modifying a binary, an adversary may attempt to impair defenses by preventing it from updating (e.g., via the `yum-versionlock` command or `versionlock.list` file in Linux systems that use the yum package manager).(Citation: Google Cloud Mandiant UNC3886 2024)

## Mitigations
- M1045: Code Signing

## Known Threat Groups Using This Technique
- G1023: APT5
- G1048: UNC3886

## Known Software Using This Technique
- S1136: BFG Agonizer
- S1184: BOLDMOVE
- S1118: BUSHWALK
- S0486: Bonadan
- S0377: Ebury
- S1120: FRAMESTING
- S9010: GlassWorm
- S0604: Industroyer
- S0487: Kessel
- S0641: Kobalos
- S1119: LIGHTWIRE
- S1121: LITTLELAMB.WOOLTEA
- S9043: Mini Shai-Hulud
- S9014: PHASEJAM
- S1104: SLOWPULSE
- S0595: ThiefQuest
- S1116: WARPWIRE
- S1115: WIREFIRE
- S0658: XCSSET
