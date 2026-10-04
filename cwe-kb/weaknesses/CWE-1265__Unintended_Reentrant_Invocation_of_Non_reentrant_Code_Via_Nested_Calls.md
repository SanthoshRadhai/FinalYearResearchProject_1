# CWE-1265: Unintended Reentrant Invocation of Non-reentrant Code Via Nested Calls

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/1265.html  

## Description
The product invokes code that is believed to be reentrant, but the code performs a call that unintentionally produces a nested invocation of the non-reentrant code.

## Extended Description
In a complex product, a single function call may lead to many different possible code paths, some of which may involve deeply nested calls. It may be difficult to foresee all possible code paths that could emanate from a given function call, even if that call is assumed to be reentrant. In some systems, an external actor can manipulate inputs to the system and thereby achieve a wide range of possible control flows. This is frequently a concern in products that execute scripts from untrusted sources. Examples of such products are web browsers and PDF readers. A weakness is present when one of the possible code paths resulting from a function call alters program state that the original caller assumes to be unchanged during the call.

## Related Weaknesses
- ChildOf: CWE-662
- PeerOf: CWE-663
- CanPrecede: CWE-416

## Common Consequences
- Scope: Integrity; Impact: Unexpected State — Exploitation of this weakness can leave the application in an unexpected state and cause variables to be reassigned before the first invocation has completed. This may eventually result in memory corruption or unexpected code execution.

## Potential Mitigations
- [Architecture and Design] When architecting a system that will execute untrusted code in response to events, consider executing the untrusted event handlers asynchronously (asynchronous message passing) as opposed to executing them synchronously at the time each event fires. The untrusted code should execute at the start of the next iteration of the thread's message loop. In this way, calls into non-reentrant code are strictly serialized, so that each operation completes fully before the next operation begins. Special attention must be paid to all places where type coercion may result in script execution. Performing all needed coercions at the very beginning of an operation can help reduce the chance of operations executing at unexpected junctures.
- [Implementation] Make sure the code (e.g., function or class) in question is reentrant by not leveraging non-local data, not modifying its own code, and not calling other non-reentrant code.

## Demonstrative Examples (summary)
- The implementation of the Widget class in the following C++ code is an example of code that is not designed to be reentrant. If an invocation of a method of Widget inadvertently produces a second nested invocation of a method of Widget, then data member backgroundImage may unexpectedly change during execution of the outer call.
- This is another example of C++ code that is not designed to be reentrant.
