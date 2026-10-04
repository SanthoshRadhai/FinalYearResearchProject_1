# CWE-170: Improper Null Termination

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/170.html  

## Description
The product does not terminate or incorrectly terminates a string or array with a null character or equivalent terminator.

## Extended Description
Null termination errors frequently occur in two different ways. An off-by-one error could cause a null to be written out of bounds, leading to an overflow. Or, a program could use a strncpy() function call incorrectly, which prevents a null terminator from being added at all. Other scenarios are possible.

## Related Weaknesses
- ChildOf: CWE-707
- CanPrecede: CWE-120
- CanPrecede: CWE-126
- CanAlsoBe: CWE-147
- PeerOf: CWE-464
- PeerOf: CWE-463
- ChildOf: CWE-20

## Common Consequences
- Scope: Confidentiality, Integrity, Availability; Impact: Read Memory, Execute Unauthorized Code or Commands — The case of an omitted null character is the most dangerous of the possible issues. This will almost certainly result in information disclosure, and possibly a buffer overflow condition, which may be exploited to execute arbitrary code.
- Scope: Confidentiality, Integrity, Availability; Impact: DoS: Crash, Exit, or Restart, Read Memory, DoS: Resource Consumption (CPU), DoS: Resource Consumption (Memory) — If a null character is omitted from a string, then most string-copying functions will read data until they locate a null character, even outside of the intended boundaries of the string. This could: cause a crash due to a segmentation fault cause sensitive adjacent memory to be copied and sent to an outsider trigger a buffer overflow when the copy is being written to a fixed-size buffer.
- Scope: Integrity, Availability; Impact: Modify Memory, DoS: Crash, Exit, or Restart — Misplaced null characters may result in any number of security problems. The biggest issue is a subset of buffer overflow, and write-what-where conditions, where data corruption occurs from the writing of a null character over valid data, or even instructions. A randomly placed null character may put the system into an undefined state, and therefore make it prone to crashing. A misplaced null character may corrupt other data in memory.
- Scope: Integrity, Confidentiality, Availability, Access Control, Other; Impact: Alter Execution Logic, Execute Unauthorized Code or Commands — Should the null character corrupt the process flow, or affect a flag controlling access, it may lead to logical errors which allow for the execution of arbitrary code.

## Potential Mitigations
- [Requirements] Use a language that is not susceptible to these issues. However, be careful of null byte interaction errors (CWE-626) with lower-level constructs that may be written in a language that is susceptible.
- [Implementation] Ensure that all string functions used are understood fully as to how they append null characters. Also, be wary of off-by-one errors when appending nulls to the end of strings.
- [Implementation] If performance constraints permit, special code can be added that validates null-termination of string buffers, this is a rather naive and error-prone solution.
- [Implementation] Switch to bounded string manipulation functions. Inspect buffer lengths involved in the buffer overrun trace reported with the defect.
- [Implementation] Add code that fills buffers with nulls (however, the length of buffers still needs to be inspected, to ensure that the non null-terminated string is not written at the physical end of the buffer).

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- The following code reads from cfgfile and copies the input into inputbuf using strcpy(). The code mistakenly assumes that inputbuf will always contain a NULL terminator.
- In the following code, readlink() expands the name of a symbolic link stored in pathname and puts the absolute path into buf. The length of the resulting value is then calculated using strlen().
- While the following example is not exploitable, it provides a good example of how nulls can be omitted or misplaced, even when "safe" functions are used:
