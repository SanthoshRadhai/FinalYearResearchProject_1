# CAPEC-1: Accessing Functionality Not Properly Constrained by ACLs

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/1.html  

## Description
In applications, particularly web applications, access to functionality is mitigated by an authorization framework. This framework maps Access Control Lists (ACLs) to elements of the application's functionality; particularly URL's for web apps. In the case that the administrator failed to specify an ACL for a particular element, an attacker may be able to access it with impunity. An attacker with the ability to access functionality not properly constrained by ACLs can obtain sensitive information and possibly compromise the entire application. Such an attacker can access resources that must be available only to users at a higher privilege level, can access management sections of the application, or can run queries for data that they otherwise not supposed to.

## Related Attack Patterns
- ChildOf: CAPEC-122
- CanPrecede: CAPEC-17

## Prerequisites
- The application must be navigable in a manner that associates elements (subsections) of the application with ACLs.
- The various resources, or individual URLs, must be somehow discoverable by the attacker
- The administrator must have forgotten to associate an ACL or has associated an inappropriately permissive ACL with a particular navigable resource.

## Skills Required
- [Low] In order to discover unrestricted resources, the attacker does not need special tools or skills. They only have to observe the resources or access mechanisms invoked as each action is performed and then try and access those access mechanisms directly.

## Resources Required
- None: No specialized resources are required to execute this type of attack.

## Consequences
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges

## Mitigations
- In a J2EE setting, administrators can associate a role that is impossible for the authenticator to grant users, such as "NoAccess", with all Servlets to which access is guarded by a limited number of servlets visible to, and accessible by, the user. Having done so, any direct access to those protected Servlets will be prohibited by the web container. In a more general setting, the administrator must mark every resource besides the ones supposed to be exposed to the user as accessible by a role impossible for the user to assume. The default security setting must be to deny access and then grant access only to those resources intended by business logic.

## Related Weaknesses (CWE)
- CWE-276
- CWE-285
- CWE-434
- CWE-693
- CWE-732
- CWE-1191
- CWE-1193
- CWE-1220
- CWE-1297
- CWE-1311
- CWE-1314
- CWE-1315
- CWE-1318
- CWE-1320
- CWE-1321
- CWE-1327
