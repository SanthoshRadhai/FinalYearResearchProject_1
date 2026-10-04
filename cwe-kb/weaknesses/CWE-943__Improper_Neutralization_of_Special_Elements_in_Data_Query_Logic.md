# CWE-943: Improper Neutralization of Special Elements in Data Query Logic

**Abstraction:** Class  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/943.html  

## Description
The product generates a query intended to access or manipulate data in a data store such as a database, but it does not neutralize or incorrectly neutralizes special elements that can modify the intended logic of the query.

## Extended Description
Depending on the capabilities of the query language, an attacker could inject additional logic into the query to: Modify the intended selection criteria, thus changing which data entities (e.g., records) are returned, modified, or otherwise manipulated Append additional commands to the query Return more entities than intended Return fewer entities than intended Cause entities to be sorted in an unexpected way The ability to execute additional commands or change which entities are returned has obvious risks. But when the product logic depends on the order or number of entities, this can also lead to vulnerabilities. For example, if the query expects to return only one entity that specifies an administrative user, but an attacker can change which entities are returned, this could cause the logic to return information for a regular user and incorrectly assume that the user has administrative privileges. While this weakness is most commonly associated with SQL injection, there are many other query languages that are also subject to injection attacks, including HTSQL, LDAP, DQL, XQuery, Xpath, and "NoSQL" languages.

## Related Weaknesses
- ChildOf: CWE-74

## Common Consequences
- Scope: Confidentiality, Integrity, Availability, Access Control; Impact: Bypass Protection Mechanism, Read Application Data, Modify Application Data, Varies by Context

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- The following code dynamically constructs and executes a SQL query that searches for items matching a specified name. The query restricts the items displayed to those where owner matches the user name of the currently-authenticated user.
- The code below constructs an LDAP query using user input address data:
- Consider the following simple XML document that stores authentication information and a snippet of Java code that uses XPath query to retrieve authentication information:
