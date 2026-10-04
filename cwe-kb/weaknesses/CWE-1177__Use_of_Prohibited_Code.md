# CWE-1177: Use of Prohibited Code

**Abstraction:** Class  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/1177.html  

## Description
The product uses a function, library, or third party component that has been explicitly prohibited, whether by the developer or the customer.

## Extended Description
The developer - or customers - may wish to restrict or eliminate use of a function, library, or third party component for any number of reasons, including real or suspected vulnerabilities; difficulty to use securely; export controls or license requirements; obsolete or poorly-maintained code; internal code being scheduled for deprecation; etc. To reduce risk of vulnerabilities, the developer might maintain a list of "banned" functions that programmers must avoid using because the functions are difficult or impossible to use securely. This issue can also make the product more costly and difficult to maintain.

## Related Weaknesses
- ChildOf: CWE-710

## Common Consequences
- Scope: Other; Impact: Reduce Maintainability

## Potential Mitigations
- [Build and Compilation, Implementation] Identify a list of prohibited API functions and prohibit developers from using these functions, providing safer alternatives. In some cases, automatic code analysis tools or the compiler can be instructed to spot use of prohibited functions, such as the "banned.h" include file from Microsoft's SDL. [REF-554] [REF-1009] [REF-7]

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- The code below calls the gets() function to read in data from the command line.
- The following code attempts to create a local copy of a buffer to perform some manipulations to the data.
