# CWE-258: Empty Password in Configuration File

**Abstraction:** Variant  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/258.html  

## Description
Using an empty string as a password is insecure.

## Related Weaknesses
- ChildOf: CWE-260
- ChildOf: CWE-521

## Common Consequences
- Scope: Access Control; Impact: Gain Privileges or Assume Identity

## Potential Mitigations
- [System Configuration] Passwords should be at least eight characters long -- the longer the better. Avoid passwords that are in any way similar to other passwords you have. Avoid using words that may be found in a dictionary, names book, on a map, etc. Consider incorporating numbers and/or punctuation into your password. If you do use common words, consider replacing letters in that word with numbers and punctuation. However, do not use "similar-looking" punctuation. For example, it is not a good idea to change cat to c@t, ca+, (@+, or anything similar. Finally, it is never appropriate to use an empty string as a password.

## Demonstrative Examples (summary)
- The following examples show a portion of properties and configuration files for Java and ASP.NET applications. The files include username and password information but the password is provided as an empty string.
