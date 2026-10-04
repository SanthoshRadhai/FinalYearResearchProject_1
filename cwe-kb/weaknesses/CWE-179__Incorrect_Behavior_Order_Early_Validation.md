# CWE-179: Incorrect Behavior Order: Early Validation

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/179.html  

## Description
The product validates input before applying protection mechanisms that modify the input, which could allow an attacker to bypass the validation via dangerous inputs that only arise after the modification.

## Extended Description
Product needs to validate data at the proper time, after data has been canonicalized and cleansed. Early validation is susceptible to various manipulations that result in dangerous inputs that are produced by canonicalization and cleansing.

## Related Weaknesses
- ChildOf: CWE-20
- ChildOf: CWE-696

## Common Consequences
- Scope: Access Control, Integrity; Impact: Bypass Protection Mechanism, Execute Unauthorized Code or Commands — An attacker could include dangerous input that bypasses validation protection mechanisms which can be used to launch various attacks including injection attacks, execute arbitrary code or cause other unintended behavior.

## Potential Mitigations
- [Implementation] Inputs should be decoded and canonicalized to the application's current internal representation before being validated (CWE-180). Make sure that the application does not decode the same input twice (CWE-174). Such errors could be used to bypass allowlist validation schemes by introducing dangerous inputs after they have been checked.

## Demonstrative Examples (summary)
- The following code attempts to validate a given input path by checking it against an allowlist and then return the canonical path. In this specific case, the path is considered valid if it starts with the string "/safe_dir/".
- This script creates a subdirectory within a user directory and sets the user as the owner.
