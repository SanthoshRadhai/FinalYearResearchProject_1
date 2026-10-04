# CWE-404: Improper Resource Shutdown or Release

**Abstraction:** Class  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/404.html  

## Description
The product does not release or incorrectly releases a resource before it is made available for re-use.

## Extended Description
When a resource is created or allocated, the developer is responsible for properly releasing the resource as well as accounting for all potential paths of expiration or invalidation, such as a set period of time or revocation.

## Related Weaknesses
- ChildOf: CWE-664
- PeerOf: CWE-405
- CanPrecede: CWE-619

## Common Consequences
- Scope: Availability, Other; Impact: DoS: Resource Consumption (Other), Varies by Context — Most unreleased resource issues result in general software reliability problems, but if an attacker can intentionally trigger a resource leak, the attacker might be able to launch a denial of service attack by depleting the resource pool.
- Scope: Confidentiality; Impact: Read Application Data — When a resource containing sensitive information is not correctly shutdown, it may expose the sensitive data in a subsequent allocation.

## Potential Mitigations
- [Requirements] Use a language that does not allow this weakness to occur or provides constructs that make this weakness easier to avoid. For example, languages such as Java, Ruby, and Lisp perform automatic garbage collection that releases memory for objects that have been deallocated.
- [Implementation] It is good practice to be responsible for freeing all resources you allocate and to be consistent with how and where you free memory in a function. If you allocate memory that you intend to free upon completion of the function, you must be sure to free the memory at all exit points for that function including error conditions.
- [Implementation] Memory should be allocated/freed using matching functions such as malloc/free, new/delete, and new[]/delete[].
- [Implementation] When releasing a complex object or structure, ensure that you properly dispose of all of its member components, not just the object itself.

## Detection Methods
- [Automated Dynamic Analysis] This weakness can be detected using dynamic tools and techniques that interact with the software using large test suites with many diverse inputs, such as fuzz testing (fuzzing), robustness testing, and fault injection. The software's operation may slow down, but it should not become unstable, crash, or generate incorrect results. Resource clean up errors might be detected with a stress-test by calling the software simultaneously from a large number of threads or processes, and look for evidence of any unexpected behavior. The software's operation may slow down, but it should not become unstable, crash, or generate incorrect results.
- [Manual Dynamic Analysis] Identify error conditions that are not likely to occur during normal usage and trigger them. For example, run the product under low memory conditions, run with insufficient privileges or permissions, interrupt a transaction before it is completed, or disable connectivity to basic network services such as DNS. Monitor the software for any unexpected behavior. If you trigger an unhandled exception or similar error that was discovered and handled by the application's environment, it may still indicate unexpected conditions that were not handled by the application itself.
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- The following method never closes the new file handle. Given enough time, the Finalize() method for BufferReader should eventually call Close(), but there is no guarantee as to how long this action will take. In fact, there is no guarantee that Finalize() will ever be invoked. In a busy environment, the Operating System could use up all of the available file handles before the Close() function is called.
- This code attempts to open a connection to a database and catches any exceptions that may occur.
- Under normal conditions the following C# code executes a database query, processes the results returned by the database, and closes the allocated SqlConnection object. But if an exception occurs while executing the SQL or processing the results, the SqlConnection object is not closed. If this happens often enough, the database will run out of available cursors and not be able to execute any more SQL queries.
- The following C function does not close the file handle it opens if an error occurs. If the process is long-lived, the process can run out of file handles.
- In this example, the program does not use matching functions such as malloc/free, new/delete, and new[]/delete[] to allocate/deallocate the resource.
- In this example, the program calls the delete[] function on non-heap memory.
