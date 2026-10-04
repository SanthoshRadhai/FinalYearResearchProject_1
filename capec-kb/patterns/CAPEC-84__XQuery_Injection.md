# CAPEC-84: XQuery Injection

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** Very High  
**Reference:** https://capec.mitre.org/data/definitions/84.html  

## Description
This attack utilizes XQuery to probe and attack server systems; in a similar manner that SQL Injection allows an attacker to exploit SQL calls to RDBMS, XQuery Injection uses improperly validated data that is passed to XQuery commands to traverse and execute commands that the XQuery routines have access to. XQuery injection can be used to enumerate elements on the victim's environment, inject commands to the local host, or execute queries to remote files and data sources.

## Related Attack Patterns
- ChildOf: CAPEC-250

## Prerequisites
- The XQL must execute unvalidated data

## Skills Required
- [Low] Basic understanding of XQuery

## Consequences
- Scope: Integrity; Impact: Modify Data
- Scope: Confidentiality; Impact: Read Data
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands

## Mitigations
- Design: Perform input allowlist validation on all XML input
- Implementation: Run xml parsing and query infrastructure with minimal privileges so that an attacker is limited in their ability to probe other system resources from XQL.

## Related Weaknesses (CWE)
- CWE-74
- CWE-707
