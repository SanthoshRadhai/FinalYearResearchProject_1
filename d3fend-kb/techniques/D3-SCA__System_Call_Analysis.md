# D3-SCA: System Call Analysis

**Reference:** https://d3fend.mitre.org/technique/D3-SCA/  

## Definition
Analyzing system calls to determine whether a process is exhibiting unauthorized behavior.

## Parent Class(es)
- Process Analysis

## Relationships
- **analyzes:** System Call
- **kb-reference:** Reference - CAR-2020-05-001: MiniDump of LSASS - MITRE
- **kb-reference:** Reference - CAR-2021-05-011: Create Remote Thread into LSASS - MITRE
- **kb-reference:** Reference - CAR-2019-08-001: Credential Dumping via Windows Task Manager - MITRE
- **kb-reference:** Reference - CAR-2013-10-002: DLL Injection via Load Library - MITRE
- **kb-reference:** Reference - Deterministic method for detecting and blocking of exploits on interpreted code - K2 Cyber Security Inc
- **kb-reference:** Reference - Hardware-assisted system and method for detecting and analyzing system calls made to an operting system kernel - Endgame Inc
- **kb-reference:** Reference - Malware detection in event loops - Crowdstrike Inc
- **kb-reference:** Reference - Post sandbox methods and systems for detecting and blocking zero-day exploits via api call validation - K2 Cyber Security Inc

## Knowledge Base Article
## How it works

System calls are APIs between a user application and the operating system [1].

By analyzing a process's use of these APIs, it is, in some cases, possible to ascertain whether a program is exhibiting unauthorized behavior, including trying to escalate its privileges.

### Gathering System Calls
A common method to capture system calls is to use kernel APIs to hook [2] a process's system call invocations.

The Linux system call `ptrace` tracks other system calls in a process and allows their alteration; this is made use of by GDB.  `strace` utilizes `ptrace` and will print to stdout each system call invoked. Other applications record this data in local or remote databases.

The log entry for each system call, which may reference additional information such as the date and time, and the process tree for the process which made the system call, is relayed, in real time or post-facto, to an analysis module which consults a catalog or model to determine whether the distribution matches a known-good or known-bad pattern.


### Analysis

System calls are analyzed with a variety of methods. Some analytics look for specific sequences of instructions, others may apply statistical methods to identify abnormal behavior. Sequences of instructions can be abstracted into conceptually higher order user activities, for example:

* An attacker executes many system calls in a short period of time, with several sequences which could be used to escalate privileges.
* Getting the contents from a URL, writing to a new file, and then executing the same file.
* A ransomware program which either uses a loop or creates many threads to: read a specified file, encrypt its contents, create an output file with a similar name to the original file, and delete the unencrypted original.

## Considerations

* Duplicative or extraneous system calls may be added to malware to defeat analytics.
* Malware could replace API hooking instructions to allow system calls to be made without being monitored.
* A model built from a training set of system calls and related data may not be updated fast enough to detect new threats.


[1] [Syscalls](http://man7.org/linux/man-pages/man2/syscalls.2.html)

[2] [Hooking](http://dbpedia.org/resource/Hooking)
