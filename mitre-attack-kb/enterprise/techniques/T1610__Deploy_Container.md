# T1610: Deploy Container


**ATT&CK ID:** T1610  
**Domain:** Mitre Attack  
**Tactic(s):** Execution  
**Platforms:** Containers  
**Reference:** https://attack.mitre.org/techniques/T1610  

## Description
Adversaries may deploy a container into an environment to facilitate execution or evade defenses. In some cases, adversaries may deploy a new container to execute processes associated with a particular image or deployment, such as processes that execute or download malware. In others, an adversary may deploy a new container configured without network rules, user limitations, etc. to bypass existing defenses within the environment. In Kubernetes environments, an adversary may attempt to deploy a privileged or vulnerable container into a specific node in order to [Escape to Host](https://attack.mitre.org/techniques/T1611) and access other containers running on the node. (Citation: AppSecco Kubernetes Namespace Breakout 2020)

Containers can be deployed by various means, such as via Docker's <code>create</code> and <code>start</code> APIs or via a web application such as the Kubernetes dashboard or Kubeflow. (Citation: Docker Container)(Citation: Kubernetes Dashboard)(Citation: Kubeflow Pipelines) In Kubernetes environments, containers may be deployed through workloads such as ReplicaSets or DaemonSets, which can allow containers to be deployed across multiple nodes.(Citation: Kubernetes Workload Management) Adversaries may deploy containers based on retrieved or built malicious images or from benign images that download and execute malicious payloads at runtime.(Citation: Aqua Build Images on Hosts)

## Mitigations
- M1018: User Account Management
- M1030: Network Segmentation
- M1035: Limit Access to Resource Over Network
- M1047: Audit

## Known Threat Groups Using This Technique
- G0139: TeamTNT

## Known Software Using This Technique
- S0600: Doki
- S0599: Kinsing
- S0683: Peirates
