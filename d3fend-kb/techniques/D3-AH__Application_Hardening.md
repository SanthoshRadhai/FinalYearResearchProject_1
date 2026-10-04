# D3-AH: Application Hardening

**Synonym(s):** Process Hardening  
**Reference:** https://d3fend.mitre.org/technique/D3-AH/  

## Definition
Application Hardening makes an executable application more resilient to a class of exploits which either introduce new code or execute unwanted existing code. These techniques may be applied at compile-time or on an application binary.

## Parent Class(es)
- Defensive Technique

## Relationships
- **enables:** Harden

## Knowledge Base Article
## Technique Overview

Exploits may, for example, rely on knowledge of addresses in a process's memory, they may alter memory contents, and they may cause a program to use instructions in a way that they were not intended.  By, for example, including code that dynamically changes the memory address of data or code on each run, introducing logic to validating the memory contents before certain potentially dangerous flows are executed, or monitoring a program for unusual sequence of instructions, this makes it harder for an attacker to craft a working exploit.
