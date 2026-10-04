# CWE-766: Critical Data Element Declared Public

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/766.html  

## Description
The product declares a critical variable, field, or member to be public when intended security policy requires it to be private.

## Extended Description
This issue makes it more difficult to maintain the product, which indirectly affects security by making it more difficult or time-consuming to find and/or fix vulnerabilities. It also might make it easier to introduce vulnerabilities.

## Related Weaknesses
- ChildOf: CWE-732
- ChildOf: CWE-1061

## Common Consequences
- Scope: Integrity, Confidentiality; Impact: Read Application Data, Modify Application Data — Making a critical variable public allows anyone with access to the object in which the variable is contained to alter or read the value.
- Scope: Other; Impact: Reduce Maintainability

## Potential Mitigations
- [Implementation] Data should be private, static, and final whenever possible. This will assure that your code is protected by instantiating early, preventing access, and preventing tampering.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- The following example declares a critical variable public, making it accessible to anyone with access to the object in which it is contained.
- The following example shows a basic user account class that includes member variables for the username and password as well as a public constructor for the class and a public method to authorize access to the user account.
