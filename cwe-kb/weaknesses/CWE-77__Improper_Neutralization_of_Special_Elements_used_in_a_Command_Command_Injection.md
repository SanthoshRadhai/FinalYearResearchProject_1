# CWE-77: Improper Neutralization of Special Elements used in a Command ('Command Injection')

**Abstraction:** Class  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/77.html  

## Description
The product constructs all or part of a command using externally-influenced input from an upstream component, but it does not neutralize or incorrectly neutralizes special elements that could modify the intended command when it is sent to a downstream component.

## Extended Description
Many protocols and products have their own custom command language. While OS or shell command strings are frequently discovered and targeted, developers may not realize that these other command languages might also be vulnerable to attacks.

## Related Weaknesses
- ChildOf: CWE-74
- ChildOf: CWE-74

## Common Consequences
- Scope: Integrity, Confidentiality, Availability; Impact: Execute Unauthorized Code or Commands — If a malicious user injects a character (such as a semi-colon) that delimits the end of one command and the beginning of another, it may be possible to then insert an entirely new and unrelated command that was not intended to be executed. This gives an attacker a privilege or capability that they would not otherwise have.

## Potential Mitigations
- [Architecture and Design] If at all possible, use library calls rather than external processes to recreate the desired functionality.
- [Implementation] If possible, ensure that all external commands called from the program are statically created.
- [Implementation] Assume all input is malicious. Use an "accept known good" input validation strategy, i.e., use a list of acceptable inputs that strictly conform to specifications. Reject any input that does not strictly conform to specifications, or transform it into something that does. When performing input validation, consider all potentially relevant properties, including length, type of input, the full range of acceptable values, missing or extra inputs, syntax, consistency across related fields, and conformance to business rules. As an example of business rule logic, "boat" may be syntactically valid because it only contains alphanumeric characters, but it is not valid if the input is only expected to contain colors such as "red" or "blue." Do not rely exclusively on looking for malicious or malformed inputs. This is likely to miss at least one undesirable input, especially if the code's environment changes. This can give attackers enough room to bypass the intended validation. However, denylists can be useful for detecting potential attacks or determining which inputs are so malformed that they should be rejected outright.
- [Operation] Run time: Run time policy enforcement may be used in an allowlist fashion to prevent use of any non-sanctioned commands.
- [System Configuration] Assign permissions that prevent the user from accessing/opening privileged files.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- Consider a "CWE Differentiator" application that uses an an LLM generative AI based "chatbot" to explain the difference between two weaknesses. As input, it accepts two CWE IDs, constructs a prompt string, sends the prompt to the chatbot, and prints the results. The prompt string effectively acts as a command to the chatbot component. Assume that invokeChatbot() calls the chatbot and returns the response as a string; the implementation details are not important here.
- Consider the following program. It intends to perform an "ls -l" on an input filename. The validate_name() subroutine performs validation on the input to make sure that only alphanumeric and "-" characters are allowed, which avoids path traversal (CWE-22) and OS command injection (CWE-78) weaknesses. Only filenames like "abc" or "d-e-f" are intended to be allowed.
- The following simple program accepts a filename as a command line argument and displays the contents of the file back to the user. The program is installed setuid root because it is intended for use as a learning tool to allow system administrators in-training to inspect privileged system files without giving them the ability to modify them or damage the system.
- The following code is from an administrative web application designed to allow users to kick off a backup of an Oracle database using a batch-file wrapper around the rman utility and then run a cleanup.bat script to delete some temporary files. The script rmanDB.bat accepts a single command line parameter, which specifies what type of backup to perform. Because access to the database is restricted, the application runs the backup as a privileged user.
