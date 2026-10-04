# D3-IPCTA: IPC Traffic Analysis

**Synonym(s):** IPC Analysis  
**Reference:** https://d3fend.mitre.org/technique/D3-IPCTA/  

## Definition
Analyzing standard inter process communication (IPC) protocols to detect deviations from normal protocol activity.

## Parent Class(es)
- Network Traffic Analysis

## Relationships
- **analyzes:** Intranet IPC Network Traffic
- **kb-reference:** Reference - CAR-2015-04-001: Remotely Scheduled Tasks via AT - MITRE
- **kb-reference:** Reference - CAR-2013-05-005: SMB Copy and Execution - MITRE
- **kb-reference:** Reference - CAR-2013-01-003: SMB Events Monitoring - MITRE
- **kb-reference:** Reference - CAR-2013-09-003: SMB Session Setups - MITRE
- **kb-reference:** Reference - CAR-2014-03-001: SMB Write Request - NamedPipes - MITRE
- **kb-reference:** Reference - CAR-2013-05-003: SMB Write Request - MITRE
- **kb-reference:** Reference - Security System with Methodology for Interprocess Communication Control - Check Point Software Tech Inc

## Knowledge Base Article
## How it works
Inter process communication enables applications or threads to share data. This can involve one or more computers. Monitoring IPC in your environment can reveal abnormal or malicious activity.
IPC can occur within a single computer or between multiple computers remotely through network protocols. Thus there are multiple ways to collect and monitor these exchanges between processes. A network protocol analyzer may monitor and parse SMB network traffic to record system activity. A host based monitoring agent may monitor IPC activity contained within a single host to look for deviations from standard usages.

### Examples
 * SMB
 * Zeromq
 * Java RMI API

## Considerations
* IPC can generate substantial amounts of data, and it may not be feasible to collect all of it.
* IPC may occur over loopback interfaces or direct memory access granted by the operating system.
