# CWE-103: Struts: Incomplete validate() Method Definition

**Abstraction:** Variant  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/103.html  

## Description
The product has a validator form that either does not define a validate() method, or defines a validate() method but does not call super.validate().

## Related Weaknesses
- ChildOf: CWE-573
- ChildOf: CWE-20

## Common Consequences
- Scope: Other; Impact: Unexpected State, Varies by Context — If the code does not call super.validate(), the Validation Framework cannot check the contents of the form against a validation form. In other words, the validation framework will be disabled for the given form. Disabling the validation framework for a form exposes the product to numerous types of attacks.
- Scope: Confidentiality, Integrity, Availability, Other; Impact: Other — Although J2EE applications are not generally susceptible to memory corruption attacks, if a J2EE application interfaces with native code that does not perform array bounds checking, an attacker may be able to use an input validation mistake in the J2EE application to launch a buffer overflow attack.

## Potential Mitigations
- [Implementation] Implement the validate() method and call super.validate() within that method.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- In the following Java example the class RegistrationForm is a Struts framework ActionForm Bean that will maintain user input data from a registration webpage for an online business site. The user will enter registration data and the RegistrationForm bean in the Struts framework will maintain the user data. Tthe RegistrationForm class implements the validate method to validate the user input entered into the form.
