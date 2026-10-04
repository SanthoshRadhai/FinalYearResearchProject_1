# D3-SEA: Script Execution Analysis

**Reference:** https://d3fend.mitre.org/technique/D3-SEA/  

## Definition
Analyzing the execution of a script to detect unauthorized user activity.

## Parent Class(es)
- Process Analysis

## Relationships
- **analyzes:** Script Application Process
- **kb-reference:** Reference - Detecting script-based malware - Crowdstrike Inc

## Knowledge Base Article
## How it works
Software installed on the host system hooks into a scripting engine to intercept commands before they are executed and block commands if they are determined to be harmful. Pattern matching is used to identify unauthorized commands or in the case of script files, a hash of the file is compared against hashes of known unauthorized script files.

## Considerations
List of known unauthorized script files or regular expression patterns must be kept up to date to ensure detection of new threats.
