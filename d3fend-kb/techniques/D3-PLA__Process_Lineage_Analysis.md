# D3-PLA: Process Lineage Analysis

**Synonym(s):** Process Tree Analysis  
**Reference:** https://d3fend.mitre.org/technique/D3-PLA/  

## Definition
Identification of suspicious processes executing on an end-point device by examining the ancestry and siblings of a process, and the associated metadata of each node on the tree, such as process execution, duration, and order relative to siblings and ancestors.

## Parent Class(es)
- Process Spawn Analysis

## Relationships
- **analyzes:** Process
- **analyzes:** Process Tree
- **kb-reference:** Reference - CAR-2020-11-002: Local Network Sniffing - MITRE
- **kb-reference:** Reference - CAR-2020-11-004: Processes Started From Irregular Parent - MITRE
- **kb-reference:** Reference - CAR-2021-02-002: Get System Elevation - MITRE
- **kb-reference:** Reference - CAR-2021-05-003: BCDEdit Failure Recovery Modification - MITRE
- **kb-reference:** Reference - CAR-2014-11-008: Command Launched from WinLogon - MITRE
- **kb-reference:** Reference - CAR-2014-11-003: Debuggers for Accessibility Applications - MITRE
- **kb-reference:** Reference - CAR-2019-04-002: Generic Regsvr32 - MITRE
- **kb-reference:** Reference - CAR-2014-11-002: Outlier Parents of Cmd - MITRE
- **kb-reference:** Reference - CAR-2013-02-003: Processes Spawning cmd.exe - MITRE
- **kb-reference:** Reference - CAR-2013-04-002: Quick execution of a series of suspicious commands - MITRE
- **kb-reference:** Reference - CAR-2013-03-001: Reg.exe called from Command Shell - MITRE
- **kb-reference:** Reference - CAR-2014-12-001: Remotely Launched Executables via WMI - MITRE
- **kb-reference:** Reference - CAR-2013-09-005: Service Outlier Executables - MITRE
- **kb-reference:** Reference - CAR-2014-07-001: Service Search Path Interception - MITRE
- **kb-reference:** Reference - CAR-2014-05-002: Services launching Cmd - MITRE
- **kb-reference:** Reference - System and methods thereof for causality identification and attributions determination of processes in a network - Palo Alto Networks IncCyber Secdo Ltd
- **kb-reference:** Reference - System and methods thereof for identification of suspicious system processes - Palo Alto Networks Inc
- **kb-reference:** Reference - CAR-2019-04-001: UAC Bypass - MITRE

## Knowledge Base Article
## How it works
Process tree analysis techniques gather information on how a process was initiated to determine if a process is malicious. For example, if a process was not initiated from boot or not initiated by another process, that process is identified as suspicious. Also, if a new process was started before a process initiated by the device (ex. during boot) and that new process was not initiated by a user (which can be determined by examining process parameters such as type of process, its creator, source, etc.) the process is identified as suspicious.

For example, Microsoft Word may block execution of any subprocess that is not in an approved path.

## Considerations
* Attackers may spoof the parent PID (https://attack.mitre.org/techniques/T1502/), rendering such after-the-fact analysis on process lineage ineffective.
* Processes may hide from various means of detection; an example on Linux is where a rootkit might remove key files for the process from its directory in /proc.
* Zombie processes.
