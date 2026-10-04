# D3-SFA: System File Analysis

**Reference:** https://d3fend.mitre.org/technique/D3-SFA/  

## Definition
Monitoring system files such as authentication databases, configuration files, system logs, and system executables for modification or tampering.

## Parent Class(es)
- Operating System Monitoring

## Relationships
- **analyzes:** Operating System File
- **kb-reference:** Reference - CAR-2019-07-001: Access Permission Modification - MITRE
- **kb-reference:** Reference - CAR-2013-01-002: Autorun Differences - MITRE
- **kb-reference:** Reference - CAR-2016-04-002: User Activity from Clearing Event Logs - MITRE

## Knowledge Base Article
## How it works
This technique ensures the integrity of system owned file resources. System files can impact the behavior below the user level.


## Considerations
* Need to manage the size of log file analysis.
* False positives are a concern with this technique and filtering will need to be given additional thought.
* A baseline or snapshot of file checksums should be established for future comparison.
