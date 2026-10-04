# CWE-457: Use of Uninitialized Variable

**Abstraction:** Variant  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/457.html  

## Description
The code uses a variable that has not been initialized, leading to unpredictable or unintended results.

## Extended Description
In some languages such as C and C++, stack variables are not initialized by default. They generally contain junk data with the contents of stack memory before the function was invoked. An attacker can sometimes control or read these contents. In other languages or conditions, a variable that is not explicitly initialized can be given a default value that has security implications, depending on the logic of the program. The presence of an uninitialized variable can sometimes indicate a typographic error in the code.

## Related Weaknesses
- ChildOf: CWE-908
- ChildOf: CWE-665
- ChildOf: CWE-665

## Common Consequences
- Scope: Availability, Integrity, Other; Impact: Other — Initial variables usually contain junk, which can not be trusted for consistency. This can lead to denial of service conditions, or modify control flow in unexpected ways. In some cases, an attacker can "pre-initialize" the variable using previous actions, which might enable code execution. This can cause a race condition if a lock variable check passes when it should not.
- Scope: Authorization, Other; Impact: Other — Strings that are not initialized are especially dangerous, since many functions expect a null at the end -- and only at the end -- of a string.

## Potential Mitigations
- [Implementation] Ensure that critical variables are initialized before first use [REF-1485].
- [Build and Compilation] Most compilers will complain about the use of uninitialized variables if warnings are turned on.
- [Implementation, Operation] When using a language that does not require explicit declaration of variables, run or compile the software in a mode that reports undeclared or unknown variables. This may indicate the presence of a typographic error in the variable's name.
- [Requirements] Choose a language that is not susceptible to these issues.
- [Architecture and Design] Mitigating technologies such as safe string libraries and container abstractions could be introduced.

## Detection Methods
- [Fuzzing] Fuzz testing (fuzzing) is a powerful technique for generating large numbers of diverse inputs - either randomly or algorithmically - and dynamically invoking the code with those inputs. Even with random inputs, it is often capable of generating unexpected results such as crashes, memory corruption, or resource consumption. Fuzzing effectively produces repeatable test cases that clearly indicate bugs, which helps developers to diagnose the issues.
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- This code prints a greeting using information stored in a POST request:
- The following switch statement is intended to set the values of the variables aN and bN before they are used:
- This example will leave test_string in an unknown condition when i is the same value as err_val, because test_string is not initialized (CWE-456). Depending on where this code segment appears (e.g. within a function body), test_string might be random if it is stored on the heap or stack. If the variable is declared in static memory, it might be zero or NULL. Compiler optimization might contribute to the unpredictability of this address.
