# TA0102: Discovery

**Type:** Tactic  
**Reference:** https://attack.mitre.org/tactics/TA0102  

## Description
The adversary is locating information to assess and identify their targets in your environment.

Discovery consists of techniques that adversaries use to survey your ICS environment and gain knowledge about the internal network, control system devices, and how their processes interact. These techniques help adversaries observe the environment and determine next steps for target selection and Lateral Movement. They also allow adversaries to explore what they can control and gain insight on interactions between various control system processes. Discovery techniques are often an act of progression into the environment which enable the adversary to orient themselves before deciding how to act. Adversaries may use Discovery techniques that result in Collection, to help determine how available resources benefit their current objective. A combination of native device communications and functions, and custom tools are often used toward this post-compromise information-gathering objective.

## Techniques in This Tactic
- T0840: Network Connection Enumeration
- T0842: Network Sniffing
- T0846: Remote System Discovery
- T0846.001: Port Scan
- T0846.002: Broadcast Discovery
- T0846.003: Multicast Discovery
- T0887: Wireless Sniffing
- T0888: Remote System Information Discovery
