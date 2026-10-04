# CWE-447: Unimplemented or Unsupported Feature in UI

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/447.html  

## Description
A UI function for a security feature appears to be supported and gives feedback to the user that suggests that it is supported, but the underlying functionality is not implemented.

## Related Weaknesses
- ChildOf: CWE-446
- ChildOf: CWE-671

## Common Consequences
- Scope: Other; Impact: Varies by Context, Unexpected State

## Potential Mitigations
- [Testing] Perform functionality testing before deploying the application.
