# CAPEC-676: NoSQL Injection

**Abstraction:** Standard  
**Status:** Stable  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/676.html  

## Description
An adversary targets software that constructs NoSQL statements based on user input or with parameters vulnerable to operator replacement in order to achieve a variety of technical impacts such as escalating privileges, bypassing authentication, and/or executing code.

## Related Attack Patterns
- ChildOf: CAPEC-248

## Prerequisites
- Awareness of the technology stack being leveraged by the target application.
- NoSQL queries used by the application to store, retrieve, or modify data.
- User-controllable input that is not properly validated by the application as part of NoSQL queries.
- Target potentially susceptible to operator replacement attacks.

## Skills Required
- [Low] For keyword and JavaScript injection attacks, it is fairly simple for someone with basic NoSQL knowledge to perform NoSQL injection, once the target's technology stack has been determined.
- [Medium] For operator replacement attacks, the adversary must also have knowledge of HTTP Parameter Pollution attacks and how to conduct them.

## Resources Required
- None: No specialized resources are required to execute this type of attack.

## Consequences
- Scope: Integrity; Impact: Modify Data
- Scope: Confidentiality; Impact: Read Data
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges

## Mitigations
- Strong input validation - All user-controllable input must be validated and filtered for illegal characters as well as relevant NoSQL and JavaScript content. NoSQL-specific keywords, such as $ne, $eq or $gt for MongoDB, must be filtered in addition to characters such as a single-quote(') or semicolons (;) based on the context in which they appear. Validation should also extend to expected types.
- If possible, leverage safe APIs (e.g., PyMongo and Flask-PyMongo for Python and MongoDB) for queries as opposed to building queries from strings.
- Ensure the most recent version of a NoSQL database and it's corresponding API are used by the application.
- Use of custom error pages - Adversaries can glean information about the nature of queries from descriptive error messages. Input validation must be coupled with customized error pages that inform about an error without disclosing information about the database or application.
- Exercise the principle of Least Privilege with regards to application accounts to minimize damage if a NoSQL injection attack is successful.
- If using MongoDB, disable server-side JavaScript execution and leverage a sanitization module such as "mongo-sanitize".
- If using PHP with MongoDB, ensure all special query operators (starting with $) use single quotes to prevent operator replacement attacks.
- Additional mitigations will depend on the NoSQL database, API, and programming language leveraged by the application.

## Related Weaknesses (CWE)
- CWE-943
- CWE-1286
