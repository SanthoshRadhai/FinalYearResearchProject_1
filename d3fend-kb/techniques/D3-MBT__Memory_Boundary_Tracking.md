# D3-MBT: Memory Boundary Tracking

**Reference:** https://d3fend.mitre.org/technique/D3-MBT/  

## Definition
Analyzing a call stack for return addresses which point to unexpected  memory locations.

## Parent Class(es)
- Operating System Monitoring

## Relationships
- **analyzes:** Process Code Segment
- **kb-reference:** Reference - Inferential exploit attempt detection - Crowdstrike Inc

## Knowledge Base Article
## How it works
This technique monitors for indicators of whether a return address is outside memory previously allocated for an object (i.e. function, module, process, or thread). If so, code that the return address points to is treated as malicious code.

## Considerations
Kernel malware can manipulate memory contents, for example modifying pointers to hide processes, and thereby impact the accuracy of memory allocation information used to perform the analysis.
