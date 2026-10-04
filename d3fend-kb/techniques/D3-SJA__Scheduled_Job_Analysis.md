# D3-SJA: Scheduled Job Analysis

**Synonym(s):** Scheduled Job Execution  
**Reference:** https://d3fend.mitre.org/technique/D3-SJA/  

## Definition
Analysis of source files, processes, destination files, or destination servers associated with a scheduled job to detect unauthorized use of job scheduling.

## Parent Class(es)
- Operating System Monitoring

## Relationships
- **analyzes:** Job Schedule
- **kb-reference:** Reference - CAR-2013-05-004: Execution with AT - MITRE
- **kb-reference:** Reference - CAR-2013-08-001: Execution with schtasks - MITRE
- **kb-reference:** Reference - Preventing execution of task scheduled malware - McAfee LLC

## Knowledge Base Article
## How it works
Scheduled job execution can be utilized by adversaries for the purpose of persistence, conducting remote execution, or gaining privileges. Details of a scheduled job such as associated source files, processes, destination files, or destination servers are first identified and analyzed and then compared against an anti-malware signature database, whitelist, or reputation server. For example, a file associated with a scheduled job to be executed at a specified time or a remote server that is accessed as part of a scheduled task is compared against an anti-malware signature database, whitelist, or reputation server, and if a match is found, execution is denied and an alert is generated.

In addition to traditional scheduled jobs, triggers can be set to execute a specific command after detecting a specific event in the system, such as with WMI Event Subscriptions in Windows.

## Considerations
Jobs can be scheduled in many different and sometimes creative ways through operating system capabilities.
