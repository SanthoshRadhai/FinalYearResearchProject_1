# CAPEC-127: Directory Indexing

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/127.html  

## Description
An adversary crafts a request to a target that results in the target listing/indexing the content of a directory as output. One common method of triggering directory contents as output is to construct a request containing a path that terminates in a directory name rather than a file name since many applications are configured to provide a list of the directory's contents when such a request is received. An adversary can use this to explore the directory tree on a target as well as learn the names of files. This can often end up revealing test files, backup files, temporary files, hidden files, configuration files, user accounts, script contents, as well as naming conventions, all of which can be used by an attacker to mount additional attacks.

## Related Attack Patterns
- ChildOf: CAPEC-54

## Prerequisites
- The target must be misconfigured to return a list of a directory's content when it receives a request that ends in a directory name rather than a file name.
- The adversary must be able to control the path that is requested of the target.
- The administrator must have failed to properly configure an ACL or has associated an overly permissive ACL with a particular directory.
- The server version or patch level must not inherently prevent known directory listing attacks from working.

## Skills Required
- [Low] To issue the request to URL without given a specific file name
- [High] To bypass the access control of the directory of listings

## Resources Required
- Ability to send HTTP requests to a web application.

## Consequences
- Scope: Confidentiality; Impact: Read Data

## Mitigations
- 1. Using blank index.html: putting blank index.html simply prevent directory listings from displaying to site visitors.
- 2. Preventing with .htaccess in Apache web server: In .htaccess, write "Options-indexes".
- 3. Suppressing error messages: using error 403 "Forbidden" message exactly like error 404 "Not Found" message.

## Related Weaknesses (CWE)
- CWE-424
- CWE-425
- CWE-288
- CWE-285
- CWE-732
- CWE-276
- CWE-693
