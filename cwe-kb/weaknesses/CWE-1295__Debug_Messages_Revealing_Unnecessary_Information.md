# CWE-1295: Debug Messages Revealing Unnecessary Information

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/1295.html  

## Description
The product fails to adequately prevent the revealing of unnecessary and potentially sensitive system information within debugging messages.

## Extended Description
Debug messages are messages that help troubleshoot an issue by revealing the internal state of the system. For example, debug data in design can be exposed through internal memory array dumps or boot logs through interfaces like UART via TAP commands, scan chain, etc. Thus, the more information contained in a debug message, the easier it is to debug. However, there is also the risk of revealing information that could help an attacker either decipher a vulnerability, and/or gain a better understanding of the system. Thus, this extra information could lower the "security by obscurity" factor. While "security by obscurity" alone is insufficient, it can help as a part of "Defense-in-depth".

## Related Weaknesses
- ChildOf: CWE-200
- PeerOf: CWE-209

## Common Consequences
- Scope: Confidentiality, Integrity, Availability, Access Control, Accountability, Authentication, Authorization, Non-Repudiation; Impact: Read Memory, Bypass Protection Mechanism, Gain Privileges or Assume Identity, Varies by Context

## Potential Mitigations
- [Implementation] Ensure that a debug message does not reveal any unnecessary information during the debug process for the intended response.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- This example here shows how an attacker can take advantage of unnecessary information in debug messages.
