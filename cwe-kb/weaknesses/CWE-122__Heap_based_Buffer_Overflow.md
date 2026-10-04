# CWE-122: Heap-based Buffer Overflow

**Abstraction:** Variant  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/122.html  

## Description
A heap overflow condition is a buffer overflow, where the buffer that can be overwritten is allocated in the heap portion of memory, generally meaning that the buffer was allocated using a routine such as malloc().

## Related Weaknesses
- ChildOf: CWE-788
- ChildOf: CWE-787

## Common Consequences
- Scope: Availability; Impact: DoS: Crash, Exit, or Restart, DoS: Resource Consumption (CPU), DoS: Resource Consumption (Memory) — Buffer overflows generally lead to crashes. Other attacks leading to lack of availability are possible, including putting the program into an infinite loop.
- Scope: Integrity, Confidentiality, Availability, Access Control; Impact: Execute Unauthorized Code or Commands, Bypass Protection Mechanism, Modify Memory — Buffer overflows often can be used to execute arbitrary code, which is usually outside the scope of a program's implicit security policy. Besides important user data, heap-based overflows can be used to overwrite function pointers that may be living in memory, pointing it to the attacker's code. Even in applications that do not explicitly use function pointers, the run-time will usually leave many in memory. For example, object methods in C++ are generally implemented using function pointers. Even in C programs, there is often a global offset table used by the underlying runtime.
- Scope: Integrity, Confidentiality, Availability, Access Control, Other; Impact: Execute Unauthorized Code or Commands, Bypass Protection Mechanism, Other — When the consequence is arbitrary code execution, this can often be used to subvert any other security service.

## Potential Mitigations
- Pre-design: Use a language or compiler that performs automatic bounds checking.
- [Architecture and Design] Use an abstraction library to abstract away risky APIs. Not a complete solution.
- [Operation, Build and Compilation] Use automatic buffer overflow detection mechanisms that are offered by certain compilers or compiler extensions. Examples include: the Microsoft Visual Studio /GS flag, Fedora/Red Hat FORTIFY_SOURCE GCC flag, StackGuard, and ProPolice, which provide various mechanisms including canary-based detection and range/index checking. D3-SFCV (Stack Frame Canary Validation) from D3FEND [REF-1334] discusses canary-based detection in detail.
- [Operation, Build and Compilation] Run or compile the software using features or extensions that randomly arrange the positions of a program's executable and libraries in memory. Because this makes the addresses unpredictable, it can prevent an attacker from reliably jumping to exploitable code. Examples include Address Space Layout Randomization (ASLR) [REF-58] [REF-60] and Position-Independent Executables (PIE) [REF-64]. Imported modules may be similarly realigned if their default memory addresses conflict with other modules, in a process known as "rebasing" (for Windows) and "prelinking" (for Linux) [REF-1332] using randomly generated addresses. ASLR for libraries cannot be used in conjunction with prelink since it would require relocating the libraries at run-time, defeating the whole purpose of prelinking. For more information on these techniques see D3-SAOR (Segment Address Offset Randomization) from D3FEND [REF-1335].
- [Implementation] Implement and perform bounds checking on input.
- [Implementation] Do not use dangerous functions such as gets. Look for their safe equivalent, which checks for the boundary.
- [Operation] Use OS-level preventative functionality. This is not a complete solution, but it provides some defense in depth.

## Detection Methods
- [Fuzzing] Fuzz testing (fuzzing) is a powerful technique for generating large numbers of diverse inputs - either randomly or algorithmically - and dynamically invoking the code with those inputs. Even with random inputs, it is often capable of generating unexpected results such as crashes, memory corruption, or resource consumption. Fuzzing effectively produces repeatable test cases that clearly indicate bugs, which helps developers to diagnose the issues.
- [Automated Dynamic Analysis] Use tools that are integrated during compilation to insert runtime error-checking mechanisms related to memory safety errors, such as AddressSanitizer (ASan) for C/C++ [REF-1518].

## Demonstrative Examples (summary)
- While buffer overflow examples can be rather complex, it is possible to have very simple, yet still exploitable, heap-based buffer overflows:
- This example applies an encoding procedure to an input string and stores it into a buffer.
