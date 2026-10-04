# CWE-767: Access to Critical Private Variable via Public Method

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/767.html  

## Description
The product defines a public method that reads or modifies a private variable.

## Extended Description
If an attacker modifies the variable to contain unexpected values, this could violate assumptions from other parts of the code. Additionally, if an attacker can read the private variable, it may expose sensitive information or make it easier to launch further attacks.

## Related Weaknesses
- ChildOf: CWE-668

## Common Consequences
- Scope: Integrity, Other; Impact: Modify Application Data, Other

## Potential Mitigations
- [Implementation] Use class accessor and mutator methods appropriately. Perform validation when accepting data from a public method that is intended to modify a critical private variable. Also be sure that appropriate access controls are being applied when a public method interfaces with critical data.

## Demonstrative Examples (summary)
- The following example declares a critical variable to be private, and then allows the variable to be modified by public methods.
- The following example could be used to implement a user forum where a single user (UID) can switch between multiple profiles (PID).
