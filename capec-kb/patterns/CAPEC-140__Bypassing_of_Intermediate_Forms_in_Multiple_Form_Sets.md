# CAPEC-140: Bypassing of Intermediate Forms in Multiple-Form Sets

**Abstraction:** Standard  
**Status:** Draft  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/140.html  

## Description
Some web applications require users to submit information through an ordered sequence of web forms. This is often done if there is a very large amount of information being collected or if information on earlier forms is used to pre-populate fields or determine which additional information the application needs to collect. An attacker who knows the names of the various forms in the sequence may be able to explicitly type in the name of a later form and navigate to it without first going through the previous forms. This can result in incomplete collection of information, incorrect assumptions about the information submitted by the attacker, or other problems that can impair the functioning of the application.

## Related Attack Patterns
- ChildOf: CAPEC-74

## Prerequisites
- The target must collect information from the user in a series of forms where each form has its own URL that the attacker can anticipate and the application must fail to detect attempts to access intermediate forms without first filling out the previous forms.

## Resources Required
- None: No specialized resources are required to execute this type of attack.

## Related Weaknesses (CWE)
- CWE-372
