# CWE-181: Incorrect Behavior Order: Validate Before Filter

**Abstraction:** Variant  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/181.html  

## Description
The product validates data before it has been filtered, which prevents the product from detecting data that becomes invalid after the filtering step.

## Extended Description
This can be used by an attacker to bypass the validation and launch attacks that expose weaknesses that would otherwise be prevented, such as injection.

## Related Weaknesses
- ChildOf: CWE-179

## Common Consequences
- Scope: Access Control; Impact: Bypass Protection Mechanism

## Potential Mitigations
- [Implementation, Architecture and Design] Inputs should be decoded and canonicalized to the application's current internal representation before being filtered.

## Demonstrative Examples (summary)
- This script creates a subdirectory within a user directory and sets the user as the owner.
