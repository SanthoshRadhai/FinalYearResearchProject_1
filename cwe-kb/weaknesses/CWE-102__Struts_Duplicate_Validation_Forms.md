# CWE-102: Struts: Duplicate Validation Forms

**Abstraction:** Variant  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/102.html  

## Description
The product uses multiple validation forms with the same name, which might cause the Struts Validator to validate a form that the programmer does not expect.

## Extended Description
If two validation forms have the same name, the Struts Validator arbitrarily chooses one of the forms to use for input validation and discards the other. This decision might not correspond to the programmer's expectations, possibly leading to resultant weaknesses. Moreover, it indicates that the validation logic is not up-to-date, and can indicate that other, more subtle validation errors are present.

## Related Weaknesses
- ChildOf: CWE-694
- ChildOf: CWE-1173
- ChildOf: CWE-20

## Common Consequences
- Scope: Integrity; Impact: Unexpected State

## Potential Mitigations
- [Implementation] The DTD or schema validation will not catch the duplicate occurrence of the same form name. To find the issue in the implementation, manual checks or automated static analysis could be applied to the xml configuration files.

## Demonstrative Examples (summary)
- These two Struts validation forms have the same name.
