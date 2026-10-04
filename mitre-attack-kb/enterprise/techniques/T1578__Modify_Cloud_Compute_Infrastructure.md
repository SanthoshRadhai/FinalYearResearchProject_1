# T1578: Modify Cloud Compute Infrastructure


**ATT&CK ID:** T1578  
**Domain:** Mitre Attack  
**Tactic(s):** Defense Impairment  
**Platforms:** IaaS  
**Reference:** https://attack.mitre.org/techniques/T1578  

## Description
An adversary may attempt to modify a cloud account's compute service infrastructure to evade defenses. A modification to the compute service infrastructure can include the creation, deletion, or modification of one or more components such as compute instances, virtual machines, and snapshots.

Permissions gained from the modification of infrastructure components may bypass restrictions that prevent access to existing infrastructure. Modifying infrastructure components may also allow an adversary to evade detection and remove evidence of their presence.(Citation: Mandiant M-Trends 2020)

## Sub-techniques
- T1578.001: Create Snapshot
- T1578.002: Create Cloud Instance
- T1578.003: Delete Cloud Instance
- T1578.004: Revert Cloud Instance
- T1578.005: Modify Cloud Compute Configurations

## Mitigations
- M1018: User Account Management
- M1047: Audit
