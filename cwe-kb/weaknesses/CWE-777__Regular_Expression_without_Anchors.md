# CWE-777: Regular Expression without Anchors

**Abstraction:** Variant  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/777.html  

## Description
The product uses a regular expression to perform neutralization, but the regular expression is not anchored and may allow malicious or malformed data to slip through.

## Extended Description
When performing tasks such as validating against a set of allowed inputs (allowlist), data is examined and possibly modified to ensure that it is well-formed and adheres to a list of safe values. If the regular expression is not anchored, malicious or malformed data may be included before or after any string matching the regular expression. The type of malicious data that is allowed will depend on the context of the application and which anchors are omitted from the regular expression.

## Related Weaknesses
- ChildOf: CWE-625

## Common Consequences
- Scope: Availability, Confidentiality, Access Control; Impact: Bypass Protection Mechanism — An unanchored regular expression in the context of an allowlist will possibly result in a protection mechanism failure, allowing malicious or malformed data to enter trusted regions of the program. The specific consequences will depend on what functionality the allowlist was protecting.

## Potential Mitigations
- [Implementation] Be sure to understand both what will be matched and what will not be matched by a regular expression. Anchoring the ends of the expression will allow the programmer to define an allowlist strictly limited to what is matched by the text in the regular expression. If you are using a package that only matches one line by default, ensure that you can match multi-line inputs if necessary.

## Demonstrative Examples (summary)
- Consider a web application that supports multiple languages. It selects messages for an appropriate language by using the lang parameter.
- This code uses a regular expression to validate an IP string prior to using it in a call to the "ping" command.
