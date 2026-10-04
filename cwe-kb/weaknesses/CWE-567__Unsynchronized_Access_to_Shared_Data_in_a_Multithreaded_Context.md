# CWE-567: Unsynchronized Access to Shared Data in a Multithreaded Context

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/567.html  

## Description
The product does not properly synchronize shared data, such as static variables across threads, which can lead to undefined behavior and unpredictable data changes.

## Extended Description
Within servlets, shared static variables are not protected from concurrent access, but servlets are multithreaded. This is a typical programming mistake in J2EE applications, since the multithreading is handled by the framework. When a shared variable can be influenced by an attacker, one thread could wind up modifying the variable to contain data that is not valid for a different thread that is also using the data within the variable. Note that this weakness is not unique to servlets.

## Related Weaknesses
- ChildOf: CWE-820
- ChildOf: CWE-662
- ChildOf: CWE-662
- CanPrecede: CWE-488

## Common Consequences
- Scope: Confidentiality, Integrity, Availability; Impact: Read Application Data, Modify Application Data, DoS: Instability, DoS: Crash, Exit, or Restart — If the shared variable contains sensitive data, it may be manipulated or displayed in another user session. If this data is used to control the application, its value can be manipulated to cause the application to crash or perform poorly.

## Potential Mitigations
- [Implementation] Remove the use of static variables used between servlets. If this cannot be avoided, use synchronized access for these variables.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- The following code implements a basic counter for how many times the page has been accesed.
