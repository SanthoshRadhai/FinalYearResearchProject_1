# CWE-594: J2EE Framework: Saving Unserializable Objects to Disk

**Abstraction:** Variant  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/594.html  

## Description
When the J2EE container attempts to write unserializable objects to disk there is no guarantee that the process will complete successfully.

## Extended Description
In heavy load conditions, most J2EE application frameworks flush objects to disk to manage memory requirements of incoming requests. For example, session scoped objects, and even application scoped objects, are written to disk when required. While these application frameworks do the real work of writing objects to disk, they do not enforce that those objects be serializable, thus leaving the web application vulnerable to crashes induced by serialization failure. An attacker may be able to mount a denial of service attack by sending enough requests to the server to force the web application to save objects to disk.

## Related Weaknesses
- ChildOf: CWE-1076

## Common Consequences
- Scope: Integrity; Impact: Modify Application Data — Data represented by unserializable objects can be corrupted.
- Scope: Availability; Impact: DoS: Crash, Exit, or Restart — Non-serializability of objects can lead to system crash.

## Potential Mitigations
- [Architecture and Design, Implementation] All objects that become part of session and application scope must implement the java.io.Serializable interface to ensure serializability of containing objects.

## Demonstrative Examples (summary)
- In the following Java example, a Customer Entity JavaBean provides access to customer information in a database for a business application. The Customer Entity JavaBean is used as a session scoped object to return customer information to a Session EJB.
