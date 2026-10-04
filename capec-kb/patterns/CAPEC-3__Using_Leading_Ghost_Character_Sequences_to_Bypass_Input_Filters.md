# CAPEC-3: Using Leading 'Ghost' Character Sequences to Bypass Input Filters

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Medium  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/3.html  

## Description
Some APIs will strip certain leading characters from a string of parameters. An adversary can intentionally introduce leading "ghost" characters (extra characters that don't affect the validity of the request at the API layer) that enable the input to pass the filters and therefore process the adversary's input. This occurs when the targeted API will accept input data in several syntactic forms and interpret it in the equivalent semantic way, while the filter does not take into account the full spectrum of the syntactic forms acceptable to the targeted API.

## Related Attack Patterns
- ChildOf: CAPEC-267

## Prerequisites
- The targeted API must ignore the leading ghost characters that are used to get past the filters for the semantics to be the same.

## Skills Required
- [Medium] The ability to make an API request, and knowledge of "ghost" characters that will not be filtered by any input validation. These "ghost" characters must be known to not affect the way in which the request will be interpreted.

## Consequences
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges
- Scope: Integrity; Impact: Modify Data

## Mitigations
- Use an allowlist rather than a denylist input validation.
- Canonicalize all data prior to validation.
- Take an iterative approach to input validation (defense in depth).

## Related Weaknesses (CWE)
- CWE-173
- CWE-41
- CWE-172
- CWE-179
- CWE-180
- CWE-181
- CWE-183
- CWE-184
- CWE-20
- CWE-74
- CWE-697
- CWE-707
