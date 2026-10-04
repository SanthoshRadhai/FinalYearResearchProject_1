# CWE-107: Struts: Unused Validation Form

**Abstraction:** Variant  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/107.html  

## Description
An unused validation form indicates that validation logic is not up-to-date.

## Related Weaknesses
- ChildOf: CWE-1164
- ChildOf: CWE-20

## Common Consequences
- Scope: Other; Impact: Quality Degradation

## Potential Mitigations
- [Implementation] Remove the unused Validation Form from the validation.xml file.

## Demonstrative Examples (summary)
- In the following example the class RegistrationForm is a Struts framework ActionForm Bean that will maintain user input data from a registration webpage for an online business site. The user will enter registration data and, through the Struts framework, the RegistrationForm bean will maintain the user data in the form fields using the private member variables. The RegistrationForm class uses the Struts validation capability by extending the ValidatorForm class and including the validation for the form fields within the validator XML file, validator.xml.
