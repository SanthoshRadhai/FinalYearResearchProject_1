# CWE-184: Incomplete List of Disallowed Inputs

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/184.html  

## Description
The product implements a protection mechanism that relies on a list of inputs (or properties of inputs) that are not allowed by policy or otherwise require other action to neutralize before additional processing takes place, but the list is incomplete.

## Related Weaknesses
- ChildOf: CWE-693
- ChildOf: CWE-1023
- CanPrecede: CWE-79
- CanPrecede: CWE-78
- CanPrecede: CWE-434
- CanPrecede: CWE-98

## Common Consequences
- Scope: Access Control; Impact: Bypass Protection Mechanism — Attackers may be able to find other malicious inputs that were not expected by the developer, allowing them to bypass the intended protection mechanism.

## Potential Mitigations
- [Implementation] Do not rely exclusively on detecting disallowed inputs. There are too many variants to encode a character, especially when different environments are used, so there is a high likelihood of missing some variants. Only use detection of disallowed inputs as a mechanism for detecting suspicious activity. Ensure that you are using other protection mechanisms that only identify "good" input - such as lists of allowed inputs - and ensure that you are properly encoding your outputs.

## Detection Methods
- [Black Box] Exploitation of a vulnerability with commonly-used manipulations might fail, but minor variations might succeed.

## Demonstrative Examples (summary)
- The following code attempts to stop XSS attacks by removing all occurences of "script" in an input string.
- This example takes user input, passes it through an encoding scheme, then lists the contents of the user's home directory based on the user name.
