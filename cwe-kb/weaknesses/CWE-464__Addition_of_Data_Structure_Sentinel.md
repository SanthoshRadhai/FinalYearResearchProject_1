# CWE-464: Addition of Data Structure Sentinel

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/464.html  

## Description
The accidental addition of a data-structure sentinel can cause serious programming logic problems.

## Extended Description
Data-structure sentinels are often used to mark the structure of data. A common example of this is the null character at the end of strings or a special sentinel to mark the end of a linked list. It is dangerous to allow this type of control data to be easily accessible. Therefore, it is important to protect from the addition or modification of sentinels.

## Related Weaknesses
- ChildOf: CWE-138

## Common Consequences
- Scope: Integrity; Impact: Modify Application Data — Generally this error will cause the data structure to not work properly by truncating the data.

## Potential Mitigations
- [Implementation, Architecture and Design] Encapsulate the user from interacting with data sentinels. Validate user input to verify that sentinels are not present.
- [Implementation] Proper error checking can reduce the risk of inadvertently introducing sentinel values into data. For example, if a parsing function fails or encounters an error, it might return a value that is the same as the sentinel.
- [Architecture and Design] Use an abstraction library to abstract away risky APIs. This is not a complete solution.
- [Operation] Use OS-level preventative functionality. This is not a complete solution.

## Demonstrative Examples (summary)
- The following example assigns some character values to a list of characters and prints them each individually, and then as a string. The third character value is intended to be an integer taken from user input and converted to an int. The first print statement will print each character separated by a space.
