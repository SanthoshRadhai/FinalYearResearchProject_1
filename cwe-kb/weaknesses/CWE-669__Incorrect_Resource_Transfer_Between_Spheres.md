# CWE-669: Incorrect Resource Transfer Between Spheres

**Abstraction:** Class  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/669.html  

## Description
The product does not properly transfer a resource/behavior to another sphere, or improperly imports a resource/behavior from another sphere, in a manner that provides unintended control over that resource.

## Related Weaknesses
- ChildOf: CWE-664

## Common Consequences
- Scope: Confidentiality, Integrity; Impact: Read Application Data, Modify Application Data, Unexpected State

## Demonstrative Examples (summary)
- The following code demonstrates the unrestricted upload of a file with a Java servlet and a path traversal vulnerability. The action attribute of an HTML form is sending the upload file request to the Java servlet.
- This code includes an external script to get database credentials, then authenticates a user against the database, allowing access to the application.
- This code either generates a public HTML user information page or a JSON response containing the same user information.
