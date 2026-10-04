# T1613: Container and Resource Discovery


**ATT&CK ID:** T1613  
**Domain:** Mitre Attack  
**Tactic(s):** Discovery  
**Platforms:** Containers  
**Reference:** https://attack.mitre.org/techniques/T1613  

## Description
Adversaries may attempt to discover containers and other resources that are available within a containers environment. Other resources may include images, deployments, pods, nodes, and other information such as the status of a cluster.

These resources can be viewed within web applications such as the Kubernetes dashboard or can be queried via the Docker and Kubernetes APIs.(Citation: Docker API)(Citation: Kubernetes API) In Docker, logs may leak information about the environment, such as the environment’s configuration, which services are available, and what cloud provider the victim may be utilizing. The discovery of these resources may inform an adversary’s next steps in the environment, such as how to perform lateral movement and which methods to utilize for execution.

## Mitigations
- M1018: User Account Management
- M1030: Network Segmentation
- M1035: Limit Access to Resource Over Network

## Known Threat Groups Using This Technique
- G0139: TeamTNT

## Known Software Using This Technique
- S9042: CanisterWorm
- S0601: Hildegard
- S0683: Peirates
- S9041: TeamPCP Cloud Stealer
