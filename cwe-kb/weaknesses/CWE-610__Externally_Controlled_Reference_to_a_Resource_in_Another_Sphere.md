# CWE-610: Externally Controlled Reference to a Resource in Another Sphere

**Abstraction:** Class  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/610.html  

## Description
The product uses an externally controlled name or reference that resolves to a resource that is outside of the intended control sphere.

## Related Weaknesses
- ChildOf: CWE-664

## Common Consequences
- Scope: Confidentiality, Integrity; Impact: Read Application Data, Modify Application Data — An adversary could read or modify data, depending on how the resource is intended to be used.
- Scope: Access Control; Impact: Gain Privileges or Assume Identity — An adversary that can supply a reference to an unintended resource can potentially access a resource that they do not have privileges for, thus bypassing existing access control mechanisms.

## Demonstrative Examples (summary)
- The following code is a Java servlet that will receive a GET request with a url parameter in the request to redirect the browser to the address specified in the url parameter. The servlet will retrieve the url parameter value from the request and send a response to redirect the browser to the url address.
