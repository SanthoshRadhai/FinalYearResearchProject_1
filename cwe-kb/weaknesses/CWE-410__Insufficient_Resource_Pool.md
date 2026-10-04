# CWE-410: Insufficient Resource Pool

**Abstraction:** Class  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/410.html  

## Description
The product's resource pool is not large enough to handle peak demand, which allows an attacker to prevent others from accessing the resource by using a (relatively) large number of requests for resources.

## Extended Description
Frequently the consequence is a "flood" of connection or sessions.

## Related Weaknesses
- ChildOf: CWE-664
- CanPrecede: CWE-400

## Common Consequences
- Scope: Availability, Integrity, Other; Impact: DoS: Crash, Exit, or Restart, Other — Floods often cause a crash or other problem besides denial of the resource itself; these are likely examples of *other* vulnerabilities, not an insufficient resource pool.

## Potential Mitigations
- [Architecture and Design] Do not perform resource-intensive transactions for unauthenticated users and/or invalid requests.
- [Architecture and Design] Consider implementing a velocity check mechanism which would detect abusive behavior.
- [Operation] Consider load balancing as an option to handle heavy loads.
- [Implementation] Make sure that resource handles are properly closed when no longer needed.
- [Architecture and Design] Identify the system's resource intensive operations and consider protecting them from abuse (e.g. malicious automated script which runs the resources out).

## Demonstrative Examples (summary)
- In the following snippet from a Tomcat configuration file, a JDBC connection pool is defined with a maximum of 5 simultaneous connections (with a 60 second timeout). In this case, it may be trivial for an attacker to instigate a denial of service (DoS) by using up all of the available connections in the pool.
