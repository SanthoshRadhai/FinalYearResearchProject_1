# CWE-96: Improper Neutralization of Directives in Statically Saved Code ('Static Code Injection')

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/96.html  

## Description
The product receives input from an upstream component, but it does not neutralize or incorrectly neutralizes code syntax before inserting the input into an executable resource, such as a library, configuration file, or template.

## Related Weaknesses
- ChildOf: CWE-94

## Common Consequences
- Scope: Confidentiality; Impact: Read Files or Directories, Read Application Data — The injected code could access restricted data / files.
- Scope: Access Control; Impact: Bypass Protection Mechanism — In some cases, injectable code controls authentication; this may lead to a remote vulnerability.
- Scope: Access Control; Impact: Gain Privileges or Assume Identity — Injected code can access resources that the attacker is directly prevented from accessing.
- Scope: Integrity, Confidentiality, Availability, Other; Impact: Execute Unauthorized Code or Commands — Code injection attacks can lead to loss of data integrity in nearly all cases as the control-plane data injected is always incidental to data recall or writing. Additionally, code injection can often result in the execution of arbitrary code.
- Scope: Non-Repudiation; Impact: Hide Activities — Often the actions performed by injected control code are unlogged.

## Potential Mitigations
- [Implementation] Assume all input is malicious. Use an "accept known good" input validation strategy, i.e., use a list of acceptable inputs that strictly conform to specifications. Reject any input that does not strictly conform to specifications, or transform it into something that does. When performing input validation, consider all potentially relevant properties, including length, type of input, the full range of acceptable values, missing or extra inputs, syntax, consistency across related fields, and conformance to business rules. As an example of business rule logic, "boat" may be syntactically valid because it only contains alphanumeric characters, but it is not valid if the input is only expected to contain colors such as "red" or "blue." Do not rely exclusively on looking for malicious or malformed inputs. This is likely to miss at least one undesirable input, especially if the code's environment changes. This can give attackers enough room to bypass the intended validation. However, denylists can be useful for detecting potential attacks or determining which inputs are so malformed that they should be rejected outright.
- [Implementation] Perform proper output validation and escaping to neutralize all code syntax from data written to code files.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- This example attempts to write user messages to a message file and allow users to view them.
