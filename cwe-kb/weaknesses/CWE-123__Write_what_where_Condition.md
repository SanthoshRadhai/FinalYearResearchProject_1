# CWE-123: Write-what-where Condition

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/123.html  

## Description
Any condition where the attacker has the ability to write an arbitrary value to an arbitrary location, often as the result of a buffer overflow.

## Related Weaknesses
- ChildOf: CWE-787
- ChildOf: CWE-787
- ChildOf: CWE-119

## Common Consequences
- Scope: Integrity, Confidentiality, Availability, Access Control; Impact: Modify Memory, Execute Unauthorized Code or Commands, Gain Privileges or Assume Identity, DoS: Crash, Exit, or Restart, Bypass Protection Mechanism — Clearly, write-what-where conditions can be used to write data to areas of memory outside the scope of a policy. Also, they almost invariably can be used to execute arbitrary code, which is usually outside the scope of a program's implicit security policy. If the attacker can overwrite a pointer's worth of memory (usually 32 or 64 bits), they can redirect a function pointer to their own malicious code. Even when the attacker can only modify a single byte arbitrary code execution can be possible. Sometimes this is because the same problem can be exploited repeatedly to the same effect. Other times it is because the attacker can overwrite security-critical application-specific data -- such as a flag indicating whether the user is an administrator.
- Scope: Integrity, Availability; Impact: DoS: Crash, Exit, or Restart, Modify Memory — Many memory accesses can lead to program termination, such as when writing to addresses that are invalid for the current process.
- Scope: Access Control, Other; Impact: Bypass Protection Mechanism, Other — When the consequence is arbitrary code execution, this can often be used to subvert any other security service.

## Potential Mitigations
- [Architecture and Design] Use a language that provides appropriate memory abstractions.
- [Operation] Use OS-level preventative functionality integrated after the fact. Not a complete solution.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)
- [Automated Dynamic Analysis] Use tools that are integrated during compilation to insert runtime error-checking mechanisms related to memory safety errors, such as AddressSanitizer (ASan) for C/C++ [REF-1518].

## Demonstrative Examples (summary)
- The classic example of a write-what-where condition occurs when the accounting information for memory allocations is overwritten in a particular fashion. Here is an example of potentially vulnerable code:
