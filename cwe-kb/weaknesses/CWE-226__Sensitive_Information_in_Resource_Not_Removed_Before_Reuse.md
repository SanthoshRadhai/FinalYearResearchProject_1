# CWE-226: Sensitive Information in Resource Not Removed Before Reuse

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/226.html  

## Description
The product releases a resource such as memory or a file so that it can be made available for reuse, but it does not clear or "zeroize" the information contained in the resource before the product performs a critical state transition or makes the resource available for reuse by other entities.

## Extended Description
When resources are released, they can be made available for reuse. For example, after memory is de-allocated, an operating system may make the memory available to another process, or disk space may be reallocated when a file is deleted. As removing information requires time and additional resources, operating systems do not usually clear the previously written information. Even when the resource is reused by the same process, this weakness can arise when new data is not as large as the old data, which leaves portions of the old data still available. Equivalent errors can occur in other situations where the length of data is variable but the associated data structure is not. If memory is not cleared after use, the information may be read by less trustworthy parties when the memory is reallocated. This weakness can apply in hardware, such as when a device or system switches between power, sleep, or debug states during normal operation, or when execution changes to different users or privilege levels.

## Related Weaknesses
- ChildOf: CWE-459
- ChildOf: CWE-212
- CanPrecede: CWE-201

## Common Consequences
- Scope: Confidentiality; Impact: Read Application Data

## Potential Mitigations
- [Architecture and Design, Implementation] During critical state transitions, information not needed in the next state should be removed or overwritten with fixed patterns (such as all 0's) or random data, before the transition to the next state.
- [Architecture and Design, Implementation] When releasing, de-allocating, or deleting a resource, overwrite its data and relevant metadata with fixed patterns or random data. Be cautious about complex resource types whose underlying representation might be non-contiguous or change at a low level, such as how a file might be split into different chunks on a file system, even though "logical" file positions are contiguous at the application layer. Such resource types might require invocation of special modes or APIs to tell the underlying operating system to perform the necessary clearing, such as SDelete (Secure Delete) on Windows, although the appropriate functionality might not be available at the application layer.

## Detection Methods
- [Manual Analysis] Write a known pattern into each sensitive location. Trigger the release of the resource or cause the desired state transition to occur. Read data back from the sensitive locations. If the reads are successful, and the data is the same as the pattern that was originally written, the test fails and the product needs to be fixed. Note that this test can likely be automated.
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- This example shows how an attacker can take advantage of an incorrect state transition.
- The following code calls realloc() on a buffer containing sensitive data:
- The following example code is excerpted from the AES wrapper/interface, aes0_wrapper, module of one of the AES engines (AES0) in the Hack@DAC'21 buggy OpenPiton System-on-Chip (SoC). Note that this SoC contains three distinct AES engines. Within this wrapper module, four 32-bit registers are utilized to store the message intended for encryption, referred to as p_c[i]. Using the AXI Lite interface, these registers are filled with the 128-bit message to be encrypted.
