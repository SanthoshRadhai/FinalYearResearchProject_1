# CWE-180: Incorrect Behavior Order: Validate Before Canonicalize

**Abstraction:** Variant  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/180.html  

## Description
The product validates input before it is canonicalized, which prevents the product from detecting data that becomes invalid after the canonicalization step.

## Extended Description
This can be used by an attacker to bypass the validation and launch attacks that expose weaknesses that would otherwise be prevented, such as injection.

## Related Weaknesses
- ChildOf: CWE-179

## Common Consequences
- Scope: Access Control; Impact: Bypass Protection Mechanism

## Potential Mitigations
- [Implementation] Inputs should be decoded and canonicalized to the application's current internal representation before being validated (CWE-180). Make sure that the application does not decode the same input twice (CWE-174). Such errors could be used to bypass allowlist validation schemes by introducing dangerous inputs after they have been checked.

## Demonstrative Examples (summary)
- The following code attempts to validate a given input path by checking it against an allowlist and then return the canonical path. In this specific case, the path is considered valid if it starts with the string "/safe_dir/".
