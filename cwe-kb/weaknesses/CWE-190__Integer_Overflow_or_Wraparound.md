# CWE-190: Integer Overflow or Wraparound

**Abstraction:** Base  
**Status:** Stable  
**Reference:** https://cwe.mitre.org/data/definitions/190.html  

## Description
The product performs a calculation that can produce an integer overflow or wraparound when the logic assumes that the resulting value will always be larger than the original value. This occurs when an integer value is incremented to a value that is too large to store in the associated representation. When this occurs, the value may become a very small or negative number.

## Related Weaknesses
- ChildOf: CWE-682
- ChildOf: CWE-682
- ChildOf: CWE-20
- CanPrecede: CWE-119

## Common Consequences
- Scope: Availability; Impact: DoS: Crash, Exit, or Restart, DoS: Resource Consumption (Memory), DoS: Instability — This weakness can generally lead to undefined behavior and therefore crashes. When the calculated result is used for resource allocation, this weakness can cause too many (or too few) resources to be allocated, possibly enabling crashes if the product requests more resources than can be provided.
- Scope: Integrity; Impact: Modify Memory — If the value in question is important to data (as opposed to flow), simple data corruption has occurred. Also, if the overflow/wraparound results in other conditions such as buffer overflows, further memory corruption may occur.
- Scope: Confidentiality, Availability, Access Control; Impact: Execute Unauthorized Code or Commands, Bypass Protection Mechanism — This weakness can sometimes trigger buffer overflows, which can be used to execute arbitrary code. This is usually outside the scope of the product's implicit security policy.
- Scope: Availability, Other; Impact: Alter Execution Logic, DoS: Crash, Exit, or Restart, DoS: Resource Consumption (CPU) — If the overflow/wraparound occurs in a loop index variable, this could cause the loop to terminate at the wrong time - too early, too late, or not at all (i.e., infinite loops). With too many iterations, some loops could consume too many resources such as memory, file handles, etc., possibly leading to a crash or other DoS.
- Scope: Access Control; Impact: Bypass Protection Mechanism — If integer values are used in security-critical decisions, such as calculating quotas or allocation limits, integer overflows can be used to cause an incorrect security decision.

## Potential Mitigations
- [Requirements] Ensure that all protocols are strictly defined, such that all out-of-bounds behavior can be identified simply, and require strict conformance to the protocol.
- [Requirements] Use a language that does not allow this weakness to occur or provides constructs that make this weakness easier to avoid. If possible, choose a language or compiler that performs automatic bounds checking.
- [Architecture and Design] Use a vetted library or framework that does not allow this weakness to occur or provides constructs that make this weakness easier to avoid [REF-1482]. Use libraries or frameworks that make it easier to handle numbers without unexpected consequences. Examples include safe integer handling packages such as SafeInt (C++) or IntegerLib (C or C++). [REF-106]
- [Implementation] Perform input validation on any numeric input by ensuring that it is within the expected range. Enforce that the input meets both the minimum and maximum requirements for the expected range. Use unsigned integers where possible. This makes it easier to perform validation for integer overflows. When signed integers are required, ensure that the range check includes minimum values as well as maximum values.
- [Implementation] Understand the programming language's underlying representation and how it interacts with numeric calculation (CWE-681). Pay close attention to byte size discrepancies, precision, signed/unsigned distinctions, truncation, conversion and casting between types, "not-a-number" calculations, and how the language handles numbers that are too large or too small for its underlying representation. [REF-7] Also be careful to account for 32-bit, 64-bit, and other potential differences that may affect the numeric representation.
- [Architecture and Design] For any security checks that are performed on the client side, ensure that these checks are duplicated on the server side, in order to avoid CWE-602. Attackers can bypass the client-side checks by modifying values after the checks have been performed, or by changing the client to remove the client-side checks entirely. Then, these modified values would be submitted to the server.
- [Implementation] Examine compiler warnings closely and eliminate problems with potential security implications, such as signed / unsigned mismatch in memory operations, or use of uninitialized variables. Even if the weakness is rarely exploitable, a single failure may lead to the compromise of the entire system.

## Detection Methods
- [Automated Static Analysis] This weakness can often be detected using automated static analysis tools. Many modern tools use data flow analysis or constraint-based techniques to minimize the number of false positives.
- [Black Box] Sometimes, evidence of this weakness can be detected using dynamic tools and techniques that interact with the product using large test suites with many diverse inputs, such as fuzz testing (fuzzing), robustness testing, and fault injection. The product's operation may slow down, but it should not become unstable, crash, or generate incorrect results.
- [Manual Analysis] This weakness can be detected using tools and techniques that require manual (human) analysis, such as penetration testing, threat modeling, and interactive tools that allow the tester to record and modify an active session. Specifically, manual static analysis is useful for evaluating the correctness of allocation calculations. This can be useful for detecting overflow conditions (CWE-190) or similar weaknesses that might have serious security impacts on the program.
- [Automated Static Analysis - Binary or Bytecode] According to SOAR [REF-1479], the following detection techniques may be useful: Highly cost effective: Bytecode Weakness Analysis - including disassembler + source code weakness analysis Binary Weakness Analysis - including disassembler + source code weakness analysis
- [Dynamic Analysis with Manual Results Interpretation] According to SOAR [REF-1479], the following detection techniques may be useful: Cost effective for partial coverage: Fuzz Tester Framework-based Fuzzer
- [Manual Static Analysis - Source Code] According to SOAR [REF-1479], the following detection techniques may be useful: Cost effective for partial coverage: Manual Source Code Review (not inspections)
- [Automated Static Analysis - Source Code] According to SOAR [REF-1479], the following detection techniques may be useful: Highly cost effective: Source code Weakness Analyzer Context-configured Source Code Weakness Analyzer
- [Architecture or Design Review] According to SOAR [REF-1479], the following detection techniques may be useful: Highly cost effective: Formal Methods / Correct-By-Construction Cost effective for partial coverage: Inspection (IEEE 1028 standard) (can apply to requirements, design, source code, etc.)

## Demonstrative Examples (summary)
- The following image processing code allocates a table for images.
- The following code excerpt from OpenSSH 3.3 demonstrates a classic case of integer overflow:
- Integer overflows can be complicated and difficult to detect. The following example is an attempt to show how an integer overflow may lead to undefined looping behavior:
- In this example the method determineFirstQuarterRevenue is used to determine the first quarter revenue for an accounting/business application. The method retrieves the monthly sales totals for the first three months of the year, calculates the first quarter sales totals from the monthly sales totals, calculates the first quarter revenue based on the first quarter sales, and finally saves the first quarter revenue results to the database.
