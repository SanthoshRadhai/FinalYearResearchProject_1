# CWE-655: Insufficient Psychological Acceptability

**Abstraction:** Class  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/655.html  

## Description
The product has a protection mechanism that is too difficult or inconvenient to use, encouraging non-malicious users to disable or bypass the mechanism, whether by accident or on purpose.

## Related Weaknesses
- ChildOf: CWE-657
- ChildOf: CWE-693

## Common Consequences
- Scope: Access Control; Impact: Bypass Protection Mechanism — By bypassing the security mechanism, a user might leave the system in a less secure state than intended by the administrator, making it more susceptible to compromise.

## Potential Mitigations
- [Testing] Where possible, perform human factors and usability studies to identify where your product's security mechanisms are difficult to use, and why.
- [Architecture and Design] Make the security mechanism as seamless as possible, while also providing the user with sufficient details when a security decision produces unexpected results.

## Demonstrative Examples (summary)
- In "Usability of Security: A Case Study" [REF-540], the authors consider human factors in a cryptography product. Some of the weakness relevant discoveries of this case study were: users accidentally leaked sensitive information, could not figure out how to perform some tasks, thought they were enabling a security option when they were not, and made improper trust decisions.
- Enforcing complex and difficult-to-remember passwords that need to be frequently changed for access to trivial resources, e.g., to use a black-and-white printer. Complex password requirements can also cause users to store the passwords in an unsafe manner so they don't have to remember them, such as using a sticky note or saving them in an unencrypted file.
- Some CAPTCHA utilities produce images that are too difficult for a human to read, causing user frustration.
