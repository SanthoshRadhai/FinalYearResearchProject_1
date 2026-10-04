# T1694: Insecure Credentials


**ATT&CK ID:** T1694  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Persistence, Lateral Movement  
**Reference:** https://attack.mitre.org/techniques/T1694  

## Description
Adversaries may target insecure credentials as a means to persist on a system or device or move laterally from one system or device to another. Insecure credentials may appear as default credentials which are pre-configured credentials on a system, device, or software that are well-known in documentation or hard-coded credentials which are built into the system, device, or software that cannot be changed or not easily changed because of the impact on control processes.(Citation: NIST SP 800-82r3)(Citation: ICS-ALERT-13-164-01)(Citation: OT IceFall)
 Adversaries often times use insecure credentials to evade detection as they are typically forgotten about by system and device owners.

## Sub-techniques
- T1694.001: Default Credentials
- T1694.002: Hardcoded Credentials

## Mitigations
- M0801: Access Management
