# T1136: Create Account


**ATT&CK ID:** T1136  
**Domain:** Mitre Attack  
**Tactic(s):** Persistence  
**Platforms:** Windows, IaaS, Linux, macOS, Network Devices, Containers, SaaS, Office Suite, Identity Provider, ESXi  
**Reference:** https://attack.mitre.org/techniques/T1136  

## Description
Adversaries may create an account to maintain access to victim systems.(Citation: Symantec WastedLocker June 2020) With a sufficient level of access, creating such accounts may be used to establish secondary credentialed access that do not require persistent remote access tools to be deployed on the system.

Accounts may be created on the local system or within a domain or cloud tenant. In cloud environments, adversaries may create accounts that only have access to specific services, which can reduce the chance of detection.

## Sub-techniques
- T1136.001: Local Account
- T1136.002: Domain Account
- T1136.003: Cloud Account

## Mitigations
- M1026: Privileged Account Management
- M1028: Operating System Configuration
- M1030: Network Segmentation
- M1032: Multi-factor Authentication

## Known Threat Groups Using This Technique
- G0119: Indrik Spider
- G1045: Salt Typhoon
- G1015: Scattered Spider

## Known Software Using This Technique
- S1199: LockBit 2.0
