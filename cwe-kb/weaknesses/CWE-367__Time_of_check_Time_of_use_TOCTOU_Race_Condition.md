# CWE-367: Time-of-check Time-of-use (TOCTOU) Race Condition

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/367.html  

## Description
The product checks the state of a resource before using that resource, but the resource's state can change between the check and the use in a way that invalidates the results of the check.

## Related Weaknesses
- ChildOf: CWE-362
- ChildOf: CWE-362

## Common Consequences
- Scope: Integrity, Other; Impact: Alter Execution Logic, Unexpected State — The attacker can gain access to otherwise unauthorized resources.
- Scope: Integrity, Other; Impact: Modify Application Data, Modify Files or Directories, Modify Memory, Other — Race conditions such as this kind may be employed to gain read or write access to resources which are not normally readable or writable by the user in question.
- Scope: Integrity, Other; Impact: Other — The resource in question, or other resources (through the corrupted one), may be changed in undesirable ways by a malicious user.
- Scope: Non-Repudiation; Impact: Hide Activities — If a file or other resource is written in this method, as opposed to in a valid way, logging of the activity may not occur.
- Scope: Non-Repudiation, Other; Impact: Other — In some cases it may be possible to delete files a malicious user might not otherwise have access to, such as log files.
- Scope: Other; Impact: Unexpected State — The product may perform invalid actions when the resource is in an unexpected state.

## Potential Mitigations
- [Implementation] The most basic advice for TOCTOU vulnerabilities is to not perform a check before the use. This does not resolve the underlying issue of the execution of a function on a resource whose state and identity cannot be assured, but it does help to limit the false sense of security given by the check.
- [Implementation] When the file being altered is owned by the current user and group, set the effective gid and uid to that of the current user and group when executing this statement.
- [Architecture and Design] Limit the interleaving of operations on files from multiple processes.
- [Implementation, Architecture and Design] If you cannot perform operations atomically and you must share access to the resource between multiple processes or threads, then try to limit the amount of time (CPU cycles) between the check and use of the resource. This will not fix the problem, but it could make it more difficult for an attack to succeed.
- [Implementation] Recheck the resource after the use call to verify that the action was taken appropriately.
- [Architecture and Design] Ensure that some environmental locking mechanism can be used to protect resources effectively.
- [Implementation] Ensure that locking occurs before the check, as opposed to afterwards, such that the resource, as checked, is the same as it is when in use.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- The following code checks a file, then updates its contents.
- The following code is from a program installed setuid root. The program performs certain file operations on behalf of non-privileged users, and uses access checks to ensure that it does not use its root privileges to perform operations that should otherwise be unavailable the current user. The program uses the access() system call to check if the person running the program has permission to access the specified file before it opens the file and performs the necessary operations.
- This code prints the contents of a file if a user has permission.
- This example is adapted from [REF-18]. Assume that this code block is invoked from multiple threads. The switch statement will execute different code depending on the time when MYFILE.txt was last changed.
