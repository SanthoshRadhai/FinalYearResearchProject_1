# CWE-74: Improper Neutralization of Special Elements in Output Used by a Downstream Component ('Injection')

**Abstraction:** Class  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/74.html  

## Description
The product constructs all or part of a command, data structure, or record using externally-influenced input from an upstream component, but it does not neutralize or incorrectly neutralizes special elements that could modify how it is parsed or interpreted when it is sent to a downstream component.

## Related Weaknesses
- ChildOf: CWE-707

## Common Consequences
- Scope: Confidentiality; Impact: Read Application Data — Many injection attacks involve the disclosure of important information -- in terms of both data sensitivity and usefulness in further exploitation.
- Scope: Access Control; Impact: Bypass Protection Mechanism — In some cases, injectable code controls authentication; this may lead to a remote vulnerability.
- Scope: Other; Impact: Alter Execution Logic — Injection attacks are characterized by the ability to significantly change the flow of a given process, and in some cases, to the execution of arbitrary code.
- Scope: Integrity, Other; Impact: Other — Data injection attacks lead to loss of data integrity in nearly all cases as the control-plane data injected is always incidental to data recall or writing.
- Scope: Non-Repudiation; Impact: Hide Activities — Often the actions performed by injected control code are unlogged.

## Potential Mitigations
- [Requirements] Programming languages and supporting technologies might be chosen which are not subject to these issues.
- [Implementation] Utilize an appropriate mix of allowlist and denylist parsing to filter control-plane syntax from all input.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- This example code intends to take the name of a user and list the contents of that user's home directory. It is subject to the first variant of OS command injection.
- The following code segment reads the name of the author of a weblog entry, author, from an HTTP request and sets it in a cookie header of an HTTP response.
- Consider the following program. It intends to perform an "ls -l" on an input filename. The validate_name() subroutine performs validation on the input to make sure that only alphanumeric and "-" characters are allowed, which avoids path traversal (CWE-22) and OS command injection (CWE-78) weaknesses. Only filenames like "abc" or "d-e-f" are intended to be allowed.
- Consider a "CWE Differentiator" application that uses an an LLM generative AI based "chatbot" to explain the difference between two weaknesses. As input, it accepts two CWE IDs, constructs a prompt string, sends the prompt to the chatbot, and prints the results. The prompt string effectively acts as a command to the chatbot component. Assume that invokeChatbot() calls the chatbot and returns the response as a string; the implementation details are not important here.
- The following code is a workflow job written using YAML. The code attempts to download pull request artifacts, unzip from the artifact called pr.zip and extract the value of the file NR into a variable "pr_number" that will be used later in another job. It attempts to create a github workflow environment variable, writing to $GITHUB_ENV. The environment variable value is retrieved from an external resource.
