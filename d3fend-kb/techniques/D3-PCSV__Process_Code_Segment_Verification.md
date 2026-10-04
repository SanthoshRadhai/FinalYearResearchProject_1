# D3-PCSV: Process Code Segment Verification

**Reference:** https://d3fend.mitre.org/technique/D3-PCSV/  

## Definition
Comparing the "text" or "code" memory segments to a source of truth.

## Parent Class(es)
- Process Analysis

## Relationships
- **kb-reference:** Reference - Anti-tamper system with self-adjusting guards - ARXAN TECHNOLOGIES Inc
- **kb-reference:** Reference - Guards for application in software tamperproofing - Purdue Research Foundation
- **kb-reference:** Reference - System and method for detecting malware injected into memory of a computing device - Endgame Inc
- **kb-reference:** Reference - System and method for validating in-memory integrity of executable files to identify malicious activity - Endgame Inc
- **kb-reference:** Reference - Tamper proof mutating software - ARXAN TECHNOLOGIES Inc
- **kb-reference:** Reference - Threat detection through the accumulated detection of threat characteristics - Sophos Ltd
- **verifies:** Process Code Segment

## Knowledge Base Article
## How it works
A process code segment is an executable portion of computer memory allocated to a particular process. Process Code Segment Verification implements verification to compare a process code segment to some expected value.

### Verification logic
Verification can occur during application startup, or continuously during execution. The logic which verifies the process code may be separate in a third-party process, embedded in the application itself at compile time, or dynamically linked at runtime.

### System of record
Examples of systems of record:

 * On-disk application binary files or checksums
 * Remotely stored binary data or checksums
 * Embedded binary data or checksums

### Post Verification Actions
If the verification function determines a process code segment may have been altered, a capability may invoke Eviction techniques  as **Process Termination** to end the current process, or **Executable Blacklisting** to prevent the executable from launching in the future.

## Considerations

### False positives

False positives commonly occur in the case that the layout of code in the process segment is legitimately modified:

*  Operating system features or third-party security software may modify the layout of process code, for example in the defensive technique **Segment Address Offset Randomization**, or in the case that a module is rebased.  In both of these cases, the alteration occurs before the code is fully loaded into memory, and it would be possible to avoid the false positive by securely feeding this constant offset and any relocation data into the verification logic.

* Process code segments may be written to modify themselves or other process code segments; however, this goes against widely-accepted current practices in software development.

### False negatives

False negatives can occur via alteration of the verification logic or source of truth, or insufficient verification logic.

* Verification techniques which are executed only locally may be defeated by altering the local verification logic.

* Verification that is run only on a recurring basis could be evaded if the malicious alteration is completed before verification is run.

* Verification that requests an operation to be performed on a subset of the code segment could be evaded by performing that operation on a copy of the relevant bytes of the code segment.

* Verification based on a system of record that can be altered may fail if that system of record is modifiable by a malicious user.
