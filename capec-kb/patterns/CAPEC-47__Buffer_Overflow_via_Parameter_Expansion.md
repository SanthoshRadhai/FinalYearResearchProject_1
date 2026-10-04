# CAPEC-47: Buffer Overflow via Parameter Expansion

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/47.html  

## Description
In this attack, the target software is given input that the adversary knows will be modified and expanded in size during processing. This attack relies on the target software failing to anticipate that the expanded data may exceed some internal limit, thereby creating a buffer overflow.

## Related Attack Patterns
- ChildOf: CAPEC-100

## Prerequisites
- The program expands one of the parameters passed to a function with input controlled by the user, but a later function making use of the expanded parameter erroneously considers the original, not the expanded size of the parameter.
- The expanded parameter is used in the context where buffer overflow may become possible due to the incorrect understanding of the parameter size (i.e. thinking that it is smaller than it really is).

## Skills Required
- [High] Finding this particular buffer overflow may not be trivial. Also, stack and especially heap based buffer overflows require a lot of knowledge if the intended goal is arbitrary code execution. Not only that the adversary needs to write the shell code to accomplish their goals, but the adversary also needs to find a way to get the program execution to jump to the planted shell code. There also needs to be sufficient room for the payload. So not every buffer overflow will be exploitable, even by a skilled adversary.

## Resources Required
- Access to the program source or binary. If the program is only available in binary then a disassembler and other reverse engineering tools will be helpful.

## Consequences
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges
- Scope: Availability; Impact: Unreliable Execution
- Scope: Integrity; Impact: Modify Data
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands
- Scope: Confidentiality; Impact: Read Data

## Mitigations
- Ensure that when parameter expansion happens in the code that the assumptions used to determine the resulting size of the parameter are accurate and that the new size of the parameter is visible to the whole system

## Related Weaknesses (CWE)
- CWE-120
- CWE-119
- CWE-118
- CWE-130
- CWE-131
- CWE-74
- CWE-20
- CWE-680
- CWE-697
