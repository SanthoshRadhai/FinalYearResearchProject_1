# CWE-772: Missing Release of Resource after Effective Lifetime

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/772.html  

## Description
The product does not release a resource after its effective lifetime has ended, i.e., after the resource is no longer needed.

## Related Weaknesses
- ChildOf: CWE-404
- ChildOf: CWE-404
- ChildOf: CWE-404
- ChildOf: CWE-404

## Common Consequences
- Scope: Availability; Impact: DoS: Resource Consumption (Other), DoS: Resource Consumption (Memory), DoS: Resource Consumption (CPU) — An attacker that can influence the allocation of resources that are not properly released could deplete the available resource pool and prevent all other processes from accessing the same type of resource. Frequently-affected resources include memory, CPU, disk space, power or battery, etc.

## Potential Mitigations
- [Requirements] Use a language that does not allow this weakness to occur or provides constructs that make this weakness easier to avoid. For example, languages such as Java, Ruby, and Lisp perform automatic garbage collection that releases memory for objects that have been deallocated.
- [Implementation] It is good practice to be responsible for freeing all resources you allocate and to be consistent with how and where you free resources in a function. If you allocate resources that you intend to free upon completion of the function, you must be sure to free the resources at all exit points for that function including error conditions.
- [Operation, Architecture and Design] Use resource-limiting settings provided by the operating system or environment. For example, when managing system resources in POSIX, setrlimit() can be used to set limits for certain types of resources, and getrlimit() can determine how many resources are available. However, these functions are not available on all operating systems. When the current levels get close to the maximum that is defined for the application (see CWE-770), then limit the allocation of further resources to privileged users; alternately, begin releasing resources for less-privileged users. While this mitigation may protect the system from attack, it will not necessarily stop attackers from adversely impacting other users. Ensure that the application performs the appropriate error checks and error handling in case resources become unavailable (CWE-703).

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- The following method never closes the new file handle. Given enough time, the Finalize() method for BufferReader should eventually call Close(), but there is no guarantee as to how long this action will take. In fact, there is no guarantee that Finalize() will ever be invoked. In a busy environment, the Operating System could use up all of the available file handles before the Close() function is called.
- The following code attempts to open a new connection to a database, process the results returned by the database, and close the allocated SqlConnection object.
- This code attempts to open a connection to a database and catches any exceptions that may occur.
- Under normal conditions the following C# code executes a database query, processes the results returned by the database, and closes the allocated SqlConnection object. But if an exception occurs while executing the SQL or processing the results, the SqlConnection object is not closed. If this happens often enough, the database will run out of available cursors and not be able to execute any more SQL queries.
- The following C function does not close the file handle it opens if an error occurs. If the process is long-lived, the process can run out of file handles.
