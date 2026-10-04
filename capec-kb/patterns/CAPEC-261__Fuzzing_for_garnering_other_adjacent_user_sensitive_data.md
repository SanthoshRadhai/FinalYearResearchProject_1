# CAPEC-261: Fuzzing for garnering other adjacent user/sensitive data

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/261.html  

## Description
An adversary who is authorized to send queries to a target sends variants of expected queries in the hope that these modified queries might return information (directly or indirectly through error logs) beyond what the expected set of queries should provide.

## Related Attack Patterns
- ChildOf: CAPEC-54

## Prerequisites
- The server must assume that the queries it receives follow specific templates and/or have fields or attributes that follow specific procedures. The server must process queries that it receives without adequately checking or sanitizing queries to ensure they follow these templates.

## Resources Required
- The attacker must have sufficient privileges to send queries to the targeted server. A normal client might limit the nature of these queries, so the attacker must either have a modified client or their own application which allows them to modify the expected queries.

## Related Weaknesses (CWE)
- CWE-20
