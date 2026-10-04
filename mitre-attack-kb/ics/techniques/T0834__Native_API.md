# T0834: Native API


**ATT&CK ID:** T0834  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Execution  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0834  

## Description
Adversaries may directly interact with the native OS application programming interface (API) to access system functions. Native APIs provide a controlled means of calling low-level OS services within the kernel, such as those involving hardware/devices, memory, and processes. (Citation: The MITRE Corporation May 2017) These native APIs are leveraged by the OS during system boot (when other system components are not yet initialized) as well as carrying out tasks and requests during routine operations. 

Functionality provided by native APIs are often also exposed to user-mode applications via interfaces and libraries. For example, functions such as memcpy and direct operations on memory registers can be used to modify user and system memory space.

## Mitigations
- M0938: Execution Prevention

## Known Software Using This Technique
- S1006: PLC-Blaster
- S0603: Stuxnet
- S1009: Triton
