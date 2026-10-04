# CWE-479: Signal Handler Use of a Non-reentrant Function

**Abstraction:** Variant  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/479.html  

## Description
The product defines a signal handler that calls a non-reentrant function.

## Extended Description
Non-reentrant functions are functions that cannot safely be called, interrupted, and then recalled before the first call has finished without resulting in memory corruption. This can lead to an unexpected system state and unpredictable results with a variety of potential consequences depending on context, including denial of service and code execution. Many functions are not reentrant, but some of them can result in the corruption of memory if they are used in a signal handler. The function call syslog() is an example of this. In order to perform its functionality, it allocates a small amount of memory as "scratch space." If syslog() is suspended by a signal call and the signal handler calls syslog(), the memory used by both of these functions enters an undefined, and possibly, exploitable state. Implementations of malloc() and free() manage metadata in global structures in order to track which memory is allocated versus which memory is available, but they are non-reentrant. Simultaneous calls to these functions can cause corruption of the metadata.

## Related Weaknesses
- ChildOf: CWE-828
- ChildOf: CWE-663
- CanPrecede: CWE-123

## Common Consequences
- Scope: Integrity, Confidentiality, Availability; Impact: Execute Unauthorized Code or Commands — It may be possible to execute arbitrary code through the use of a write-what-where condition.
- Scope: Integrity; Impact: Modify Memory, Modify Application Data — Signal race conditions often result in data corruption.

## Potential Mitigations
- [Requirements] Require languages or libraries that provide reentrant functionality, or otherwise make it easier to avoid this weakness.
- [Architecture and Design] Design signal handlers to only set flags rather than perform complex functionality.
- [Implementation] Ensure that non-reentrant functions are not found in signal handlers.
- [Implementation] Use sanity checks to reduce the timing window for exploitation of race conditions. This is only a partial solution, since many attacks might fail, but other attacks still might work within the narrower window, even accidentally.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- In this example, a signal handler uses syslog() to log a message:
