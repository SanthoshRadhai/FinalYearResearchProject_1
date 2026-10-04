# CWE-566: Authorization Bypass Through User-Controlled SQL Primary Key

**Abstraction:** Variant  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/566.html  

## Description
The product uses a database table that includes records that should not be accessible to an actor, but it executes a SQL statement with a primary key that can be controlled by that actor.

## Extended Description
When a user can set a primary key to any value, then the user can modify the key to point to unauthorized records. Database access control errors occur when: Data enters a program from an untrusted source. The data is used to specify the value of a primary key in a SQL query. The untrusted source does not have the permissions to be able to access all rows in the associated table.

## Related Weaknesses
- ChildOf: CWE-639

## Common Consequences
- Scope: Confidentiality, Integrity, Access Control; Impact: Read Application Data, Modify Application Data, Bypass Protection Mechanism

## Potential Mitigations
- [Implementation] Assume all input is malicious. Use a standard input validation mechanism to validate all input for length, type, syntax, and business rules before accepting the data. Use an "accept known good" validation strategy.
- [Implementation] Use a parameterized query AND make sure that the accepted values conform to the business rules. Construct your SQL statement accordingly.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- The following code uses a parameterized statement, which escapes metacharacters and prevents SQL injection vulnerabilities, to construct and execute a SQL query that searches for an invoice matching the specified identifier [1]. The identifier is selected from a list of all invoices associated with the current authenticated user.
