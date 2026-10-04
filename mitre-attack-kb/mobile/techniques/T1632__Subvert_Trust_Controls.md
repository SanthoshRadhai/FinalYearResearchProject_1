# T1632: Subvert Trust Controls


**ATT&CK ID:** T1632  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Defense Evasion  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1632  

## Description
Adversaries may undermine security controls that will either warn users of untrusted activity or prevent execution of untrusted applications. Operating systems and security products may contain mechanisms to identify programs or websites as possessing some level of trust. Examples of such features include: an app being allowed to run because it is signed by a valid code signing certificate; an OS prompt alerting the user that an app came from an untrusted source; or getting an indication that you are about to connect to an untrusted site. The method adversaries use will depend on the specific mechanism they seek to subvert.

## Sub-techniques
- T1632.001: Code Signing Policy Modification

## Mitigations
- M1006: Use Recent OS Version
- M1011: User Guidance
- M1012: Enterprise Policy
