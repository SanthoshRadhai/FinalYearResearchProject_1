# T1553: Subvert Trust Controls


**ATT&CK ID:** T1553  
**Domain:** Mitre Attack  
**Tactic(s):** Defense Impairment  
**Platforms:** Linux, macOS, Windows  
**Reference:** https://attack.mitre.org/techniques/T1553  

## Description
Adversaries may undermine security controls that will either warn users of untrusted activity or prevent execution of untrusted programs. Operating systems and security products may contain mechanisms to identify programs or websites as possessing some level of trust. Examples of such features would include a program being allowed to run because it is signed by a valid code signing certificate, a program prompting the user with a warning because it has an attribute set from being downloaded from the Internet, or getting an indication that you are about to connect to an untrusted site.

Adversaries may attempt to subvert these trust mechanisms. The method adversaries use will depend on the specific mechanism they seek to subvert. Adversaries may conduct [File and Directory Permissions Modification](https://attack.mitre.org/techniques/T1222) or [Modify Registry](https://attack.mitre.org/techniques/T1112) in support of subverting these controls.(Citation: SpectorOps Subverting Trust Sept 2017) Adversaries may also create or steal code signing certificates to acquire trust on target systems.(Citation: Securelist Digital Certificates)(Citation: Symantec Digital Certificates)

## Sub-techniques
- T1553.001: Gatekeeper Bypass
- T1553.002: Code Signing
- T1553.003: SIP and Trust Provider Hijacking
- T1553.004: Install Root Certificate
- T1553.005: Mark-of-the-Web Bypass
- T1553.006: Code Signing Policy Modification

## Mitigations
- M1024: Restrict Registry Permissions
- M1026: Privileged Account Management
- M1028: Operating System Configuration
- M1038: Execution Prevention
- M1054: Software Configuration

## Known Threat Groups Using This Technique
- G0001: Axiom

## Known Software Using This Technique
- S9008: Shai-Hulud
