# D3-PS: Process Suspension

**Reference:** https://d3fend.mitre.org/technique/D3-PS/  

## Definition
Suspending a running process on a computer system.

## Parent Class(es)
- Process Eviction

## Relationships
- **kb-reference:** Reference - PsSuspend - Microsoft
- **suspends:** Process

## Knowledge Base Article
## How it works

A running process might be suspended to mitigate its immediate effects if it is exhibiting anomalous, unauthorized, or malicious behavior. Defenders may choose to suspend rather than terminate to analyze the process first and resume the process if deemed benign.

### System-provided functions

#### Windows tools
In Windows, the `PsSuspend` command line utility from the SysInternals Suite provides functionality to suspend processes on a local or remote system.
