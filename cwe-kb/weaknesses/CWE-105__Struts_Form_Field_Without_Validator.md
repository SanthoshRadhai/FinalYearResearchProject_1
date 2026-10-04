# CWE-105: Struts: Form Field Without Validator

**Abstraction:** Variant  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/105.html  

## Description
The product has a form field that is not validated by a corresponding validation form, which can introduce other weaknesses related to insufficient input validation.

## Extended Description
Omitting validation for even a single input field may give attackers the leeway they need to compromise the product. Although J2EE applications are not generally susceptible to memory corruption attacks, if a J2EE application interfaces with native code that does not perform array bounds checking, an attacker may be able to use an input validation mistake in the J2EE application to launch a buffer overflow attack.

## Related Weaknesses
- ChildOf: CWE-1173
- ChildOf: CWE-20

## Common Consequences
- Scope: Integrity; Impact: Unexpected State
- Scope: Integrity; Impact: Bypass Protection Mechanism — If unused fields are not validated, shared business logic in an action may allow attackers to bypass the validation checks that are performed for other uses of the form.

## Potential Mitigations
- [Implementation] Validate all form fields. If a field is unused, it is still important to constrain it so that it is empty or undefined.

## Demonstrative Examples (summary)
- In the following example the Java class RegistrationForm is a Struts framework ActionForm Bean that will maintain user input data from a registration webpage for an online business site. The user will enter registration data and, through the Struts framework, the RegistrationForm bean will maintain the user data in the form fields using the private member variables. The RegistrationForm class uses the Struts validation capability by extending the ValidatorForm class and including the validation for the form fields within the validator XML file, validator.xml.
