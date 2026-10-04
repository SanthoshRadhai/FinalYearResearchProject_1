# D3-AL: Account Locking

**Reference:** https://d3fend.mitre.org/technique/D3-AL/  

## Definition
The process of temporarily disabling user accounts on a system or domain.

## Parent Class(es)
- Credential Eviction

## Relationships
- **created:** 2020-08-05T00:00:00
- **disables:** User Account
- **kb-reference:** Reference - Account monitoring - Forescout Technologies
- **kb-reference:** Reference - Framework for notifying a directory service of authentication events processed outside the directory service - Oracle International Corp

## Knowledge Base Article
## How it works
Management servers with enterprise policies for account management provide the ability to enable and disable account for given rules. The rules may include specific periods of time (eg. weekend, plant shutdown, leave periods), specific user types or groups, or individual users.

## Considerations
* Local accounts caches vs centralized account management
* Single Sign-on
* Role based vs Attribute based systems

## Examples of account configuration stores
* Directory Services
* Active Directory
* RADIUS
* LDAP
* Oracle User Account Management
* JumpCloud
