# CWE-462: Duplicate Key in Associative List (Alist)

**Abstraction:** Variant  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/462.html  

## Description
Duplicate keys in associative lists can lead to non-unique keys being mistaken for an error.

## Extended Description
A duplicate key entry -- if the alist is designed properly -- could be used as a constant time replace function. However, duplicate key entries could be inserted by mistake. Because of this ambiguity, duplicate key entries in an association list are not recommended and should not be allowed.

## Related Weaknesses
- ChildOf: CWE-694

## Common Consequences
- Scope: Other; Impact: Quality Degradation, Varies by Context

## Potential Mitigations
- [Architecture and Design] Use a hash table instead of an alist.
- [Architecture and Design] Use an alist which checks the uniqueness of hash keys with each entry before inserting the entry.

## Demonstrative Examples (summary)
- The following code adds data to a list and then attempts to sort the data.
