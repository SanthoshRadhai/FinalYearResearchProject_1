# T1609: Container Administration Command


**ATT&CK ID:** T1609  
**Domain:** Mitre Attack  
**Tactic(s):** Execution  
**Platforms:** Containers  
**Reference:** https://attack.mitre.org/techniques/T1609  

## Description
Adversaries may abuse a container administration service to execute commands within a container. A container administration service such as the Docker daemon, the Kubernetes API server, or the kubelet may allow remote management of containers within an environment.(Citation: Docker Daemon CLI)(Citation: Kubernetes API)(Citation: Kubernetes Kubelet)

In Docker, adversaries may specify an entrypoint during container deployment that executes a script or command, or they may use a command such as <code>docker exec</code> to execute a command within a running container.(Citation: Docker Entrypoint)(Citation: Docker Exec) In Kubernetes, if an adversary has sufficient permissions, they may gain remote execution in a container in the cluster via interaction with the Kubernetes API server, the kubelet, or by running a command such as <code>kubectl exec</code>.(Citation: Kubectl Exec Get Shell)

## Mitigations
- M1018: User Account Management
- M1026: Privileged Account Management
- M1035: Limit Access to Resource Over Network
- M1038: Execution Prevention
- M1042: Disable or Remove Feature or Program

## Known Threat Groups Using This Technique
- G0139: TeamTNT

## Known Software Using This Technique
- S9042: CanisterWorm
- S0601: Hildegard
- S0599: Kinsing
- S9043: Mini Shai-Hulud
- S0683: Peirates
- S0623: Siloscape
- S9041: TeamPCP Cloud Stealer
