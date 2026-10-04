# CAPEC-540: Overread Buffers

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/540.html  

## Description
An adversary attacks a target by providing input that causes an application to read beyond the boundary of a defined buffer. This typically occurs when a value influencing where to start or stop reading is set to reflect positions outside of the valid memory location of the buffer. This type of attack may result in exposure of sensitive information, a system crash, or arbitrary code execution.

## Related Attack Patterns
- ChildOf: CAPEC-123

## Prerequisites
- For this type of attack to be successful, a few prerequisites must be met. First, the targeted software must be written in a language that enables fine grained buffer control. (e.g., c, c++) Second, the targeted software must actually perform buffer operations and inadequately perform bounds-checking on those buffer operations. Finally, the adversary must have the capability to influence the input that guides these buffer operations.

## Consequences
- Scope: Confidentiality; Impact: Read Data
- Scope: Availability; Impact: Unreliable Execution

## Related Weaknesses (CWE)
- CWE-125
