# D3-EDL: Executable Denylisting

**Synonym(s):** Executable Blacklisting  
**Reference:** https://d3fend.mitre.org/technique/D3-EDL/  

## Definition
Blocking the execution of files on a host in accordance with defined application policy rules.

## Parent Class(es)
- Execution Isolation

## Relationships
- **blocks:** Executable File
- **filters:** Create Process
- **kb-reference:** Reference - Content extractor and analysis system - Bit 9 Inc, Carbon Black Inc
- **kb-reference:** Reference - Method and apparatus for increasing the speed at which computer viruses are detected - McAfee LLC

## Knowledge Base Article
## How it works

#### Criteria

A policy-enforcing application can register an application for denylisting based on conditions including the following:

* File attributes
    * file name
    * file path
    * file hash
    * file publisher, as obtained from the digital signature
    * permissions of the file
* File malware scan (eg. Windows SmartScreen)
* User-File combination

This may be done to prevent execution of applications which are:

* an old version with known vulnerabilities
* without a valid license, which could cause legal issues
* in a directory that is accessible to low-privileged users, that could be accessed by a malware dropper
* known trojan horse programs
* too open in their permissions, possibly set to run as a user other than the originator or allowing execution when they should not be
* a match to the hash of other known malware
* are detected as undesirable based on a file scan runtime behavior

System administrators will customize the rules for the given environment.

#### Backend

The policy-enforcing program may work by running in kernel mode, and [intercepting] [system calls which execute a process].

## Considerations

* If denylisting is done by filename, filepath, or hash, these mechanisms may be a worthy first line of defense and detection, but could still be evaded by an attacker.
* Continuous management is needed to keep the denylist up to date, whether it is based on hash, publisher, behavior, or any other digital artifact.
* Although denylists based on attributes such as file path and virus scan could defend against some threats which they have not been explicitly coded to block, denylists may not provide protection from new, unknown, or zero day attacks.


## Examples
On a Windows machine the Windows Defender Application Control (WDAC) policy enforcement is run in the kernel and allows for restricting applications.
