# D3-PSMD: Process Self-Modification Detection

**Reference:** https://d3fend.mitre.org/technique/D3-PSMD/  

## Definition
Detects processes that modify, change, or replace their own code at runtime.

## Parent Class(es)
- Process Analysis

## Relationships
- **analyzes:** Process
- **kb-reference:** Reference - System and Method for Process Hollowing Detection - Carbon Black Inc

## Knowledge Base Article
## How it Works
A security agent installed on the host machine intercepts API calls between a process and operating system. Intercepted API calls are then compared against attack signatures/patterns to identify API calls that modify executable memory or modify the entry point address of a suspended child process. Attack patterns include:

* Executable code of a suspended child process removed from memory by one or more API calls.
* New executable code injected and / or loaded into memory of a suspended child process by one or more API calls.
* Executable code modified by one or more API calls.
* Next instruction pointer value in memory modified by one or more API calls.

## Considerations
Comparing loaded code segments of processes with what is expected to have been loaded from a file can result in false positives, due to legitimate uses of self-modification for decrypting or uncompressing code segments.
