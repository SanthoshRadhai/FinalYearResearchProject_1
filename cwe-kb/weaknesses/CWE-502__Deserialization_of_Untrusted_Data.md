# CWE-502: Deserialization of Untrusted Data

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/502.html  

## Description
The product deserializes untrusted data without sufficiently ensuring that the resulting data will be valid.

## Related Weaknesses
- ChildOf: CWE-913
- ChildOf: CWE-913
- PeerOf: CWE-915

## Common Consequences
- Scope: Integrity; Impact: Modify Application Data, Unexpected State — Attackers can modify unexpected objects or data that was assumed to be safe from modification. Deserialized data or code could be modified without using the provided accessor functions, or unexpected functions could be invoked.
- Scope: Availability; Impact: DoS: Resource Consumption (CPU) — If a function is making an assumption on when to terminate, based on a sentry in a string, it could easily never terminate.
- Scope: Other; Impact: Varies by Context — The consequences can vary widely, because it depends on which objects or methods are being deserialized, and how they are used. Making an assumption that the code in the deserialized object is valid is dangerous and can enable exploitation. One example is attackers using gadget chains to perform unauthorized actions, such as generating a shell.

## Potential Mitigations
- [Architecture and Design, Implementation] If available, use the signing/sealing features of the programming language to assure that deserialized data has not been tainted. For example, a hash-based message authentication code (HMAC) could be used to ensure that data has not been modified.
- [Implementation] When deserializing data, populate a new object rather than just deserializing. The result is that the data flows through safe input validation and that the functions are safe.
- [Implementation] Explicitly define a final object() to prevent deserialization.
- [Architecture and Design, Implementation] Make fields transient to protect them from deserialization. An attempt to serialize and then deserialize a class containing transient fields will result in NULLs where the transient data should be. This is an excellent way to prevent time, environment-based, or sensitive variables from being carried over and used improperly.
- [Implementation] Avoid having unnecessary types or gadgets (a sequence of instances and method invocations that can self-execute during the deserialization process, often found in libraries) available that can be leveraged for malicious ends. This limits the potential for unintended or unauthorized types and gadgets to be leveraged by the attacker. Add only acceptable classes to an allowlist. Note: new gadgets are constantly being discovered, so this alone is not a sufficient mitigation.
- [Architecture and Design, Implementation] Employ cryptography of the data or code for protection. However, it's important to note that it would still be client-side security. This is risky because if the client is compromised then the security implemented on the client (the cryptography) can be bypassed.
- [Operation] Use an application firewall that can detect attacks against this weakness. It can be beneficial in cases in which the code cannot be fixed (because it is controlled by a third party), as an emergency prevention measure while more comprehensive software assurance measures are applied, or to provide defense in depth [REF-1481].

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- This code snippet deserializes an object from a file and uses it as a UI button:
- In Python, the Pickle library handles the serialization and deserialization processes. In this example derived from [REF-467], the code receives and parses data, and afterwards tries to authenticate a user based on validating a token.
