# T1127: Trusted Developer Utilities Proxy Execution


**ATT&CK ID:** T1127  
**Domain:** Mitre Attack  
**Tactic(s):** Stealth, Execution  
**Platforms:** Windows  
**Reference:** https://attack.mitre.org/techniques/T1127  

## Description
Adversaries may take advantage of trusted developer utilities to proxy execution of malicious payloads. There are many utilities used for software development related tasks that can be used to execute code in various forms to assist in development, debugging, and reverse engineering.(Citation: engima0x3 DNX Bypass)(Citation: engima0x3 RCSI Bypass)(Citation: Exploit Monday WinDbg)(Citation: LOLBAS Tracker) These utilities may often be signed with legitimate certificates that allow them to execute on a system and proxy execution of malicious code through a trusted process that effectively bypasses application control solutions.

Smart App Control is a feature of Windows that blocks applications it considers potentially malicious from running by verifying unsigned applications against a known safe list from a Microsoft cloud service before executing them.(Citation: Microsoft Smart App Control) However, adversaries may leverage "reputation hijacking" to abuse an operating system’s trust of safe, signed applications that support the execution of arbitrary code. By leveraging [Trusted Developer Utilities Proxy Execution](https://attack.mitre.org/techniques/T1127) to run their malicious code, adversaries may bypass Smart App Control protections.(Citation: Elastic Security Labs)

## Sub-techniques
- T1127.001: MSBuild
- T1127.002: ClickOnce
- T1127.003: JamPlus

## Mitigations
- M1021: Restrict Web-Based Content
- M1038: Execution Prevention
- M1042: Disable or Remove Feature or Program
