# CWE-532: Insertion of Sensitive Information into Log File

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/532.html  

## Description
The product writes sensitive information to a log file.

## Related Weaknesses
- ChildOf: CWE-538
- ChildOf: CWE-200

## Common Consequences
- Scope: Confidentiality; Impact: Read Application Data — Logging sensitive user data, full path names, or system information often provides attackers with an additional, less-protected path to acquiring the information.

## Potential Mitigations
- [Architecture and Design, Implementation] Consider seriously the sensitivity of the information written into log files. Do not write secrets into the log files.
- [Distribution] Remove debug log files before deploying the application into production.
- [Operation] Protect log files against unauthorized read/write.
- [Implementation] Adjust configurations appropriately when software is transitioned from a debug state to production.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- In the following code snippet, a user's full name and credit card number are written to a log file.
- This code stores location information about the current user:
- In the example below, the method getUserBankAccount retrieves a bank account object from a database using the supplied username and account number to query the database. If an SQLException is raised when querying the database, an error message is created and output to a log file.
