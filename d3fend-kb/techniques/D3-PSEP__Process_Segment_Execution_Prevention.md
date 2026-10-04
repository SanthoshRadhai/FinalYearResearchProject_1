# D3-PSEP: Process Segment Execution Prevention

**Synonym(s):** Execute Disable, No Execute  
**Reference:** https://d3fend.mitre.org/technique/D3-PSEP/  

## Definition
Preventing execution of any address in a memory region other than the code segment.

## Parent Class(es)
- Application Hardening

## Relationships
- **kb-reference:** Reference - Mitigate threats by using Windows 10 security features: Data Execution Prevention - Microsoft
- **kb-reference:** Reference - What is NX/XD feature?
- **neutralizes:** Process Segment

## Knowledge Base Article
## How it works

During execution of a process, the instruction pointer register should only point to addresses in a code segment (also called the .text segment), as this is the sole segment which should contain program code.

When this technique detects an attempt to execute something that has been designated as non-executable, other techniques such as those in **Process Eviction** might be invoked, such as **Process Termination** to end the current process, or **Executable Blacklisting** to blacklist the potentially vulnerable or malfunctioning executable.

### Software-based implementations
The software-based implementation in Windows XP SP2 might not check that every time the instruction pointer is changed, and does not check on each jump or return.  Before calling an exception handler, Windows XP SP2 software-enforced DEP checks whether the exception handler is located in a memory region marked as executable.  If the program was also built with SafeSEH, this implementation also checks before changing control to the exception handler whether it is a registered exception handler in the program's file on disk.

### Hardware-based implementations
The NX (No Execute) or XD (Execute Disable) bit on the processor specifies whether a certain part of memory is executable.  Early implementations set this bit by the memory segment, while modern implementations which are built on the flat memory model often store this bit in each entry of the page table, to control execution by the page.


## Considerations

Non-hardware process data segment execution prevention is more susceptible to being able to be turned off for a page of memory.

Different implementations of this defense have been in place since the 1980s, but implementation stalled when larger 16-bit programs began stuffing code in the segments usually reserved for data. Many modern programs follow the best practice of separation of code and data, are able to run under this defense.

ROP or ret2libc/return-to-function attacks could bypass this defense, as although they may pass attacker-controlled data or stack frames to a function, they abuse functions that are legitimately located in the .text segment (code segment) of the program.  For those, more advanced defenses such as a table of valid jump addresses, function call analysis, or return depth analysis could be used.
