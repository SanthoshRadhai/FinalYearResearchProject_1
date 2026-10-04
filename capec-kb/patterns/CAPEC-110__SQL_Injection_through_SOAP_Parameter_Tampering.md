# CAPEC-110: SQL Injection through SOAP Parameter Tampering

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** Very High  
**Reference:** https://capec.mitre.org/data/definitions/110.html  

## Description
An attacker modifies the parameters of the SOAP message that is sent from the service consumer to the service provider to initiate a SQL injection attack. On the service provider side, the SOAP message is parsed and parameters are not properly validated before being used to access a database in a way that does not use parameter binding, thus enabling the attacker to control the structure of the executed SQL query. This pattern describes a SQL injection attack with the delivery mechanism being a SOAP message.

## Related Attack Patterns
- ChildOf: CAPEC-66
- CanPrecede: CAPEC-108

## Prerequisites
- SOAP messages are used as a communication mechanism in the system
- SOAP parameters are not properly validated at the service provider
- The service provider does not properly utilize parameter binding when building SQL queries

## Skills Required
- [Medium] If the attacker is able to gain good understanding of the system's database schema
- [High] If the attacker has to perform Blind SQL Injection

## Resources Required
- None: No specialized resources are required to execute this type of attack.

## Consequences
- Scope: Integrity; Impact: Modify Data
- Scope: Availability; Impact: Unreliable Execution
- Scope: Confidentiality; Impact: Read Data
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands

## Mitigations
- Properly validate and sanitize/reject user input at the service provider.
- Ensure that prepared statements or other mechanism that enables parameter binding is used when accessing the database in a way that would prevent the attackers' supplied data from controlling the structure of the executed query.
- At the database level, ensure that the database user used by the application in a particular context has the minimum needed privileges to the database that are needed to perform the operation. When possible, run queries against pre-generated views rather than the tables directly.

## Related Weaknesses (CWE)
- CWE-89
- CWE-20
