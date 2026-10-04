# CWE-628: Function Call with Incorrectly Specified Arguments

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/628.html  

## Description
The product calls a function, procedure, or routine with arguments that are not correctly specified, leading to always-incorrect behavior and resultant weaknesses.

## Extended Description
There are multiple ways in which this weakness can be introduced, including: the wrong variable or reference; an incorrect number of arguments; incorrect order of arguments; wrong type of arguments; or wrong value.

## Related Weaknesses
- ChildOf: CWE-573

## Common Consequences
- Scope: Other, Access Control; Impact: Quality Degradation, Gain Privileges or Assume Identity — This weakness can cause unintended behavior and can lead to additional weaknesses such as allowing an attacker to gain unintended access to system resources.

## Potential Mitigations
- [Build and Compilation] Once found, these issues are easy to fix. Use code inspection tools and relevant compiler features to identify potential violations. Pay special attention to code that is not likely to be exercised heavily during QA.
- [Architecture and Design] Make sure your API's are stable before you use them in production code.

## Detection Methods
- [Other] Since these bugs typically introduce incorrect behavior that is obvious to users, they are found quickly, unless they occur in rarely-tested code paths. Managing the correct number of arguments can be made more difficult in cases where format strings are used, or when variable numbers of arguments are supported.

## Demonstrative Examples (summary)
- The following PHP method authenticates a user given a username/password combination but is called with the parameters in reverse order.
- This Perl code intends to record whether a user authenticated successfully or not, and to exit if the user fails to authenticate. However, when it calls ReportAuth(), the third argument is specified as 0 instead of 1, so it does not exit.
- In the following Java snippet, the accessGranted() method is accidentally called with the static ADMIN_ROLES array rather than the user roles.
