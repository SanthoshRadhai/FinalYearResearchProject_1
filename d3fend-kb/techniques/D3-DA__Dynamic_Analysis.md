# D3-DA: Dynamic Analysis

**Synonym(s):** Malware Detonation, Malware Sandbox  
**Reference:** https://d3fend.mitre.org/technique/D3-DA/  

## Definition
Executing or opening a file in a synthetic "sandbox" environment to determine if the file is a malicious program or if the file exploits another program such as a document reader.

## Parent Class(es)
- File Analysis

## Relationships
- **analyzes:** Document File
- **analyzes:** Executable File
- **kb-reference:** Reference - Malware analysis system - Palo Alto Networks Inc
- **kb-reference:** Reference - Use of an application controller to monitor and control software file and application environments - Sophos Ltd

## Knowledge Base Article
## How it works
Analyzing the interaction of a piece of code with a system while the code is being executed in a controlled environment such as a sandbox, virtual machine, or simulator. This exposes the natural behavior of the piece of code without requiring the code to be disassembled.

## Considerations
 * Malware often detects a fake environment, then changes its behavior accordingly. For example, it could detect that the system clock is being sped up in an effort to get it to execute commands that it would normally only execute at a later time, or that the hardware manufacturer of the machine is a virtualization provider.
 * Malware can attempt to determine if it is being debugged, and change its behavior accordingly.
 * For maximum fidelity, the simulated and real environments should be as similar as possible because the malware could perform differently in different environments.
 * Sometimes the malware behavior is triggered only under certain conditions (on a specific system date, after a certain time, or after it is sent a specific command) and can't be detected through a short execution in a virtual environment.

## Implementations
* Cuckoo Sandbox
