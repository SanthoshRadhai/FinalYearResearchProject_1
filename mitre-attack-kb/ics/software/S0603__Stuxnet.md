# S0603: Stuxnet

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0603  
**Aliases:** Stuxnet, W32.Stuxnet  
**Platforms:** Windows  

## Description
[Stuxnet](https://attack.mitre.org/software/S0603) was the first publicly reported malware to specifically target industrial control systems devices. [Stuxnet](https://attack.mitre.org/software/S0603) is a large and complex malware that utilized multiple behaviors, including numerous zero-day vulnerabilities, a sophisticated Windows rootkit, and network infection routines.(Citation: Nicolas Falliere, Liam O Murchu, Eric Chien February 2011)(Citation: CISA ICS Advisory ICSA-10-272-01)(Citation: ESET Stuxnet Under the Microscope)(Citation: Langer Stuxnet) [Stuxnet](https://attack.mitre.org/software/S0603) was discovered in 2010, with some components being used as early as November 2008.(Citation: Nicolas Falliere, Liam O Murchu, Eric Chien February 2011)

## Techniques Used
- T0801: Monitor Process State
- T0807: Command-Line Interface
- T0821: Modify Controller Tasking
- T0831: Manipulation of Control
- T0832: Manipulation of View
- T0834: Native API
- T0835: Manipulate I/O Image
- T0836: Modify Parameter
- T0842: Network Sniffing
- T0843: Program Download
- T0847: Replication Through Removable Media
- T0849: Masquerading
- T0851: Rootkit
- T0863: User Execution
- T0866: Exploitation of Remote Services
- T0867: Lateral Tool Transfer
- T0869: Standard Application Layer Protocol
- T0873.001: Siemens Project File Format
- T0874: Hooking
- T0877: I/O Image
- T0885: Commonly Used Port
- T0886: Remote Services
- T0888: Remote System Information Discovery
- T0889: Modify Program
- T1694.002: Hardcoded Credentials
