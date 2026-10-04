# T1538: Cloud Service Dashboard


**ATT&CK ID:** T1538  
**Domain:** Mitre Attack  
**Tactic(s):** Discovery  
**Platforms:** IaaS, SaaS, Office Suite, Identity Provider  
**Reference:** https://attack.mitre.org/techniques/T1538  

## Description
An adversary may use a cloud service dashboard GUI with stolen credentials to gain useful information from an operational cloud environment, such as specific services, resources, and features. For example, the GCP Command Center can be used to view all assets, review findings of potential security risks, and run additional queries, such as finding public IP addresses and open ports.(Citation: Google Command Center Dashboard)

Depending on the configuration of the environment, an adversary may be able to enumerate more information via the graphical dashboard than an API. This also allows the adversary to gain information without manually making any API requests.

## Mitigations
- M1018: User Account Management

## Known Threat Groups Using This Technique
- G1015: Scattered Spider
