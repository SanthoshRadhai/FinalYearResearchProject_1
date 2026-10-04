# CAPEC-136: LDAP Injection

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/136.html  

## Description
An attacker manipulates or crafts an LDAP query for the purpose of undermining the security of the target. Some applications use user input to create LDAP queries that are processed by an LDAP server. For example, a user might provide their username during authentication and the username might be inserted in an LDAP query during the authentication process. An attacker could use this input to inject additional commands into an LDAP query that could disclose sensitive information. For example, entering a * in the aforementioned query might return information about all users on the system. This attack is very similar to an SQL injection attack in that it manipulates a query to gather additional information or coerce a particular return value.

## Related Attack Patterns
- ChildOf: CAPEC-248

## Prerequisites
- The target application must accept a string as user input, fail to sanitize characters that have a special meaning in LDAP queries in the user input, and insert the user-supplied string in an LDAP query which is then processed.

## Skills Required
- [Medium] The attacker needs to have knowledge of LDAP, especially its query syntax.

## Consequences
- Scope: Availability; Impact: Unreliable Execution
- Scope: Integrity; Impact: Modify Data
- Scope: Confidentiality; Impact: Read Data
- Scope: Authorization; Impact: Execute Unauthorized Commands
- Scope: Accountability, Authentication, Authorization, Non-Repudiation; Impact: Gain Privileges
- Scope: Access Control, Authorization; Impact: Bypass Protection Mechanism

## Mitigations
- Strong input validation - All user-controllable input must be validated and filtered for illegal characters as well as LDAP content.
- Use of custom error pages - Attackers can glean information about the nature of queries from descriptive error messages. Input validation must be coupled with customized error pages that inform about an error without disclosing information about the LDAP or application.

## Related Weaknesses (CWE)
- CWE-77
- CWE-90
- CWE-20
