# CWE-1037: Processor Optimization Removal or Modification of Security-critical Code

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/1037.html  

## Description
The developer builds a security-critical protection mechanism into the software, but the processor optimizes the execution of the program such that the mechanism is removed or modified.

## Related Weaknesses
- ChildOf: CWE-1038

## Common Consequences
- Scope: Integrity; Impact: Bypass Protection Mechanism — A successful exploitation of this weakness will change the order of an application's execution and will likely be used to bypass specific protection mechanisms. This bypass can be exploited further to potentially read data that should otherwise be unaccessible.

## Detection Methods
- [White Box] In theory this weakness can be detected through the use of white box testing techniques where specifically crafted test cases are used in conjunction with debuggers to verify the order of statements being executed.
